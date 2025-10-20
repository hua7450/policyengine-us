from policyengine_us.model_api import *


class ct_tanf(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut Temporary Family Assistance (TFA/TANF)"
    unit = USD
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = "ct_tanf_eligible"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf

        # Standard benefit calculation: payment standard - countable income
        payment_standard = spm_unit("ct_tanf_payment_standard", period)
        countable_income = spm_unit("ct_tanf_countable_income", period)

        standard_benefit = max_(payment_standard - countable_income, 0)

        # Check if total gross earnings are in extended eligibility reduction tier (171-230% FPL)
        # This only applies to recipients with earnings between those thresholds
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

        # Apply 20% reduction if in tier (effective January 1, 2024)
        reduction_rate = p.extended_eligibility.benefit_reduction
        reduced_benefit = standard_benefit * (1 - reduction_rate)

        return where(in_reduction_tier, reduced_benefit, standard_benefit)
