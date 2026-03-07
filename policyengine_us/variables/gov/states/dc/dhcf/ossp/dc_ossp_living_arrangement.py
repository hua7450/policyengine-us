from policyengine_us.model_api import *


class DCOSSPLivingArrangement(Enum):
    OS_A = "Adult foster care facility with 50 or fewer beds"
    OS_B = "Adult foster care facility with more than 50 beds"
    OS_G = "Nursing facility"
    NONE = "Not in a qualifying facility"


class dc_ossp_living_arrangement(Variable):
    value_type = Enum
    entity = Person
    label = "DC OSSP living arrangement"
    definition_period = YEAR
    defined_for = StateCode.DC
    possible_values = DCOSSPLivingArrangement
    default_value = DCOSSPLivingArrangement.NONE
    reference = (
        "https://code.dccouncil.gov/us/dc/council/code/sections/4-205.49",
        "https://secure.ssa.gov/poms.nsf/lnx/0501415009",
    )
