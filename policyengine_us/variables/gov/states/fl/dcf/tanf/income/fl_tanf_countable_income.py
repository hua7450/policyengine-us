from policyengine_us.model_api import *


class fl_tanf_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Florida TANF countable income"
    unit = USD
    definition_period = MONTH
    reference = "Florida Administrative Code Rule 65A-4.209"
    documentation = (
        "Total countable income for Florida TANF benefit calculation."
    )
    defined_for = StateCode.FL

    adds = [
        "fl_tanf_countable_earned_income",
        "fl_tanf_countable_unearned_income",
    ]
