from policyengine_us.model_api import *


class ct_tanf_payment_standard(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA payment standard"
    documentation = "Maximum monthly benefit amount for Connecticut TFA by household size. Geographic variation exists but is not currently implemented due to incomplete documentation. Uses highest-cost region standard."
    unit = USD
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf.payment_standard
        # Use spm_unit_size variable (simplified - assumes everyone in unit is eligible)
        unit_size = spm_unit("spm_unit_size", period)
        # Cap at size 8 (largest defined in parameter)
        capped_unit_size = min_(unit_size, 8)
        # Index directly into parameter using household size
        return p.amount[capped_unit_size]
