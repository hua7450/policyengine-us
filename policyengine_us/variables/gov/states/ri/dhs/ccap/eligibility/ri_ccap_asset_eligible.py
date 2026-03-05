from policyengine_us.model_api import *


class ri_ccap_asset_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Asset eligible for the Rhode Island Child Care Assistance Program"
    reference = (
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3",
        "https://dhs.ri.gov/media/7311/download?language=en#page=25",
    )
    defined_for = StateCode.RI

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.eligibility
        assets = spm_unit("spm_unit_assets", period.this_year)
        return assets <= p.asset_limit
