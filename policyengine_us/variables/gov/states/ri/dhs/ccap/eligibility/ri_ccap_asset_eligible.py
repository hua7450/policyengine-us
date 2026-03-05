from policyengine_us.model_api import *


class ri_ccap_asset_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Rhode Island CCAP based on assets"
    definition_period = MONTH
    reference = "https://dhs.ri.gov/media/9236/download?language=en#page=28"
    defined_for = StateCode.RI

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap
        assets = spm_unit("spm_unit_assets", period.this_year)
        return assets <= p.asset_limit
