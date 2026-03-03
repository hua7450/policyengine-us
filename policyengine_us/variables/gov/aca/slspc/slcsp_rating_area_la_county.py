from policyengine_us.model_api import *


class slcsp_rating_area_la_county(Variable):
    value_type = int
    entity = Household
    label = "Second-lowest ACA silver-plan cost rating area in Los Angeles County"
    definition_period = YEAR
    defined_for = "in_la"

    def formula(household, period, parameters):
        zip3 = household("three_digit_zip_code", period)
        p = parameters(period).gov.aca
        is_in_la = household("in_la", period)
        has_zip = zip3 != ""
        can_lookup = is_in_la & has_zip
        result = np.zeros(zip3.shape, dtype=int)
        if can_lookup.any():
            result[can_lookup] = p.la_county_rating_area[zip3[can_lookup]]
        return result
