from policyengine_us.model_api import *


class ri_ccap_provider_rate(Variable):
    value_type = float
    entity = Person
    label = "Rhode Island CCAP weekly provider reimbursement rate"
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.RI
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.12"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.rates
        provider_type = person("ri_ccap_provider_type", period)
        time_category = person("ri_ccap_time_category", period)
        star_rating = person("ri_ccap_star_rating", period)
        step_rating = person("ri_ccap_step_rating", period)
        center_age = person("ri_ccap_center_age_group", period)
        family_age = person("ri_ccap_family_age_group", period)

        PT = provider_type.possible_values
        TC = time_category.possible_values

        is_center = provider_type == PT.LICENSED_CENTER
        is_family = provider_type == PT.LICENSED_FAMILY

        # Look up rate by time category for each provider type
        center_rate = _lookup_rate(
            p.licensed_center, time_category, TC, star_rating, center_age
        )
        family_rate = _lookup_rate(
            p.licensed_family, time_category, TC, star_rating, family_age
        )
        exempt_rate = _lookup_rate(
            p.licensed_exempt, time_category, TC, step_rating, family_age
        )

        return select(
            [is_center, is_family],
            [center_rate, family_rate],
            default=exempt_rate,
        )


def _lookup_rate(rates, time_category, TC, quality_rating, age_group):
    ft = rates.full_time[quality_rating][age_group]
    tqt = rates.three_quarter_time[quality_rating][age_group]
    ht = rates.half_time[quality_rating][age_group]
    qt = rates.quarter_time[quality_rating][age_group]
    return select(
        [
            time_category == TC.FULL_TIME,
            time_category == TC.THREE_QUARTER_TIME,
            time_category == TC.HALF_TIME,
        ],
        [ft, tqt, ht],
        default=qt,
    )
