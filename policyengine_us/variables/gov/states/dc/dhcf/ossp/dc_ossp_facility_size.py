from policyengine_us.model_api import *


class dc_ossp_facility_size(Variable):
    value_type = int
    entity = Person
    label = "Number of beds in the adult foster care facility"
    definition_period = YEAR
    defined_for = StateCode.DC
    default_value = 0
    reference = ("https://secure.ssa.gov/poms.nsf/lnx/0501415009",)
