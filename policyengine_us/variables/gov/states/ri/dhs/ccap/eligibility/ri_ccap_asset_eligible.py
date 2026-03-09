from policyengine_us.model_api import *


class ri_ccap_asset_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Rhode Island CCAP based on assets"
    definition_period = YEAR
    defined_for = StateCode.RI
    reference = "https://rules.sos.ri.gov/regulations/part/218-20-00-4#4.6.1"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.assets
        assets = spm_unit("ri_ccap_assets", period)
        return assets <= p.limit
