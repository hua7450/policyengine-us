from policyengine_us.model_api import *


class ri_ccap_weekly_benefit(Variable):
    value_type = float
    entity = Person
    unit = USD
    label = "Rhode Island CCAP weekly benefit for each child"
    definition_period = MONTH
    reference = (
        "https://dhs.ri.gov/media/9236/download?language=en#page=31",
        "https://dhs.ri.gov/media/9236/download?language=en#page=63",
    )
    defined_for = StateCode.RI

    def formula(person, period, parameters):
        eligible_child = person("ri_ccap_eligible_child", period)
        rate = person("ri_ccap_max_weekly_rate", period)
        age = person("monthly_age", period)
        # Per Section 4.6.1(C)(2)(a), copay is assigned to youngest
        # eligible child. Use large age for ineligible children so they
        # never match as youngest.
        effective_age = where(eligible_child, age, 1e6)
        youngest_age = person.spm_unit.min(effective_age)
        is_youngest = eligible_child & (age == youngest_age)
        family_share = person.spm_unit("ri_ccap_family_share", period)
        return where(
            is_youngest,
            max_(rate - family_share, 0),
            where(eligible_child, rate, 0),
        )
