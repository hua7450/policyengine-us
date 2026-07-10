from policyengine_us.model_api import *


class or_erdc_maximum_monthly_rate(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    unit = USD
    label = "Oregon ERDC maximum monthly provider reimbursement"
    defined_for = "or_erdc_eligible_child"
    reference = "https://www.oregon.gov/delc/programs/pages/rates.aspx"

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
                [hourly_rate * hours, part_time_rate, monthly_rate],
                default=0,
            ),
            0,
        )
