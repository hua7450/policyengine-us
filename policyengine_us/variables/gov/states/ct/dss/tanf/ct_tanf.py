from policyengine_us.model_api import *


class ct_tanf(Variable):
    value_type = float
    entity = SPMUnit
    label = "Connecticut Temporary Family Assistance (TANF)"
    unit = USD
    definition_period = MONTH
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = "ct_tanf_eligible"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf

        payment_standard = spm_unit("ct_tanf_payment_standard", period)
        countable_income = spm_unit("ct_tanf_countable_income", period)

        # Standard benefit calculation
        standard_benefit = max_(payment_standard - countable_income, 0)

        # Check if in extended eligibility reduction tier (171-230% FPL)
        # This applies when total gross earnings are in this range
        total_gross_earnings = add(
            spm_unit, period, ["tanf_gross_earned_income"]
        )
        fpg = spm_unit("tanf_fpg", period)

        reduction_threshold = (
            p.income.standards.extended_eligibility_reduction_threshold * fpg
        )
        upper_threshold = p.income.standards.extended_eligibility_upper * fpg

        in_reduction_tier = (total_gross_earnings >= reduction_threshold) & (
            total_gross_earnings <= upper_threshold
        )

        # Apply 20% reduction if in tier
        reduction_rate = p.extended_eligibility.benefit_reduction
        reduced_benefit = standard_benefit * (1 - reduction_rate)

        return where(in_reduction_tier, reduced_benefit, standard_benefit)
