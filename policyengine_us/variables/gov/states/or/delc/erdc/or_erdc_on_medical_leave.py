from policyengine_us.model_api import *


class or_erdc_on_medical_leave(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Oregon ERDC caretaker on verified medical leave"
    defined_for = StateCode.OR
    reference = "https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=7871"
