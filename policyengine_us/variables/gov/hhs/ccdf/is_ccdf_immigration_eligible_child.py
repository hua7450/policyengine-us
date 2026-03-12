from policyengine_us.model_api import *


class is_ccdf_immigration_eligible_child(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Immigration eligibility for CCDF"
    reference = (
        "https://www.law.cornell.edu/uscode/text/8/1641",
        "https://www.law.cornell.edu/cfr/text/45/section-98.20#c",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.hhs.ccdf
        immigration_status = person("immigration_status", period)
        immigration_status_str = immigration_status.decode_to_str()
        return np.isin(
            immigration_status_str,
            p.qualified_immigration_statuses,
        )
