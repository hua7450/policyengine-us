from policyengine_us.model_api import *


class FLOSSLivingArrangement(Enum):
    ALF = "Assisted Living Facility"
    AFCH = "Adult Family Care Home"
    MHRTF = "Mental Health Residential Treatment Facility"
    MEDICAID_FACILITY = "Medicaid facility"
    NONE = "None"


class fl_oss_living_arrangement(Variable):
    value_type = Enum
    entity = Person
    label = "Florida OSS living arrangement"
    definition_period = MONTH
    defined_for = StateCode.FL
    possible_values = FLOSSLivingArrangement
    default_value = FLOSSLivingArrangement.NONE
    reference = (
        "https://www.flrules.org/gateway/RuleNo.asp?title=PUBLIC%20ASSISTANCE&ID=65A-2.032",
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/fl.html",
    )

    def formula(person, period):
        federal_la = person("ssi_federal_living_arrangement", period)
        in_medical_facility = (
            federal_la == federal_la.possible_values.MEDICAL_TREATMENT_FACILITY
        )
        community_care = person("fl_oss_community_care_type", period)
        CC = community_care.possible_values
        LA = FLOSSLivingArrangement
        return select(
            [
                in_medical_facility,
                community_care == CC.ALF,
                community_care == CC.AFCH,
                community_care == CC.MHRTF,
            ],
            [
                LA.MEDICAID_FACILITY,
                LA.ALF,
                LA.AFCH,
                LA.MHRTF,
            ],
            default=LA.NONE,
        )
