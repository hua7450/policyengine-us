from policyengine_us.model_api import *


class wa_eceap_age_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Age-eligible for Washington ECEAP"
    definition_period = YEAR
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=43.216.505",
        "https://app.leg.wa.gov/WAC/default.aspx?cite=110-425-0080",
    )

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(period).gov.states.wa.dcyf.eceap.eligibility.age
        return p.age_range.calc(age)
