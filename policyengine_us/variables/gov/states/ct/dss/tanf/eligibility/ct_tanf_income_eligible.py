from policyengine_us.model_api import *


class ct_tanf_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA income eligibility"
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf

        # For applicants: Check gross income after $90 per earner disregard against 55% FPL
        is_enrolled = spm_unit("is_tanf_enrolled", period)
        fpg = spm_unit("tanf_fpg", period)

        # Applicant test: Gross earned income - ($90 * number of earners) + unearned < 55% FPL
        gross_earned = add(spm_unit, period, ["tanf_gross_earned_income"])

        # Count earners (people with positive earnings)
        has_earnings = spm_unit.members("tanf_gross_earned_income", period) > 0
        num_earners = spm_unit.sum(has_earnings)

        applicant_disregard = (
            p.income.disregards.applicant_disregard * num_earners
        )
        earned_after_disregard = max_(gross_earned - applicant_disregard, 0)

        gross_unearned = add(spm_unit, period, ["tanf_gross_unearned_income"])

        # For child support passthrough
        child_support = add(spm_unit, period, ["child_support_received"])
        passthrough = min_(
            child_support, p.income.deductions.child_support_passthrough
        )
        unearned_after_passthrough = max_(gross_unearned - passthrough, 0)

        total_countable_applicant = (
            earned_after_disregard + unearned_after_passthrough
        )

        initial_limit = fpg * p.income.standards.initial_eligibility
        applicant_eligible = total_countable_applicant < initial_limit

        # Recipient test: Check if gross earnings exceed extended eligibility limit
        # Recipients get 100% disregard up to 100% FPL, then extended eligibility up to 230% FPL
        extended_upper_limit = (
            fpg * p.income.standards.extended_eligibility_upper
        )
        recipient_eligible = gross_earned <= extended_upper_limit

        return where(is_enrolled, recipient_eligible, applicant_eligible)
