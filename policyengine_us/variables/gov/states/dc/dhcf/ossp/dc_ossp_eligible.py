from policyengine_us.model_api import *
from policyengine_us.variables.gov.states.dc.dhcf.ossp.dc_ossp_living_arrangement import (
    DCOSSPLivingArrangement,
)


class dc_ossp_eligible(Variable):
    value_type = bool
    entity = Person
    label = "DC OSSP eligible"
    definition_period = MONTH
    defined_for = StateCode.DC
    reference = (
        "https://code.dccouncil.gov/us/dc/council/code/sections/4-205.49",
        "https://www.ssa.gov/pubs/EN-05-11162.pdf#page=2",
    )

    def formula(person, period, parameters):
        categorically_eligible = person("is_ssi_eligible", period.this_year)
        receives_ssi = person("ssi", period) > 0
        living_arrangement = person("dc_ossp_living_arrangement", period)
        in_qualifying_facility = living_arrangement != DCOSSPLivingArrangement.NONE
        return categorically_eligible & receives_ssi & in_qualifying_facility
