from policyengine_us.model_api import *


class is_ri_ccap_enrolled(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    default_value = False
    label = "Whether the family is currently enrolled in the Rhode Island Child Care Assistance Program"
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3"
