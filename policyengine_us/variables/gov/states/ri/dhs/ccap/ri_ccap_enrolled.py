from policyengine_us.model_api import *


class ri_ccap_enrolled(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Whether the family is currently enrolled in Rhode Island Child Care Assistance Program (CCAP)"
    defined_for = StateCode.RI
