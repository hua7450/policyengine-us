from policyengine_us.model_api import *


class ct_tanf_non_financial_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA non-financial eligibility"
    documentation = "Whether the household meets non-financial requirements for Connecticut Temporary Family Assistance: at least one demographically eligible person and all members meet immigration requirements."
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        # Use federal demographic eligibility directly
        # Connecticut uses age 18 (age 19 for students) which matches federal TANF definition
        demographic_eligible = spm_unit("is_demographic_tanf_eligible", period)

        # Use federal immigration eligibility directly
        # Connecticut follows federal rules for immigration eligibility
        immigration_eligible = spm_unit.any(
            spm_unit.members("is_citizen_or_legal_immigrant", period)
        )

        return demographic_eligible & immigration_eligible
