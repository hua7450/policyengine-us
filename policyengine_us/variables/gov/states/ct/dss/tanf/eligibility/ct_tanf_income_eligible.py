from policyengine_us.model_api import *


class ct_tanf_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA income eligibility"
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf

        # Get countable income (earned with disregards + unearned)
        # Note: Earned income has up to 230% FPL disregard for recipients
        # Unearned income counted dollar-for-dollar (minus $50 child support)
        countable_income = spm_unit("ct_tanf_countable_income", period)

        # Use tanf_fpg variable instead of recalculating
        fpg = spm_unit("tanf_fpg", period)

        # Income eligibility: countable income <= 55% FPL (Standard of Need)
        # This applies to both applicants and recipients
        # The difference is in how countable income is calculated:
        # - Applicants: $90 earned income disregard
        # - Recipients: Up to 230% FPL earned income disregard
        standard_of_need = fpg * p.income.standard_of_need.rate
        meets_standard_of_need = countable_income <= standard_of_need

        # Additional check: gross earned income cannot exceed 230% FPL
        # This is the maximum income limit for the extended eligibility policy
        total_gross_earnings = add(
            spm_unit, period, ["tanf_gross_earned_income"]
        )
        income_limit = fpg * p.income_limit.rate
        below_income_limit = total_gross_earnings <= income_limit

        return meets_standard_of_need & below_income_limit
