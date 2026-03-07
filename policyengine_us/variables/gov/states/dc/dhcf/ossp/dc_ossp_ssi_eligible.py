from policyengine_us.model_api import *


class dc_ossp_ssi_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Whether the person meets SSI eligibility for DC OSSP"
    definition_period = YEAR
    defined_for = StateCode.DC
    reference = ("https://code.dccouncil.gov/us/dc/council/code/sections/4-205.49",)

    def formula(person, period, parameters):
        return person("is_ssi_eligible_individual", period)
