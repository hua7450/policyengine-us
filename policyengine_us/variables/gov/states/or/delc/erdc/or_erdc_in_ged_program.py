from policyengine_us.model_api import *


class or_erdc_in_ged_program(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Oregon ERDC caretaker participating in a GED program"
    defined_for = StateCode.OR
    reference = (
        "https://secure.sos.state.or.us/oard/view.action?ruleNumber=414-175-0023"
    )
