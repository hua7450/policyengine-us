from policyengine_us.model_api import *


class or_erdc_expanded_child_welfare_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = YEAR
    label = "Eligible for Oregon ERDC through Expanded Child Welfare"
    defined_for = StateCode.OR
    reference = "https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=7871"
