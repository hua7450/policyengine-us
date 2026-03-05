from policyengine_us.model_api import *


class ri_ccap_immigration_status_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Rhode Island Child Care Assistance Program (CCAP) based on immigration status"
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3"
    defined_for = StateCode.RI

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap
        immigration_status = person("immigration_status", period.this_year)
        immigration_status_str = immigration_status.decode_to_str()
        has_qualifying_status = np.isin(
            immigration_status_str,
            p.qualified_alien_statuses,
        )
        is_citizen = (
            immigration_status == immigration_status.possible_values.CITIZEN
        )
        return has_qualifying_status | is_citizen
