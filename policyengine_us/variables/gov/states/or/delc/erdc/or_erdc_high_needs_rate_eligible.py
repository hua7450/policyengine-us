from policyengine_us.model_api import *


class or_erdc_high_needs_rate_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eligible for the Oregon ERDC high need rate"
    defined_for = StateCode.OR
    reference = (
        "https://secure.sos.state.or.us/oard/view.action?ruleNumber=414-175-0076"
    )
