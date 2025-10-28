from policyengine_us.model_api import *


class ct_tanf_earned_income_after_disregard(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA earned income after disregard"
    unit = USD
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf

        # Use federal gross earned income
        gross_earned = add(spm_unit, period, ["tanf_gross_earned_income"])

        # Check enrollment status
        is_enrolled = spm_unit("is_tanf_enrolled", period)

        # For applicants: Apply $90 per earner disregard
        has_earnings = spm_unit.members("tanf_gross_earned_income", period) > 0
        num_earners = spm_unit.sum(has_earnings)
        applicant_disregard = (
            p.income.disregards.applicant_disregard * num_earners
        )
        applicant_income = max_(gross_earned - applicant_disregard, 0)

        # For recipients: 100% disregard up to 100% FPL
        fpg = spm_unit("tanf_fpg", period)
        recipient_disregard_limit = (
            fpg * p.income.standards.continuing_eligibility
        )
        recipient_disregard = min_(gross_earned, recipient_disregard_limit)
        recipient_income = max_(gross_earned - recipient_disregard, 0)

        return where(is_enrolled, recipient_income, applicant_income)
