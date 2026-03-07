from policyengine_us.model_api import *


class dc_ossp_in_nursing_facility(Variable):
    value_type = bool
    entity = Person
    label = "Whether the person resides in a nursing facility"
    definition_period = YEAR
    defined_for = StateCode.DC
    default_value = False
    reference = ("https://code.dccouncil.gov/us/dc/council/code/sections/4-205.49",)
