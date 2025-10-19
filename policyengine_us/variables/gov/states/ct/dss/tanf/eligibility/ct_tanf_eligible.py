from policyengine_us.model_api import *


class ct_tanf_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA eligibility"
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        # Use federal demographic eligibility directly
        # Connecticut uses age 18 (age 19 for students) which matches federal TANF
        demographic_eligible = spm_unit("is_demographic_tanf_eligible", period)

        # Use federal immigration eligibility directly
        # Connecticut follows federal rules for immigration eligibility
        immigration_eligible = spm_unit.any(
            spm_unit.members("is_citizen_or_legal_immigrant", period)
        )

        # State-specific income and resource tests
        income_eligible = spm_unit("ct_tanf_income_eligible", period)
        resources_eligible = spm_unit("ct_tanf_resources_eligible", period)

        return (
            demographic_eligible
            & immigration_eligible
            & income_eligible
            & resources_eligible
        )
