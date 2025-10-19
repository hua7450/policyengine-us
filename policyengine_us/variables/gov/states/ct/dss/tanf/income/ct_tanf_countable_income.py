from policyengine_us.model_api import *


class ct_tanf_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA countable income"
    documentation = "Total countable income (earned plus unearned) for Connecticut TFA eligibility and benefit calculation."
    unit = USD
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    adds = ["ct_tanf_countable_earned_income", "ct_tanf_countable_unearned_income"]
