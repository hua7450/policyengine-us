from policyengine_us.model_api import *


class HIOSSLivingArrangement(Enum):
    COMMUNITY_CARE = "Community care foster family home"
    DOMICILIARY_CARE_I = "Domiciliary care facility with 5 or fewer residents"
    DOMICILIARY_CARE_II = "Domiciliary care facility with 6 or more residents"
    MEDICAID_INSTITUTION = "Medicaid institution paying more than 50% of care cost"
    NONE = "Not in a qualifying facility"


class hi_oss_living_arrangement(Variable):
    value_type = Enum
    entity = Person
    label = "Hawaii OSS living arrangement"
    definition_period = YEAR
    defined_for = StateCode.HI
    possible_values = HIOSSLivingArrangement
    default_value = HIOSSLivingArrangement.NONE
    reference = (
        "https://secure.ssa.gov/poms.nsf/lnx/0501415210SF",
        "https://secure.ssa.gov/POMS.NSF/lnx/0501415057",
    )
