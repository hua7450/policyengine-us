from policyengine_us.model_api import *


class nh_child_care_subsidies(Variable):
    value_type = float
    entity = SPMUnit
    label = "New Hampshire child care subsidies"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.NH
    adds = ["nh_ccap"]
