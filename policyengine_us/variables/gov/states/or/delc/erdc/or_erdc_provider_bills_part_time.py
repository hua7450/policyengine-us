from policyengine_us.model_api import *


class or_erdc_provider_bills_part_time(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = "Oregon ERDC provider customarily bills part-time monthly"
    defined_for = StateCode.OR
    reference = (
        "https://secure.sos.state.or.us/oard/view.action?ruleNumber=414-175-0075"
    )
