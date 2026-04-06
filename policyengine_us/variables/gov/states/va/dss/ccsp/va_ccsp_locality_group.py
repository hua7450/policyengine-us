from policyengine_us.model_api import *


class VACCSPLocalityGroup(Enum):
    GROUP_I = "Group I"
    GROUP_II = "Group II"
    GROUP_III = "Group III"


class va_ccsp_locality_group(Variable):
    value_type = Enum
    possible_values = VACCSPLocalityGroup
    default_value = VACCSPLocalityGroup.GROUP_III
    entity = SPMUnit
    label = "Virginia CCSP locality group"
    definition_period = YEAR
    defined_for = StateCode.VA
    reference = (
        "https://law.lis.virginia.gov/admincode/title8/agency20/chapter790/section40/",
        "https://doe.virginia.gov/home/showpublisheddocument/56270#page=197",
    )
