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
        p = parameters(period).gov.states.ct.dss.tanf
        size = spm_unit.nb_persons()
        # Payment standard varies by household size
        # Cap at size 8 (largest defined in parameter)
        # Use getattr to access numeric parameter keys
        capped_size = min_(size, 8)
        return select(
            [
                capped_size == 1,
                capped_size == 2,
                capped_size == 3,
                capped_size == 4,
                capped_size == 5,
                capped_size == 6,
                capped_size == 7,
                capped_size == 8,
            ],
            [
                getattr(p.payment_standard, "1"),
                getattr(p.payment_standard, "2"),
                getattr(p.payment_standard, "3"),
                getattr(p.payment_standard, "4"),
                getattr(p.payment_standard, "5"),
                getattr(p.payment_standard, "6"),
                getattr(p.payment_standard, "7"),
                getattr(p.payment_standard, "8"),
            ],
        )
