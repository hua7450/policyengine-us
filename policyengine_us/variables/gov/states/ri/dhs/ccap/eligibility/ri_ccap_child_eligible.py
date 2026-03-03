from policyengine_us.model_api import *


class ri_ccap_child_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible child for the Rhode Island Child Care Assistance Program"
    reference = (
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.2",
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3",
    )
    defined_for = StateCode.RI

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.eligibility
        age = person("age", period.this_year)
        is_disabled = person("is_disabled", period.this_year)
        # Under 13, or under 19 if disabled
        age_limit = where(
            is_disabled, p.disabled_child_age_limit, p.child_age_limit
        )
        return age < age_limit
