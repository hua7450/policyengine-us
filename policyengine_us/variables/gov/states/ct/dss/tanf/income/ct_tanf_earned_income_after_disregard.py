from policyengine_us.model_api import *


class ct_tanf_earned_income_after_disregard(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Connecticut TFA earned income after disregard"
    unit = USD
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = StateCode.CT

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf
        # Use federal TANF gross earned income baseline
        gross_earned = person("tanf_gross_earned_income", period)

        # Check if household is enrolled in TANF
        is_enrolled = person.spm_unit("is_tanf_enrolled", period)

        # For applicants: $90 disregard per person
        applicant_income = max_(
            gross_earned - p.income.disregards.initial_disregard, 0
        )

        # For recipients: Disregard earned income up to % of FPL
        # Policy changed Jan 1, 2024: 100% FPL → 230% FPL
        # Parameter handles time-based transition automatically
        spm_unit = person.spm_unit
        fpg = spm_unit("tanf_fpg", period)
        # Attribute FPL disregard equally to each person in unit
        unit_size = spm_unit("spm_unit_size", period)
        # Use continuing_eligibility parameter (100% pre-2024, 230% post-2024)
        recipient_disregard_per_person = (
            fpg * p.income.standards.continuing_eligibility / unit_size
        )

        recipient_income = max_(
            gross_earned - recipient_disregard_per_person, 0
        )

        # Return appropriate value based on enrollment status
        return where(is_enrolled, recipient_income, applicant_income)
