from policyengine_us.model_api import *


class ri_ccap_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Rhode Island Child Care Assistance Program (CCAP)"
    definition_period = MONTH
    reference = (
        "https://dhs.ri.gov/media/9236/download?language=en#page=15",
        "https://dhs.ri.gov/media/9236/download?language=en#page=25",
    )
    defined_for = StateCode.RI

    def formula(spm_unit, period, parameters):
        has_eligible_child = (
            add(spm_unit, period, ["ri_ccap_eligible_child"]) > 0
        )
        income_eligible = spm_unit("ri_ccap_income_eligible", period)
        asset_eligible = spm_unit("ri_ccap_asset_eligible", period)
        activity_eligible = spm_unit("ri_ccap_activity_eligible", period)
        ri_works = spm_unit("ri_works_eligible", period)
        # RI Works recipients bypass income and activity tests.
        income_and_activity = ri_works | (income_eligible & activity_eligible)
        return has_eligible_child & asset_eligible & income_and_activity
