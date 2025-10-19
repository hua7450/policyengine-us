from policyengine_us.model_api import *


class ct_tanf(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut Temporary Family Assistance (TFA/TANF)"
    documentation = "Monthly cash assistance benefit for Connecticut TFA. Benefit equals payment standard minus countable income. Extended eligibility provisions (earnings 171-230% FPL with 20% reduction) are not yet implemented."
    unit = USD
    reference = "CGS § 17b-112"
    defined_for = "ct_tanf_eligible"

    def formula(spm_unit, period, parameters):
        payment_standard = spm_unit("ct_tanf_payment_standard", period)
        countable_income = spm_unit("ct_tanf_countable_income", period)

        # Benefit = Payment Standard - Countable Income
        # Cannot be negative
        return max_(payment_standard - countable_income, 0)
