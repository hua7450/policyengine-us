from policyengine_us.model_api import *


class SouthCounty(Enum):
    ATLANTA = "Atlanta"
    BALTIMORE = "Baltimore"
    DALLAS_FT_WORTH = "Dallas-Ft. Worth"
    HOUSTON = "Houston"
    MIAMI = "Miami"
    TAMPA = "Tampa"
    WASHINGTON_DC = "Washington DC"
    SOUTH_DEFAULT = "South default"


class south_county(Variable):
    value_type = Enum
    entity = Household
    possible_values = SouthCounty
    default_value = SouthCounty.SOUTH_DEFAULT
    definition_period = YEAR
    defined_for = "is_south_region"
    label = "South region state group"

    def formula(household, period, parameters):
        county = household("county_str", period)

        p = parameters(
            period
        ).gov.bankruptcy.local_standards.vehicle_operation.region_group

        return select(
            [
                np.isin(county, p.south.atlanta),
                np.isin(county, p.northeast.baltimore),
                np.isin(county, p.northeast.dallas_ft_worth),
                np.isin(county, p.northeast.houston),
                np.isin(county, p.northeast.miami),
                np.isin(county, p.northeast.tampa),
                np.isin(county, p.northeast.washington_dc),
            ],
            [
                SouthCounty.ATLANTA,
                SouthCounty.BALTIMORE,
                SouthCounty.DALLAS_FT_WORTH,
                SouthCounty.HOUSTON,
                SouthCounty.MIAMI,
                SouthCounty.TAMPA,
                SouthCounty.WASHINGTON_DC,
            ],
            default=SouthCounty.SOUTH_DEFAULT,
        )