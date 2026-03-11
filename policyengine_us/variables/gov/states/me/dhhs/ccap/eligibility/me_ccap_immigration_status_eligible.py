from policyengine_us.model_api import *


class me_ccap_immigration_status_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Immigration status eligible for Maine CCAP"
    definition_period = MONTH
    defined_for = StateCode.ME
    reference = (
        "https://www.maine.gov/sos/cec/rules/10/ch6.pdf#page=5",
        "https://www.law.cornell.edu/uscode/text/8/1641",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.me.dhhs.ccap
        immigration_status = person("immigration_status", period)
        immigration_status_str = immigration_status.decode_to_str()
        has_qualifying_status = np.isin(
            immigration_status_str,
            p.qualified_alien_statuses,
        )
        is_citizen = immigration_status == immigration_status.possible_values.CITIZEN
        return has_qualifying_status | is_citizen
