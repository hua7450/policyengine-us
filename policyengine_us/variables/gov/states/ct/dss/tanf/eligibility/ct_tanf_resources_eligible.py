from policyengine_us.model_api import *


class ct_tanf_resources_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Connecticut TANF resource eligibility"
    definition_period = MONTH
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf

        # Use spm_unit_assets as simplified resource measure
        assets = spm_unit("spm_unit_assets", period.this_year)
        resource_limit = p.resource_limit

        return assets <= resource_limit
