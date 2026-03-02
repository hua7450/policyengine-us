from policyengine_us.model_api import *


class mn_mfip(Variable):
    value_type = float
    entity = SPMUnit
    label = "Minnesota MFIP"
    unit = USD
    definition_period = MONTH
    reference = (
        "https://www.revisor.mn.gov/statutes/cite/142G.16#stat.142G.16.2"
    )
    defined_for = "mn_mfip_eligible"

    def formula(spm_unit, period, parameters):
        # Per MN Stat. 142G.16, Subd. 2 (benefit calculation):
        # (a) FWL - countable earned = X, cap at full transitional standard
        # (d) X - unearned = gross benefit
        # The full TS (cash + food) is used for the calculation per statute.
        # The food portion is then subtracted because PolicyEngine models
        # SNAP separately.
        # Dependent care deduction does NOT apply to benefit calculation.
        cash_ts = spm_unit("mn_mfip_transitional_standard", period)
        food = spm_unit("mn_mfip_food_portion", period)
        full_ts = cash_ts + food
        family_wage_level = spm_unit("mn_mfip_family_wage_level", period)
        countable_earned = spm_unit("mn_mfip_countable_earned_income", period)
        countable_unearned = spm_unit(
            "mn_mfip_countable_unearned_income", period
        )
        # Step 1: Subtract countable earned from FWL, floor at 0
        fwl_minus_earned = max_(family_wage_level - countable_earned, 0)
        # Step 2: Cap at full transitional standard
        earned_based_benefit = min_(fwl_minus_earned, full_ts)
        # Step 3: Subtract countable unearned income, floor at zero
        gross_benefit = max_(earned_based_benefit - countable_unearned, 0)
        # Step 4: Subtract food portion (modeled separately via SNAP)
        return max_(gross_benefit - food, 0)
