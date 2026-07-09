from policyengine_us.model_api import *


class oh_ccap_rate_with_addons(Variable):
    value_type = float
    entity = Person
    unit = USD
    label = "Ohio CCAP monthly maximum reimbursement rate after add-ons"
    definition_period = MONTH
    defined_for = "oh_ccap_eligible_child"
    reference = (
        "https://codes.ohio.gov/ohio-administrative-code/rule-5180:6-1-10",
        "https://codes.ohio.gov/ohio-administrative-code/rule-5180:2-16-09",
    )

    def formula(person, period, parameters):
        # 5180:6-1-10: the maximum rate is increased by quality, accredited,
        # non-traditional-hours, and special-needs add-ons, then capped at the
        # provider's customary charge.
        p = parameters(period).gov.states.oh.dcy.ccap.addons
        base_rate = person("oh_ccap_base_rate", period)
        customary_charge = person("pre_subsidy_childcare_expenses", period)

        # Quality: take the higher of the Step Up To Quality bonus and the
        # accredited bonus (5180:6-1-10).
        quality_tier = person("oh_ccap_quality_tier", period)
        sutq_pct = p.quality.sutq[quality_tier]
        is_accredited = person("oh_ccap_is_accredited", period)
        accredited_pct = where(is_accredited, p.accredited, 0)
        quality_pct = max_(sutq_pct, accredited_pct)

        # Non-traditional hours: +5%.
        non_traditional = person("oh_ccap_non_traditional_hours", period)
        non_traditional_pct = where(non_traditional, p.non_traditional_hours, 0)

        # Special needs: +5% of base, or 2x the base rate (an added factor of
        # the multiplier minus one) when special accommodations are approved
        # (5180:2-16-09).
        has_special_needs = person("oh_ccap_special_needs", period)
        has_accommodations = person("oh_ccap_has_special_accommodations", period)
        special_needs_add = where(
            has_special_needs,
            where(
                has_accommodations,
                p.special_needs_accommodations_multiplier - 1,
                p.special_needs,
            ),
            0,
        )

        rate_after_quality = base_rate * (1 + quality_pct)
        rate_with_addons = rate_after_quality * (
            1 + non_traditional_pct + special_needs_add
        )
        return min_(rate_with_addons, customary_charge)
