from policyengine_us.model_api import *


class ri_ccap_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Rhode Island Child Care Assistance Program (CCAP)"
    definition_period = MONTH
    defined_for = StateCode.RI
    reference = (
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3",
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.6",
    )

    def formula(spm_unit, period, parameters):
        has_eligible_child = (
            add(spm_unit, period, ["ri_ccap_child_eligible"]) > 0
        )
        # RI Works (TANF) pathway bypasses income test
        is_tanf_enrolled = spm_unit("is_tanf_enrolled", period)
        income_eligible = spm_unit("ri_ccap_income_eligible", period)
        asset_eligible = spm_unit("ri_ccap_asset_eligible", period)
        return has_eligible_child & (
            is_tanf_enrolled | (income_eligible & asset_eligible)
        )
