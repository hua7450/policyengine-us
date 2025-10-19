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

    def formula(spm_unit, period, parameters):
        countable_earned = spm_unit("ct_tanf_countable_earned_income", period)
        countable_unearned = spm_unit(
            "ct_tanf_countable_unearned_income", period
        )
        return countable_earned + countable_unearned
