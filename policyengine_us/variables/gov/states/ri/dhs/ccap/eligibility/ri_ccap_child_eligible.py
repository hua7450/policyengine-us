from policyengine_us.model_api import *


class ri_ccap_child_eligible(Variable):
    value_type = bool
    entity = Person
    label = (
        "Eligible child for Rhode Island Child Care Assistance Program (CCAP)"
    )
    definition_period = MONTH
    defined_for = StateCode.RI
    reference = (
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3",
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.2",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.age_limit
        age = person("monthly_age", period)
        is_disabled = person("is_disabled", period)
        age_limit = where(is_disabled, p.special_needs_child, p.child)
        age_eligible = age < age_limit
        is_dependent = person("is_tax_unit_dependent", period)
        immigration_eligible = person(
            "ri_ccap_immigration_status_eligible", period
        )
        return age_eligible & is_dependent & immigration_eligible
