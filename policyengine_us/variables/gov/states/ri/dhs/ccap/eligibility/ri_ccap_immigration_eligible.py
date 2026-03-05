from policyengine_us.model_api import *


class ri_ccap_immigration_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Rhode Island CCAP based on immigration status"
    definition_period = MONTH
    reference = "https://dhs.ri.gov/media/9236/download?language=en#page=16"
    defined_for = StateCode.RI

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap
        immigration_status = person("immigration_status", period)
        immigration_status_str = immigration_status.decode_to_str()
        has_qualifying_status = np.isin(
            immigration_status_str,
            p.qualified_immigrant_statuses,
        )
        is_citizen = (
            immigration_status == immigration_status.possible_values.CITIZEN
        )
        return has_qualifying_status | is_citizen
