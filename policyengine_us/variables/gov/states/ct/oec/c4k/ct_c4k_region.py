from policyengine_us.model_api import *


class CTC4KRegion(Enum):
    EASTERN = "Eastern"
    NORTH_CENTRAL = "North Central"
    NORTHWEST = "Northwest"
    SOUTH_CENTRAL = "South Central"
    SOUTHWEST = "Southwest"


class ct_c4k_region(Variable):
    value_type = Enum
    entity = Household
    possible_values = CTC4KRegion
    default_value = CTC4KRegion.NORTH_CENTRAL
    definition_period = MONTH
    defined_for = StateCode.CT
    label = "Connecticut Care 4 Kids geographic region"
    reference = "https://www.ctoec.org/care-4-kids/c4k-providers/c4k-rates/"

    def formula(household, period, parameters):
        # C4K regions are defined by town, not county. CT abolished county
        # government and towns from the same county can fall in different C4K
        # regions (e.g., Danbury is Northwest but Bridgeport is Southwest,
        # both in Fairfield County). This uses a county approximation since
        # PolicyEngine lacks town-level geography. Some families near region
        # boundaries may receive incorrect rates.
        county = household("county_str", period)
        p = parameters(period).gov.states.ct.oec.c4k.region

        eastern = np.isin(county, p.eastern)
        northwest = np.isin(county, p.northwest)
        south_central = np.isin(county, p.south_central)
        southwest = np.isin(county, p.southwest)

        return select(
            [eastern, northwest, south_central, southwest],
            [
                CTC4KRegion.EASTERN,
                CTC4KRegion.NORTHWEST,
                CTC4KRegion.SOUTH_CENTRAL,
                CTC4KRegion.SOUTHWEST,
            ],
            default=CTC4KRegion.NORTH_CENTRAL,
        )
