from policyengine_us.model_api import *


class ri_ccap_asset_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Rhode Island Child Care Assistance Program (CCAP) based on assets"
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.6"
    defined_for = StateCode.RI

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap
        assets = spm_unit("spm_unit_cash_assets", period.this_year)
        return assets <= p.asset_limit
