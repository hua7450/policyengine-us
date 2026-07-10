from policyengine_us.model_api import *


class or_erdc_unable_to_provide_care(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Oregon ERDC caretaker unable to provide care"
    defined_for = StateCode.OR
    reference = "https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=7871"
