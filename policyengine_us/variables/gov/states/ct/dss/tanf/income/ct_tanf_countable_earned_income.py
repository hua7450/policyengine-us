from policyengine_us.model_api import *


class ct_tanf_countable_earned_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA countable earned income"
    unit = USD
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf

        # Total household earned income
        total_earned = add(spm_unit, period, ["tanf_gross_earned_income"])

        # Check if household is enrolled in TANF
        is_enrolled = spm_unit("is_tanf_enrolled", period)

        # For applicants: $90 disregard total (not per person)
        applicant_disregard = p.income.disregards.initial_disregard
        applicant_income = max_(total_earned - applicant_disregard, 0)

        # For recipients: Disregard earned income up to 230% FPL
        # Policy changed Jan 1, 2024: families can earn up to 230% FPL
        # and have all earned income disregarded (for 6 months, not modeled)
        fpg = spm_unit("tanf_fpg", period)
        recipient_disregard = fpg * p.income_limit.rate
        recipient_income = max_(total_earned - recipient_disregard, 0)

        # Return appropriate value based on enrollment status
        return where(is_enrolled, recipient_income, applicant_income)
