from policyengine_us.model_api import *


class wa_rca_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Washington Refugee Cash Assistance eligible"
    definition_period = MONTH
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/wac/default.aspx?cite=388-400-0030",
        "https://app.leg.wa.gov/wac/default.aspx?cite=388-466-0120",
    )

    def formula(spm_unit, period, parameters):
        # RCA does not require a dependent child, unlike TANF and SFA.
        # Federal RCA eligibility is limited to the first 12 months after
        # entry or status grant (8 USC 1522; 45 CFR 400.211); we do not
        # track months-since-entry at the moment, so that window is not
        # enforced here.
        has_rca_eligible_immigrant = (
            add(spm_unit, period, ["wa_rca_immigration_status_eligible"]) > 0
        )
        show_all = spm_unit("wa_show_all_cash_assistance_programs", period)
        income_eligible = spm_unit("wa_tanf_income_eligible", period)
        resources_eligible = spm_unit("wa_tanf_resources_eligible", period.this_year)
        return (
            (has_rca_eligible_immigrant | show_all)
            & income_eligible
            & resources_eligible
        )
