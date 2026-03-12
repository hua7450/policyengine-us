from policyengine_us.model_api import *


class vt_ccfap_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = YEAR
    defined_for = StateCode.VT
    label = "Eligible for Vermont CCFAP"
    reference = (
        "https://outside.vermont.gov/dept/DCF/Shared%20Documents/CDD/CCFAP/CCFAP-Regulations.pdf",
        "https://legislature.vermont.gov/statutes/section/33/035/03512",
    )

    def formula(spm_unit, period, parameters):
        has_eligible_child = add(spm_unit, period, ["vt_ccfap_eligible_child"]) > 0
        asset_eligible = spm_unit("is_ccdf_asset_eligible", period)
        income_eligible = spm_unit("vt_ccfap_income_eligible", period)

        reach_up = spm_unit("is_tanf_enrolled", period.first_month)
        protective = (
            add(
                spm_unit,
                period,
                ["receives_or_needs_protective_services"],
            )
            > 0
        )
        foster = add(spm_unit, period.first_month, ["is_in_foster_care"]) > 0
        categorically_eligible = reach_up | protective | foster

        return (
            has_eligible_child
            & asset_eligible
            & (income_eligible | categorically_eligible)
        )
