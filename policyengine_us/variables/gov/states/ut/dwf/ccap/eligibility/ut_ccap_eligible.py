from policyengine_us.model_api import *


class ut_ccap_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Utah CCAP eligible"
    definition_period = MONTH
    defined_for = StateCode.UT
    reference = (
        "https://utrules.elaws.us/uac/r986-700-702",
        "https://utrules.elaws.us/uac/r986-700-707",
        "https://utrules.elaws.us/uac/r986-700-710",
    )

    def formula(spm_unit, period, parameters):
        has_eligible_child = add(spm_unit, period, ["ut_ccap_eligible_child"]) > 0
        income_eligible = spm_unit("ut_ccap_income_eligible", period)
        # The family asset limit is the federal CCDF $1,000,000 self-certified
        # limit (45 CFR 98.20), not restated in R986-700-710.
        asset_eligible = spm_unit("is_ccdf_asset_eligible", period.this_year)
        activity_eligible = spm_unit("ut_ccap_activity_eligible", period)
        # A family whose co-payment exceeds the actual cost of care is
        # ineligible (R986-700-707).
        copay = spm_unit("ut_ccap_copay", period)
        childcare_expenses = spm_unit("spm_unit_pre_subsidy_childcare_expenses", period)
        copay_affordable = copay <= childcare_expenses
        return (
            has_eligible_child
            & income_eligible
            & asset_eligible
            & activity_eligible
            & copay_affordable
        )
