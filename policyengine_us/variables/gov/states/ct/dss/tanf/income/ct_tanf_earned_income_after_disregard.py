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

        # Different disregards for applicants vs recipients
        spm_unit = person.spm_unit
        is_recipient = spm_unit("is_tanf_enrolled", period)

        # For applicants: $90 flat disregard
        applicant_disregard = p.income.disregards.initial_disregard

        # For recipients: 230% FPL per person disregard
        # Get person's share of FPL based on SPM unit size
        fpg_monthly = spm_unit("tanf_fpg", period)
        unit_size = spm_unit("spm_unit_size", period)
        fpg_per_person = fpg_monthly / unit_size
        recipient_disregard = fpg_per_person * p.income_limit.rate

        # Use recipient disregard if enrolled, otherwise use applicant disregard
        disregard = where(
            is_recipient, recipient_disregard, applicant_disregard
        )

        return max_(gross_earned - disregard, 0)
