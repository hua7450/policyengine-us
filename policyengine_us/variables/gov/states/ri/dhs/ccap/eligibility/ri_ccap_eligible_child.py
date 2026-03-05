from policyengine_us.model_api import *


class ri_ccap_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = (
        "Eligible child for Rhode Island Child Care Assistance Program (CCAP)"
    )
    definition_period = MONTH
    reference = "https://dhs.ri.gov/media/9236/download?language=en#page=15"
    defined_for = StateCode.RI

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.age_limit
        age = person("monthly_age", period)
        is_disabled = person("is_disabled", period.this_year)
        max_age = where(is_disabled, p.disabled_child, p.child)
        min_age_years = p.min_age_weeks / WEEKS_IN_YEAR
        age_eligible = (age >= min_age_years) & (age < max_age)
        is_dependent = person("is_tax_unit_dependent", period.this_year)
        immigration_eligible = person("ri_ccap_immigration_eligible", period)
        return age_eligible & is_dependent & immigration_eligible
