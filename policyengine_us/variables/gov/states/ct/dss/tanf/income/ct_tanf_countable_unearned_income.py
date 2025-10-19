from policyengine_us.model_api import *


class ct_tanf_countable_unearned_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA countable unearned income"
    unit = USD
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf.income
        # Use federal TANF gross unearned income baseline
        total_unearned_income = add(
            spm_unit, period, ["tanf_gross_unearned_income"]
        )
        # Apply child support passthrough (up to $50/month excluded)
        child_support = add(spm_unit, period, ["child_support_received"])
        child_support_deduction = min_(
            child_support, p.deductions.child_support_passthrough
        )

        return max_(0, total_unearned_income - child_support_deduction)
