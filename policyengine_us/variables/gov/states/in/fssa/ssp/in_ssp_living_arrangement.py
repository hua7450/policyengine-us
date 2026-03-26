from policyengine_us.model_api import *


class INSSPLivingArrangement(Enum):
    MEDICAID_FACILITY = "Medicaid-certified health care facility"
    LICENSED_RESIDENTIAL = "Licensed residential care facility"
    UNLICENSED_RESIDENTIAL = "Unlicensed residential care facility"
    NONE = "None"


class in_ssp_living_arrangement(Variable):
    value_type = Enum
    entity = Household
    label = "Indiana SSP living arrangement"
    definition_period = MONTH
    defined_for = StateCode.IN
    possible_values = INSSPLivingArrangement
    default_value = INSSPLivingArrangement.NONE
    reference = (
        "https://secure.ssa.gov/poms.nsf/lnx/0501401001CHI",
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/in.html",
    )
