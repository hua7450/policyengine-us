from policyengine_us.model_api import *


class fl_tanf(Variable):
    value_type = float
    entity = SPMUnit
    label = "Florida Temporary Cash Assistance (TANF)"
    unit = USD
    definition_period = MONTH
    reference = "Florida Statute § 414.095(12)"
    documentation = """
    Florida TANF benefit calculation:
    Benefit = Payment Standard - Countable Income
    Rounded down to nearest dollar, minimum $10 to receive cash
    """
    defined_for = "fl_tanf_eligible"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.fl.dcf.tanf

        payment_standard = spm_unit("fl_tanf_payment_standard", period)
        countable_income = spm_unit("fl_tanf_countable_income", period)

        # Calculate benefit
        calculated_benefit = payment_standard - countable_income

        # Apply minimum benefit threshold
        # If below minimum, family retains categorical eligibility but receives no cash
        benefit = where(
            calculated_benefit >= p.minimum_benefit, calculated_benefit, 0
        )

        return max_(benefit, 0)
