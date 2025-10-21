from policyengine_us.model_api import *


class fl_tanf_countable_earned_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Florida TANF countable earned income"
    unit = USD
    definition_period = MONTH
    reference = "Florida Statute § 414.095"
    documentation = "Earned income after applying two-step disregard process."
    defined_for = StateCode.FL

    def formula(spm_unit, period, parameters):
        gross_earned = spm_unit("fl_tanf_gross_earned_income", period)
        disregard = spm_unit("fl_tanf_earned_income_disregard", period)

        return max_(gross_earned - disregard, 0)
