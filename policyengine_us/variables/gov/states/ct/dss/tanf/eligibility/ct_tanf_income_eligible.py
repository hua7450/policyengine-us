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

        # Get countable income (already has appropriate disregards applied)
        countable_income = spm_unit("ct_tanf_countable_income", period)

        # Use tanf_fpg variable instead of recalculating
        fpg = spm_unit("tanf_fpg", period)

        # Check enrollment status to apply different eligibility tests
        is_enrolled = spm_unit("is_tanf_enrolled", period)

        # For applicants: countable income < 55% FPL (Standard of Need)
        initial_limit = fpg * p.income.standards.initial_eligibility
        applicant_eligible = countable_income <= initial_limit

        # For recipients: total gross earnings < 230% FPL (extended eligibility)
        # Recipients can have earnings up to 230% FPL for up to 6 months
        total_gross_earnings = add(
            spm_unit, period, ["tanf_gross_earned_income"]
        )
        extended_limit = fpg * p.income.standards.extended_eligibility_upper
        recipient_eligible = total_gross_earnings <= extended_limit

        return where(is_enrolled, recipient_eligible, applicant_eligible)
