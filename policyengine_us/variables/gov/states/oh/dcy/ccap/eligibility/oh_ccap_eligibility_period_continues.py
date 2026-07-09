from policyengine_us.model_api import *


class oh_ccap_eligibility_period_continues(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether the child's current Ohio CCAP eligibility period continues"
    defined_for = StateCode.OH
    reference = "https://codes.ohio.gov/ohio-administrative-code/rule-5180:6-1-02"
