from policyengine_us.model_api import *


class ct_tanf_countable_resources(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = YEAR
    label = "Connecticut TFA countable resources"
    documentation = "Total countable resources for Connecticut TFA eligibility. Simplified implementation using SPM unit assets. Full implementation would exclude one vehicle under $9,500 equity value and vehicles used to transport household members with disabilities."
    unit = USD
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        # Simplified implementation - use spm_unit_assets
        # Full implementation would apply vehicle exclusion based on
        # vehicle equity (value - loan) < $9,500 or disability transport
        return spm_unit("spm_unit_assets", period)
