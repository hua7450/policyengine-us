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
        age_limit = where(is_disabled, p.disabled_child, p.child)
        age_eligible = age < age_limit
        is_dependent = person("is_tax_unit_dependent", period)
        immigration_eligible = person(
            "ri_ccap_immigration_status_eligible_child", period
        )
        return age_eligible & is_dependent & immigration_eligible
