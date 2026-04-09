from policyengine_us.model_api import *
from policyengine_us.variables.gov.states.ga.decal.caps.payment.ga_caps_quality_rating import (
    GACAPSQualityRating,
)


class ga_caps(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Georgia CAPS benefit amount"
    definition_period = MONTH
    defined_for = "ga_caps_eligible"
    reference = (
        "https://caps.decal.ga.gov/assets/downloads/CAPS/Appendix_C-CAPS_Reimbursement_Rates.pdf#page=2",
        "https://www.acf.hhs.gov/sites/default/files/documents/occ/georgia_2025_2027_ccdf_state_plan.pdf#page=110",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ga.decal.caps
        family_fee = spm_unit("ga_caps_family_fee", period)

        # Sum per-child weekly max rates (base, without quality).
        base_max_weekly = add(spm_unit, period, ["ga_caps_maximum_weekly_benefit"])
        base_max_monthly = base_max_weekly * (WEEKS_IN_YEAR / MONTHS_IN_YEAR)

        # Quality bonus: per-child, applied to the net base payment.
        person = spm_unit.members
        weekly_rate = person("ga_caps_maximum_weekly_benefit", period)
        quality_rating = person("ga_caps_quality_rating", period)
        star_count = select(
            [
                quality_rating == GACAPSQualityRating.ONE_STAR,
                quality_rating == GACAPSQualityRating.TWO_STAR,
                quality_rating == GACAPSQualityRating.THREE_STAR,
            ],
            [1, 2, 3],
            default=0,
        )
        bonus_rate = p.quality_rated.bonus_rate.calc(star_count)
        quality_enhanced_weekly = weekly_rate * (1 + bonus_rate)
        quality_max_monthly = spm_unit.sum(quality_enhanced_weekly) * (
            WEEKS_IN_YEAR / MONTHS_IN_YEAR
        )

        # Subsidy = min(expenses - fee, base max) floored at 0.
        # Quality bonus on the net base payment.
        pre_subsidy = spm_unit("spm_unit_pre_subsidy_childcare_expenses", period)
        base_subsidy = max_(min_(pre_subsidy - family_fee, base_max_monthly), 0)
        quality_bonus = quality_max_monthly - base_max_monthly
        return base_subsidy + where(base_subsidy > 0, quality_bonus, 0)
