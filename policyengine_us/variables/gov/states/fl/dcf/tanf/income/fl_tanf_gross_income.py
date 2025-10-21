from policyengine_us.model_api import *


class fl_tanf_gross_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Florida TANF gross income (annual)"
    unit = USD
    definition_period = YEAR
    reference = "Florida Statute § 414.095"
    documentation = "Total gross income for Florida TANF 185% FPL test."
    defined_for = StateCode.FL

    def formula(spm_unit, period, parameters):
        earned = spm_unit("fl_tanf_gross_earned_income", period, options=[ADD])
        unearned = spm_unit(
            "fl_tanf_gross_unearned_income", period, options=[ADD]
        )

        return earned + unearned
