from policyengine_us.model_api import *


class ct_tanf_payment_standard(Variable):
    value_type = float
    entity = SPMUnit
    label = "Connecticut TANF payment standard"
    unit = USD
    definition_period = MONTH
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf.payment_standard
        size = spm_unit("spm_unit_size", period)
        capped_size = min_(size, 8).astype(int)
        return p[capped_size]
