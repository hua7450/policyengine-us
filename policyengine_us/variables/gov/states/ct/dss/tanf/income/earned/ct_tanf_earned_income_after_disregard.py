from policyengine_us.model_api import *


class ct_tanf_earned_income_after_disregard(Variable):
    value_type = float
    entity = SPMUnit
    label = "Connecticut TANF earned income after disregard"
    unit = USD
    definition_period = MONTH
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf.income.deductions

        # Get total gross earned income for the unit
        total_gross_earnings = add(
            spm_unit, period, ["tanf_gross_earned_income"]
        )

        # Check if enrolled - different disregards for applicants vs recipients
        is_enrolled = spm_unit("is_tanf_enrolled", period)

        # Applicants: $90 per person in the unit
        unit_size = spm_unit("spm_unit_size", period)
        applicant_disregard = (
            unit_size * p.applicant_earned_income_disregard
        )
        applicant_countable = max_(
            total_gross_earnings - applicant_disregard, 0
        )

        # Recipients: 100% FPL disregard (household total)
        fpg = spm_unit("tanf_fpg", period)
        recipient_disregard = fpg
        recipient_countable = max_(
            total_gross_earnings - recipient_disregard, 0
        )

        return where(is_enrolled, recipient_countable, applicant_countable)
