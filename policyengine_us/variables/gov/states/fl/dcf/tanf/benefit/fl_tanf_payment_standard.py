from policyengine_us.model_api import *


class fl_tanf_payment_standard(Variable):
    value_type = float
    entity = SPMUnit
    label = "Florida TANF payment standard"
    unit = USD
    definition_period = MONTH
    reference = "Florida Statute § 414.095(10)"
    documentation = (
        "Florida TANF payment standard based on family size and shelter tier."
    )
    defined_for = StateCode.FL

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.fl.dcf.tanf.payment_standard

        family_size = spm_unit("spm_unit_size", period)
        tier = spm_unit("fl_tanf_shelter_tier", period)

        # Cap family size at 13 (max size in parameter tables)
        capped_size = min_(family_size, 13)

        # Get payment standard based on tier
        tier_1_amount = p.tier_1[capped_size]
        tier_2_amount = p.tier_2[capped_size]
        tier_3_amount = p.tier_3[capped_size]

        payment_standard = select(
            [tier == 1, tier == 2, tier == 3],
            [tier_1_amount, tier_2_amount, tier_3_amount],
        )

        return payment_standard
