from policyengine_us.model_api import *


class ct_tanf_countable_unearned_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA countable unearned income"
    unit = USD
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf

        # Use federal gross unearned income baseline
        total_unearned = add(spm_unit, period, ["tanf_gross_unearned_income"])

        # Apply CT's $50 child support passthrough deduction
        child_support = add(spm_unit, period, ["child_support_received"])
        passthrough = min_(
            child_support, p.income.deductions.child_support_passthrough
        )

        return max_(total_unearned - passthrough, 0)
