from policyengine_us.model_api import *


class or_erdc_supervised_contact_required(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = YEAR
    label = "Oregon ERDC supervised contact required"
    defined_for = StateCode.OR
    reference = "https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=7871"
