from policyengine_us.model_api import *


class dc_ossp_resource_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Whether the person meets resource limits for DC OSSP"
    definition_period = YEAR
    defined_for = StateCode.DC
    reference = ("https://secure.ssa.gov/poms.nsf/lnx/0501415009",)

    def formula(person, period, parameters):
        resources = person("ssi_countable_resources", period.this_year)
        is_married = person.family("is_married", period.this_year)
        p = parameters(period).gov.states.dc.dhcf.ossp.resource_limit
        limit = where(
            is_married,
            p.couple.amount,
            p.individual.amount,
        )
        return resources <= limit
