from policyengine_us.model_api import *


class pa_ccw_market_rate(Variable):
    value_type = float
    entity = Person
    unit = USD
    label = "Pennsylvania CCW MCCA daily rate per child"
    definition_period = MONTH
    defined_for = "pa_ccw_eligible_child"
    reference = "https://www.pacodeandbulletin.gov/secure/pacode/data/055/chapter3042/055_3042.pdf#page=32"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.pa.dhs.ccw.rates
        provider_type = person("pa_ccw_provider_type", period)
        age_group = person("pa_ccw_age_group", period)
        time_category = person("pa_ccw_time_category", period)
        region = person.household("pa_ccw_region", period.this_year)

        def rate_for_region(region_param):
            return region_param[provider_type][age_group][time_category]

        return select(
            [
                region == 1,
                region == 2,
                region == 3,
                region == 4,
                region == 5,
                region == 6,
                region == 7,
                region == 8,
                region == 9,
                region == 10,
                region == 11,
                region == 12,
                region == 13,
                region == 14,
                region == 15,
                region == 16,
                region == 17,
                region == 18,
            ],
            [
                rate_for_region(p.region_1),
                rate_for_region(p.region_2),
                rate_for_region(p.region_3),
                rate_for_region(p.region_4),
                rate_for_region(p.region_5),
                rate_for_region(p.region_6),
                rate_for_region(p.region_7),
                rate_for_region(p.region_8),
                rate_for_region(p.region_9),
                rate_for_region(p.region_10),
                rate_for_region(p.region_11),
                rate_for_region(p.region_12),
                rate_for_region(p.region_13),
                rate_for_region(p.region_14),
                rate_for_region(p.region_15),
                rate_for_region(p.region_16),
                rate_for_region(p.region_17),
                rate_for_region(p.region_18),
            ],
            default=rate_for_region(p.region_19),
        )
