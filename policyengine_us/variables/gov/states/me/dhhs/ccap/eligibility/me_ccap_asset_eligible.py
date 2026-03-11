from policyengine_us.model_api import *


class me_ccap_asset_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Asset eligible for Maine CCAP"
    definition_period = MONTH
    defined_for = StateCode.ME
    reference = "https://www.maine.gov/sos/cec/rules/10/ch6.pdf#page=7"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.me.dhhs.ccap
        total_assets = spm_unit("spm_unit_assets", period.this_year)
        return total_assets <= p.asset_limit
