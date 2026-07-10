from policyengine_us.model_api import *


class or_erdc_special_circumstances_child(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Oregon ERDC child with verified special circumstances"
    defined_for = StateCode.OR
    reference = "https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=7871"
