from policyengine_us.model_api import *
from policyengine_us.variables.gov.states.dc.dhcf.ossp.dc_ossp_living_arrangement import (
    DCOSSPLivingArrangement,
)


class dc_ossp_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Whether the person is eligible for DC OSSP"
    definition_period = YEAR
    defined_for = StateCode.DC
    reference = (
        "https://code.dccouncil.gov/us/dc/council/code/sections/4-205.49",
        "https://secure.ssa.gov/poms.nsf/lnx/0501415009",
    )

    def formula(person, period, parameters):
        ssi_eligible = person("dc_ossp_ssi_eligible", period)
        resource_eligible = person("dc_ossp_resource_eligible", period)
        living_arrangement = person("dc_ossp_living_arrangement", period)
        in_qualifying_facility = living_arrangement != DCOSSPLivingArrangement.NONE
        return ssi_eligible & resource_eligible & in_qualifying_facility
