from policyengine_us.model_api import *
from policyengine_us.variables.gov.states.hi.dhs.oss.hi_oss_living_arrangement import (
    HIOSSLivingArrangement,
)


class hi_oss_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Whether the person is eligible for Hawaii OSS"
    definition_period = YEAR
    defined_for = StateCode.HI
    reference = (
        "https://secure.ssa.gov/apps10/poms.nsf/lnx/0501415200SF",
        "https://secure.ssa.gov/POMS.NSF/lnx/0501415057",
    )

    def formula(person, period, parameters):
        receives_ssi = person("ssi", period) > 0
        living_arrangement = person("hi_oss_living_arrangement", period)
        in_qualifying_facility = (
            living_arrangement != HIOSSLivingArrangement.NONE
        )
        return receives_ssi & in_qualifying_facility
