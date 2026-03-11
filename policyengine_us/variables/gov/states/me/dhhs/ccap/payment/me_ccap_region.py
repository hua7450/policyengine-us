from policyengine_us.model_api import *


class MECCAPRegion(Enum):
    REGION_1 = "Region 1"
    REGION_2 = "Region 2"


class me_ccap_region(Variable):
    value_type = Enum
    entity = Household
    possible_values = MECCAPRegion
    default_value = MECCAPRegion.REGION_2
    definition_period = MONTH
    defined_for = StateCode.ME
    label = "Maine CCAP geographic region"
    reference = "https://www.maine.gov/dhhs/sites/maine.gov.dhhs/files/inline-files/CCAP%20Full%20Rule%208.18.2025_1.pdf#page=25"

    def formula(household, period, parameters):
        county = household("county_str", period)
        p = parameters(period).gov.states.me.dhhs.ccap
        is_region_1 = np.isin(county, p.region_1_counties)
        return where(
            is_region_1,
            MECCAPRegion.REGION_1,
            MECCAPRegion.REGION_2,
        )
