from policyengine_us.model_api import *


class md_ccs_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Eligible child for Maryland Child Care Scholarship (CCS)"
    definition_period = MONTH
    defined_for = StateCode.MD
    reference = "https://dsd.maryland.gov/regulations/Pages/13A.14.06.02.aspx"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.md.msde.ccs.age_threshold
        age = person("age", period.this_year)
        is_disabled = person("is_disabled", period.this_year)
        age_limit = where(is_disabled, p.disabled_child, p.child)
        age_eligible = age < age_limit
        is_dependent = person("is_tax_unit_dependent", period.this_year)
        immigration_eligible = person(
            "is_ccdf_immigration_eligible_child", period.this_year
        )
        return age_eligible & is_dependent & immigration_eligible
