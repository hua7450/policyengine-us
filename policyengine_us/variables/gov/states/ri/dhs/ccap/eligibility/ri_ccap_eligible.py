from policyengine_us.model_api import *


class ri_ccap_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Eligible for the Rhode Island Child Care Assistance Program"
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3"
    defined_for = StateCode.RI

    def formula(spm_unit, period, parameters):
        income_eligible = spm_unit("ri_ccap_income_eligible", period)
        asset_eligible = spm_unit("ri_ccap_asset_eligible", period)
        has_eligible_child = (
            add(spm_unit, period, ["ri_ccap_child_eligible"]) > 0
        )
        return income_eligible & asset_eligible & has_eligible_child
