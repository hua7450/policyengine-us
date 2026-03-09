from policyengine_us.model_api import *


class ri_ccap_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Eligible child for Rhode Island CCAP"
    definition_period = YEAR
    defined_for = StateCode.RI
    reference = "https://rules.sos.ri.gov/regulations/part/218-20-00-4#4.3.1"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.age_threshold
        age = person("age", period)
        is_disabled = person("is_disabled", period)
        # Non-disabled: "under thirteen (13)" -> age < 13
        # Disabled: "up through eighteen (18)" -> age <= 18
        age_eligible = where(is_disabled, age <= p.disabled_child, age < p.child)
        is_dependent = person("is_tax_unit_dependent", period)
        immigration_eligible = person(
            "ri_ccap_immigration_status_eligible_child", period
        )
        return age_eligible & is_dependent & immigration_eligible
