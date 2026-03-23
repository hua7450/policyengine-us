from policyengine_us.model_api import *


class pa_ccw_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Eligible child for Pennsylvania CCW"
    definition_period = MONTH
    defined_for = StateCode.PA
    reference = (
        "https://www.pacodeandbulletin.gov/secure/pacode/data/055/chapter3042/055_3042.pdf#page=9",
        "https://www.pacodeandbulletin.gov/secure/pacode/data/055/chapter3042/055_3042.pdf#page=16",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.pa.dhs.ccw.eligibility.age_threshold
        age = person("age", period.this_year)
        is_disabled = person("is_disabled", period.this_year)
        age_eligible = where(is_disabled, age < p.disabled_child, age < p.child)
        is_dependent = person("is_tax_unit_dependent", period.this_year)
        immigration_eligible = person(
            "is_ccdf_immigration_eligible_child", period.this_year
        )
        return age_eligible & is_dependent & immigration_eligible
