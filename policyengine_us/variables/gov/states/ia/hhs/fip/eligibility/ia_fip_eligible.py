from policyengine_us.model_api import *


class ia_fip_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Iowa FIP"
    definition_period = MONTH
    reference = (
        "https://www.law.cornell.edu/regulations/iowa/Iowa-Admin-Code-r-441-41-27",
        "https://www.law.cornell.edu/regulations/iowa/Iowa-Admin-Code-r-441-41-26",
    )
    defined_for = StateCode.IA

    def formula(spm_unit, period, parameters):
        demographic_eligible = spm_unit("is_demographic_tanf_eligible", period)
        immigration_eligible = (
            add(spm_unit, period, ["is_citizen_or_legal_immigrant"]) > 0
        )
        gross_income_eligible = spm_unit(
            "ia_fip_gross_income_eligible", period
        )
        income_eligible = spm_unit("ia_fip_income_eligible", period)
        resources_eligible = spm_unit("ia_fip_resources_eligible", period)
        return (
            demographic_eligible
            & immigration_eligible
            & gross_income_eligible
            & income_eligible
            & resources_eligible
        )
