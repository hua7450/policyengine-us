from policyengine_us.model_api import *


class or_erdc_permanent_job_loss(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = YEAR
    label = "Oregon ERDC caretaker with a permanent job loss from all employment"
    defined_for = StateCode.OR
    reference = (
        "https://secure.sos.state.or.us/oard/view.action?ruleNumber=414-175-0023"
    )
