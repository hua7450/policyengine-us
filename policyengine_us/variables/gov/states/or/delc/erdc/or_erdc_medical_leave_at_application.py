from policyengine_us.model_api import *


class or_erdc_medical_leave_at_application(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = YEAR
    label = "Oregon ERDC caretaker on medical leave at initial application"
    defined_for = StateCode.OR
    reference = (
        "https://secure.sos.state.or.us/oard/view.action?ruleNumber=414-175-0023"
    )
