from policyengine_us.model_api import *


class ct_tanf_countable_resources(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = YEAR
    label = "Connecticut TFA countable resources"
    unit = USD
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = StateCode.CT

    # Simplified implementation - use spm_unit_assets directly
    # Full implementation would apply vehicle exclusion
    adds = ["spm_unit_assets"]
