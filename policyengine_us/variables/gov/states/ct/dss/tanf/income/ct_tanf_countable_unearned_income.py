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

        # Use CT-specific gross unearned income (excludes child support)
        # Sum person-level income to SPM unit level
        person_gross_unearned = spm_unit.members(
            "ct_tanf_gross_unearned_income", period
        )
        gross_unearned_income = spm_unit.sum(person_gross_unearned)

        # Child support passthrough: deduct up to $50/month if child support is received
        # This is a deduction from countable income, not counting child support as income
        person_child_support = spm_unit.members(
            "child_support_received", period
        )
        child_support = spm_unit.sum(person_child_support)
        child_support_deduction = min_(
            child_support, p.deductions.child_support_passthrough
        )

        return max_(0, gross_unearned_income - child_support_deduction)
