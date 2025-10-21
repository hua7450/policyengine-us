from policyengine_us.model_api import *


class ct_tanf_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Connecticut Temporary Family Assistance (TANF)"
    definition_period = MONTH
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        # Demographic eligibility: at least one eligible child or pregnant person
        demographic_eligible = spm_unit.any(
            spm_unit.members("is_demographic_tanf_eligible", period)
        )

        # Immigration eligibility: at least one citizen or legal immigrant
        immigration_eligible = spm_unit.any(
            spm_unit.members("is_citizen_or_legal_immigrant", period)
        )

        # Income eligibility
        income_eligible = spm_unit("ct_tanf_income_eligible", period)

        # Resources eligibility
        resources_eligible = spm_unit("ct_tanf_resources_eligible", period)

        return (
            demographic_eligible
            & immigration_eligible
            & income_eligible
            & resources_eligible
        )
