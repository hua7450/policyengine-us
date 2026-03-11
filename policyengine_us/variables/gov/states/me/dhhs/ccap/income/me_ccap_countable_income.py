from policyengine_us.model_api import *


class me_ccap_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Maine CCAP countable income"
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.ME
    reference = "https://www.maine.gov/sos/cec/rules/10/ch6.pdf#page=7"

    adds = "gov.states.me.dhhs.ccap.income.countable_income.sources"
