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

        # Base payment capped at actual expenses.
        pre_subsidy = spm_unit("spm_unit_pre_subsidy_childcare_expenses", period)
        base_payment = min_(pre_subsidy, base_max_monthly)

        # Net base payment = base payment less family fee, floored at 0.
        net_base = max_(base_payment - family_fee, 0)

        # Quality bonus: per-child weighted average bonus rate.
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
        weighted_bonus = spm_unit.sum(weekly_rate * bonus_rate)
        effective_bonus_rate = np.divide(
            weighted_bonus,
            base_max_weekly,
            out=np.zeros_like(weighted_bonus),
            where=base_max_weekly > 0,
        )

        # Subsidy = net base payment * (1 + effective quality bonus rate).
        return net_base * (1 + effective_bonus_rate)
