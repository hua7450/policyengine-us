from policyengine_us.model_api import *


class ct_tanf_countable_resources(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA countable resources"
    unit = USD
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        # Simplified implementation - use spm_unit_cash_assets directly
        # Full implementation would apply vehicle exclusion
        cash_assets = spm_unit("spm_unit_cash_assets", period.this_year)
        return cash_assets
