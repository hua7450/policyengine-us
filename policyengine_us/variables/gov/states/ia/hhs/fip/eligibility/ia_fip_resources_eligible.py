from policyengine_us.model_api import *


class ia_fip_resources_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Iowa FIP resources eligible"
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/regulations/iowa/Iowa-Admin-Code-r-441-41-26"
    defined_for = StateCode.IA

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ia.hhs.fip.resources
        resources = spm_unit("spm_unit_assets", period.this_year)
        return resources <= p.limit
