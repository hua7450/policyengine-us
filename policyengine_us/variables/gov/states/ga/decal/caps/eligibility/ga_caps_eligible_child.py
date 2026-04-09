from policyengine_us.model_api import *


class ga_caps_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Eligible child for Georgia CAPS"
    definition_period = MONTH
    defined_for = StateCode.GA
    reference = (
        "https://caps.decal.ga.gov/assets/downloads/CAPS/02-CAPS_Policy-Chapter_6.pdf#page=3",
        "https://www.acf.hhs.gov/sites/default/files/documents/occ/georgia_2025_2027_ccdf_state_plan.pdf#page=49",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ga.decal.caps.age_threshold
        age = person("age", period.this_year)
        is_disabled = person("is_disabled", period.this_year)
        age_eligible = where(is_disabled, age <= p.disabled_child, age < p.child)
        immigration_eligible = person(
            "is_ccdf_immigration_eligible_child", period.this_year
        )
        return age_eligible & immigration_eligible
