from policyengine_us.model_api import *


class or_erdc_eligible_child(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible child for Oregon ERDC"
    defined_for = StateCode.OR
    reference = "https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=7871"

    def formula(person, period, parameters):
        p = parameters(period).gov.states["or"].delc.erdc.age_threshold
        age = person("age", period.this_year)
        special_circumstances = (
            person("is_incapable_of_self_care", period.this_year)
            | person("is_in_foster_care", period.this_year)
            | person("or_erdc_high_needs_rate_eligible", period.this_year)
            | person("or_erdc_special_circumstances_child", period.this_year)
        )
        return (age < p.child) | (
            (age < p.special_circumstances_child) & special_circumstances
        )
