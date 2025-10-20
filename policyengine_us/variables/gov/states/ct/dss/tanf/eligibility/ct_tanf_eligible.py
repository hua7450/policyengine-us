from policyengine_us.model_api import *


class ct_tanf_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA eligibility"
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        # Use federal demographic eligibility
        demographic_eligible = spm_unit("is_demographic_tanf_eligible", period)

        # Use federal immigration eligibility - at least one member must be eligible
        immigration_eligible = spm_unit.any(
            spm_unit.members("is_citizen_or_legal_immigrant", period)
        )

        # State-specific tests
        income_eligible = spm_unit("ct_tanf_income_eligible", period)
        resources_eligible = spm_unit("ct_tanf_resources_eligible", period)

        return (
            demographic_eligible
            & immigration_eligible
            & income_eligible
            & resources_eligible
        )
