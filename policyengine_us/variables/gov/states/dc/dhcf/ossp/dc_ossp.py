from policyengine_us.model_api import *


class dc_ossp(Variable):
    value_type = float
    entity = Person
    label = "DC Optional State Supplemental Payment"
    unit = USD
    definition_period = MONTH
    defined_for = "dc_ossp_eligible"
    reference = (
        "https://code.dccouncil.gov/us/dc/council/code/sections/4-205.49",
        "https://www.ssa.gov/pubs/EN-05-11162.pdf#page=2",
    )
    adds = ["dc_ossp_payment_amount"]
