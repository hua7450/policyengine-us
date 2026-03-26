from policyengine_us.model_api import *


class md_ccs_receives_snap(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Whether the family receives SNAP (used for Maryland CCS copay waiver)"
    defined_for = StateCode.MD
