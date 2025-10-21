from policyengine_us.model_api import *


class fl_tanf_countable_unearned_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Florida TANF countable unearned income"
    unit = USD
    definition_period = MONTH
    reference = "Florida Administrative Code Rule 65A-4.209"
    documentation = (
        "Unearned income after applying $50 child support disregard."
    )
    defined_for = StateCode.FL

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.fl.dcf.tanf.income_disregards

        gross_unearned = spm_unit("fl_tanf_gross_unearned_income", period)
        child_support = spm_unit("child_support_received", period)

        # Apply $50 child support disregard
        child_support_disregard = min_(
            child_support, p.child_support_disregard
        )

        return max_(gross_unearned - child_support_disregard, 0)
