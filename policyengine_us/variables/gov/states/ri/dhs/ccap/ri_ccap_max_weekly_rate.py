from policyengine_us.model_api import *


class ri_ccap_max_weekly_rate(Variable):
    value_type = float
    entity = Person
    unit = USD
    label = "Rhode Island CCAP maximum weekly reimbursement rate"
    definition_period = MONTH
    reference = "https://dhs.ri.gov/media/9236/download?language=en#page=63"
    defined_for = StateCode.RI

    def formula(person, period, parameters):
        from policyengine_us.variables.gov.states.ri.dhs.ccap.ri_ccap_provider_type import (
            RICCAPProviderType,
        )

        p = parameters(period).gov.states.ri.dhs.ccap
        age = person("monthly_age", period)
        hours = person("childcare_hours_per_week", period.this_year)
        provider = person("ri_ccap_provider_type", period.this_year)
        star = max_(person("ri_ccap_quality_rating", period.this_year), 1)

        time_tier_idx = p.rates.time_tier.calc(hours)
        is_ft = time_tier_idx == 1
        is_3qt = time_tier_idx == 2
        is_ht = time_tier_idx == 3

        is_center = provider == RICCAPProviderType.CENTER
        is_family = provider == RICCAPProviderType.FAMILY

        infant_max = p.rates.age_threshold.center_infant_max
        toddler_max = p.rates.age_threshold.toddler_max
        preschool_max = p.rates.age_threshold.preschool_max

        is_infant_center = is_center & (age < infant_max)
        is_toddler_center = (
            is_center & (age >= infant_max) & (age < toddler_max)
        )
        is_preschool_center = (
            is_center & (age >= toddler_max) & (age < preschool_max)
        )
        is_school_age_center = is_center & (age >= preschool_max)

        is_infant_toddler_non_center = ~is_center & (age < toddler_max)
        is_preschool_non_center = (
            ~is_center & (age >= toddler_max) & (age < preschool_max)
        )
        is_school_age_non_center = ~is_center & (age >= preschool_max)

        rates = p.rates

        # Center rates by age and time tier.
        center_infant = select(
            [is_ft, is_3qt, is_ht],
            [
                rates.center.infant.full_time.calc(star),
                rates.center.infant.three_quarter_time.calc(star),
                rates.center.infant.half_time.calc(star),
            ],
            default=rates.center.infant.quarter_time.calc(star),
        )
        center_toddler = select(
            [is_ft, is_3qt, is_ht],
            [
                rates.center.toddler.full_time.calc(star),
                rates.center.toddler.three_quarter_time.calc(star),
                rates.center.toddler.half_time.calc(star),
            ],
            default=rates.center.toddler.quarter_time.calc(star),
        )
        center_preschool = select(
            [is_ft, is_3qt, is_ht],
            [
                rates.center.preschool.full_time.calc(star),
                rates.center.preschool.three_quarter_time.calc(star),
                rates.center.preschool.half_time.calc(star),
            ],
            default=rates.center.preschool.quarter_time.calc(star),
        )
        center_school_age = select(
            [is_ft, is_3qt, is_ht],
            [
                rates.center.school_age.full_time.calc(star),
                rates.center.school_age.three_quarter_time.calc(star),
                rates.center.school_age.half_time.calc(star),
            ],
            default=rates.center.school_age.quarter_time.calc(star),
        )

        # Family rates by age and time tier.
        family_infant_toddler = select(
            [is_ft, is_3qt, is_ht],
            [
                rates.family.infant_toddler.full_time.calc(star),
                rates.family.infant_toddler.three_quarter_time.calc(star),
                rates.family.infant_toddler.half_time.calc(star),
            ],
            default=rates.family.infant_toddler.quarter_time.calc(star),
        )
        family_preschool = select(
            [is_ft, is_3qt, is_ht],
            [
                rates.family.preschool.full_time.calc(star),
                rates.family.preschool.three_quarter_time.calc(star),
                rates.family.preschool.half_time.calc(star),
            ],
            default=rates.family.preschool.quarter_time.calc(star),
        )
        family_school_age = select(
            [is_ft, is_3qt, is_ht],
            [
                rates.family.school_age.full_time.calc(star),
                rates.family.school_age.three_quarter_time.calc(star),
                rates.family.school_age.half_time.calc(star),
            ],
            default=rates.family.school_age.quarter_time.calc(star),
        )

        # Exempt rates by age and time tier.
        exempt_infant_toddler = select(
            [is_ft, is_3qt, is_ht],
            [
                rates.exempt.infant_toddler.full_time.calc(star),
                rates.exempt.infant_toddler.three_quarter_time.calc(star),
                rates.exempt.infant_toddler.half_time.calc(star),
            ],
            default=rates.exempt.infant_toddler.quarter_time.calc(star),
        )
        exempt_preschool = select(
            [is_ft, is_3qt, is_ht],
            [
                rates.exempt.preschool.full_time.calc(star),
                rates.exempt.preschool.three_quarter_time.calc(star),
                rates.exempt.preschool.half_time.calc(star),
            ],
            default=rates.exempt.preschool.quarter_time.calc(star),
        )
        exempt_school_age = select(
            [is_ft, is_3qt, is_ht],
            [
                rates.exempt.school_age.full_time.calc(star),
                rates.exempt.school_age.three_quarter_time.calc(star),
                rates.exempt.school_age.half_time.calc(star),
            ],
            default=rates.exempt.school_age.quarter_time.calc(star),
        )

        # Select rate by provider type and age category.
        center_rate = select(
            [
                is_infant_center,
                is_toddler_center,
                is_preschool_center,
            ],
            [center_infant, center_toddler, center_preschool],
            default=center_school_age,
        )

        family_rate = select(
            [is_infant_toddler_non_center, is_preschool_non_center],
            [family_infant_toddler, family_preschool],
            default=family_school_age,
        )

        exempt_rate = select(
            [is_infant_toddler_non_center, is_preschool_non_center],
            [exempt_infant_toddler, exempt_preschool],
            default=exempt_school_age,
        )

        eligible_child = person("ri_ccap_eligible_child", period)
        rate = select(
            [is_center, is_family],
            [center_rate, family_rate],
            default=exempt_rate,
        )
        return where(eligible_child, rate, 0)
