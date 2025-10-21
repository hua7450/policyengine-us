from policyengine_us.model_api import *


class ct_tanf_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Connecticut TANF income eligibility"
    definition_period = MONTH
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf.income.standards

        countable_income = spm_unit("ct_tanf_countable_income", period)
        fpg = spm_unit("tanf_fpg", period)

        # Check if enrolled - different thresholds for applicants vs recipients
        is_enrolled = spm_unit("is_tanf_enrolled", period)

        # Applicants: must be below 55% FPL
        applicant_limit = p.initial_eligibility * fpg
        applicant_eligible = countable_income < applicant_limit

        # Recipients: can be up to 100% FPL (standard continuing eligibility)
        recipient_limit = p.continuing_eligibility * fpg
        recipient_eligible = countable_income < recipient_limit

        # Extended eligibility: total gross earnings up to 230% FPL
        total_gross_earnings = add(
            spm_unit, period, ["tanf_gross_earned_income"]
        )
        extended_limit = p.extended_eligibility_upper * fpg
        extended_eligible = total_gross_earnings <= extended_limit

        return where(
            is_enrolled,
            recipient_eligible | extended_eligible,
            applicant_eligible,
        )
