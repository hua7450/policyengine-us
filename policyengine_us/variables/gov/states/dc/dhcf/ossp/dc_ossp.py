from policyengine_us.model_api import *


class dc_ossp(Variable):
    value_type = float
    entity = Person
    label = "DC Optional State Supplemental Payment"
    unit = USD
    definition_period = YEAR
    defined_for = "dc_ossp_eligible"
    reference = (
        "https://code.dccouncil.gov/us/dc/council/code/sections/4-205.49",
        "https://secure.ssa.gov/poms.nsf/lnx/0501415009",
    )

    def formula(person, period, parameters):
        monthly_amount = person("dc_ossp_payment_amount", period)
        return monthly_amount * MONTHS_IN_YEAR
