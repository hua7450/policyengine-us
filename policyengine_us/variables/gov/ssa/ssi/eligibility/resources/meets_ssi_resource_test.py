from policyengine_us.model_api import *


class meets_ssi_resource_test(Variable):
    value_type = bool
    entity = Person
    label = "Meets SSI resource test"
    definition_period = YEAR
    reference = "https://secure.ssa.gov/poms.nsf/lnx/0501110000"

    def formula(person, period, parameters):
        p = parameters(period).gov.ssa.ssi
        couple_computation = person("ssi_couple_computation_applies", period)
        personal_resources = person("ssi_countable_resources", period)
        countable_resources = where(
            couple_computation,
            person.marital_unit.sum(personal_resources),
            personal_resources,
        )
        resource_limit = where(
            couple_computation,
            p.eligibility.resources.limit.couple,
            p.eligibility.resources.limit.individual,
        )
        return countable_resources <= resource_limit
