from policyengine_us.model_api import *


class has_esi(Variable):
    value_type = bool
    entity = Person
    label = "Person currently has ESI"
    definition_period = YEAR

    def formula(person, period, parameters):
        return person(
            "reported_has_employer_sponsored_health_coverage_at_interview",
            period,
        )
