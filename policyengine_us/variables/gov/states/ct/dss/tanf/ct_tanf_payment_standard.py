from policyengine_us.model_api import *


class ct_tanf_payment_standard(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA payment standard"
    unit = USD
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf.payment_standard
        size = spm_unit("spm_unit_size", period)

        # Cap at maximum family size in parameter (8)
        max_size = 8
        capped_size = min_(size, max_size).astype(int)

        return p[capped_size]
