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
        is_enrolled = spm_unit("is_tanf_enrolled", period)
        fpg = spm_unit("tanf_fpg", period)

        # Applicants: countable income <= 55% FPL (Standard of Need)
        # Countable income includes $90 earned income disregard per person
        countable_income = spm_unit("ct_tanf_countable_income", period)
        standard_of_need = fpg * p.income.standard_of_need.rate
        applicant_eligible = countable_income <= standard_of_need

        # Recipients: gross earnings <= income limit
        # Pre-2024: 100% FPL, Post-2024: 230% FPL for 6 months (not modeled)
        gross_earnings = add(spm_unit, period, ["tanf_gross_earned_income"])
        income_limit = fpg * p.income_limit.rate
        recipient_eligible = gross_earnings <= income_limit

        return where(is_enrolled, recipient_eligible, applicant_eligible)
