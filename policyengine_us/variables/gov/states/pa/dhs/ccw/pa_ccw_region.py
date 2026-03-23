from policyengine_us.model_api import *


class pa_ccw_region(Variable):
    value_type = int
    entity = Household
    definition_period = YEAR
    default_value = 1
    label = "Pennsylvania CCW MCCA payment region"
    defined_for = StateCode.PA
    reference = "https://www.pacodeandbulletin.gov/secure/pacode/data/055/chapter3042/055_3042.pdf#page=10"
