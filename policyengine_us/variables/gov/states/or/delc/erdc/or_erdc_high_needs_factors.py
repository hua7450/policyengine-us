from policyengine_us.model_api import *


class or_erdc_high_needs_factors(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    default_value = 0
    label = "Oregon ERDC high needs assessed factor count"
    # OAR 414-175-0076(2)-(4): the assessed high needs factor ranges from 0 to
    # 2 and multiplies the hourly or monthly supplement.
    defined_for = StateCode.OR
    reference = (
        "https://secure.sos.state.or.us/oard/view.action?ruleNumber=414-175-0076"
    )
