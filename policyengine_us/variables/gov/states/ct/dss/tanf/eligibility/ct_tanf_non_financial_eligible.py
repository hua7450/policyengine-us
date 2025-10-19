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
        # At least one person must be demographically eligible (child or pregnant)
        has_eligible_person = spm_unit.any(
            spm_unit.members("ct_tanf_demographic_eligible_person", period)
        )

        # All members must meet immigration requirements (mixed status allowed with future deeming/proration)
        immigration_eligible = spm_unit.any(
            spm_unit.members(
                "ct_tanf_immigration_status_eligible_person", period
            )
        )

        return has_eligible_person & immigration_eligible
