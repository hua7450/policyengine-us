from policyengine_us.model_api import *


class ri_ccap_immigration_status_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Eligible child for Rhode Island CCAP based on immigration status"
    definition_period = YEAR
    defined_for = StateCode.RI
    reference = "https://rules.sos.ri.gov/regulations/part/218-20-00-4#4.3.1"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap
        immigration_status = person("immigration_status", period)
        immigration_status_str = immigration_status.decode_to_str()
        return np.isin(
            immigration_status_str,
            p.qualified_immigration_statuses,
        )
