from policyengine_us.model_api import *


class ri_ccap_countable_income(Variable):
    value_type = float
    unit = USD
    entity = SPMUnit
    label = (
        "Rhode Island Child Care Assistance Program (CCAP) countable income"
    )
    definition_period = MONTH
    reference = "https://dhs.ri.gov/media/9236/download?language=en#page=10"
    defined_for = StateCode.RI

    adds = "gov.states.ri.dhs.ccap.income.countable_income.sources"
