from policyengine_us.model_api import *


class FLOSSFacilityType(Enum):
    ALF = "Assisted Living Facility"
    AFCH = "Adult Family Care Home"
    MHRTF = "Mental Health Residential Treatment Facility"
    NONE = "None"


class fl_oss_facility_type(Variable):
    value_type = Enum
    entity = Household
    label = "Florida OSS facility type"
    definition_period = MONTH
    defined_for = StateCode.FL
    possible_values = FLOSSFacilityType
    default_value = FLOSSFacilityType.NONE
    reference = (
        "https://www.flrules.org/gateway/RuleNo.asp?title=PUBLIC%20ASSISTANCE&ID=65A-2.032",
        "https://www.myflfamilies.com/sites/default/files/2024-10/Appendix%20A-12%20OSS%20Payment%20Standards.pdf",
    )
