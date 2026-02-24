from policyengine_us.model_api import *


class CTTFARegion(Enum):
    REGION_A = "Region A"
    REGION_B = "Region B"
    REGION_C = "Region C"


class ct_tfa_region(Variable):
    value_type = Enum
    entity = Household
    possible_values = CTTFARegion
    default_value = CTTFARegion.REGION_B
    definition_period = MONTH
    defined_for = StateCode.CT
    label = "Connecticut TFA payment region"
    reference = "https://secure.ssa.gov/poms.nsf/lnx/0500830403BOS"
