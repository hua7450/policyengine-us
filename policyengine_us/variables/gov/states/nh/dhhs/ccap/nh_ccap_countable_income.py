from policyengine_us.model_api import *


class nh_ccap_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "New Hampshire Child Care Scholarship Program countable income"
    definition_period = MONTH
    unit = USD
    defined_for = StateCode.NH
    reference = (
        "https://www.gencourt.state.nh.us/rules/filing_history/sourcehe-c6910.html"
    )

    adds = "gov.states.nh.dhhs.ccap.income.countable_income.sources"
