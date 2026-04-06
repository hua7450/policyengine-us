from policyengine_us.model_api import *


class sc_ccap_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for South Carolina CCAP"
    definition_period = MONTH
    defined_for = StateCode.SC
    reference = (
        "https://www.scchildcare.org/media/ubhdm1at/1-13-2025_policy-manual.pdf#page=14"
    )

    def formula(spm_unit, period, parameters):
        has_eligible_child = add(spm_unit, period, ["sc_ccap_eligible_child"]) > 0
        income_eligible = spm_unit("sc_ccap_income_eligible", period)
        asset_eligible = spm_unit("is_ccdf_asset_eligible", period.this_year)
        activity_eligible = spm_unit("sc_ccap_activity_eligible", period)
        return has_eligible_child & income_eligible & asset_eligible & activity_eligible
