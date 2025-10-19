from policyengine_us.model_api import *


class ct_tanf_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA eligibility"
    documentation = "Whether the household is eligible for Connecticut Temporary Family Assistance (TFA/TANF). Requires meeting demographic, income, and resource requirements."
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        non_financial_eligible = spm_unit(
            "ct_tanf_non_financial_eligible", period
        )
        income_eligible = spm_unit("ct_tanf_income_eligible", period)
        resources_eligible = spm_unit("ct_tanf_resources_eligible", period)

        return non_financial_eligible & income_eligible & resources_eligible
