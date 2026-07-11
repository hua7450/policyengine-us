from policyengine_us.model_api import *


class or_erdc_maximum_monthly_rate(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    unit = USD
    label = "Oregon ERDC maximum monthly provider reimbursement"
    defined_for = "or_erdc_eligible_child"
    reference = (
        "https://secure.sos.state.or.us/oard/view.action?ruleNumber=414-175-0075"
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states["or"].delc.erdc.rates
        provider_type = person("or_erdc_provider_type", period)
        tiered_provider_type = person("or_erdc_tiered_provider_type", period)
        area = person("or_erdc_provider_area", period)
        age_group = person("or_erdc_age_group", period)
        hourly_rate = p.hourly[area][provider_type][age_group]
        part_time_rate = p.part_time[area][tiered_provider_type][age_group]
        monthly_rate = p.monthly[area][provider_type][age_group]
        hours = person("or_erdc_monthly_care_hours", period)

        # OAR 414-175-0076(2): for children eligible for the high needs rate,
        # an assessed factor (0-2) adds $5 per hour on hourly billing or $840
        # on monthly billing, in addition to the base provider rate.
        factors = person("or_erdc_high_needs_factors", period.this_year)
        high_needs = person("or_erdc_high_needs_rate_eligible", period.this_year)
        supplement = p.high_needs_supplement
        hourly_supplement = where(high_needs, factors * supplement.hourly * hours, 0)
        monthly_supplement = where(high_needs, factors * supplement.monthly, 0)

        # OAR 414-175-0075(3),(6): hourly billing is the lesser of hours times
        # the hourly rate and the full-time monthly rate, which also keeps the
        # reimbursement monotonic across the monthly-billing threshold.
        hourly_payment = min_(hourly_rate * hours, monthly_rate) + hourly_supplement

        tier = person("or_erdc_billing_tier", period)
        tiers = tier.possible_values
        return where(
            hours > 0,
            select(
                [
                    tier == tiers.HOURLY,
                    tier == tiers.PART_TIME,
                    tier == tiers.MONTHLY,
                ],
                [
                    hourly_payment,
                    part_time_rate + monthly_supplement,
                    monthly_rate + monthly_supplement,
                ],
                default=0,
            ),
            0,
        )
