from policyengine_us.model_api import *


class vt_ccfap_family_share(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VT
    label = "Vermont CCFAP annual family share (copayment)"
    reference = (
        "https://outside.vermont.gov/dept/DCF/Shared%20Documents/CDD/CCFAP/Income-Guidelines.pdf",
        "https://outside.vermont.gov/dept/DCF/Shared%20Documents/CDD/CCFAP/CCFAP-Regulations.pdf",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.vt.dcf.ccfap
        income = spm_unit("vt_ccfap_countable_income", period)
        fpg = spm_unit("spm_unit_fpg", period)
        fpl_ratio = income / fpg

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
        exempt = reach_up | protective | foster

        weekly_share = p.family_share.scale.calc(fpl_ratio)
        annual_share = weekly_share * WEEKS_IN_YEAR
        return where(exempt, 0, annual_share)
