from policyengine_us.model_api import *


class me_ccap_asset_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Asset eligible for Maine CCAP"
    definition_period = MONTH
    defined_for = StateCode.ME
    reference = "https://www.maine.gov/dhhs/sites/maine.gov.dhhs/files/inline-files/CCAP%20Full%20Rule%208.18.2025_1.pdf#page=11"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.me.dhhs.ccap
        total_assets = spm_unit("spm_unit_assets", period.this_year)
        return total_assets <= p.asset_limit
