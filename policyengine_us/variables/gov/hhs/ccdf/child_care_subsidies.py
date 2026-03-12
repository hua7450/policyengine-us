from policyengine_us.model_api import *

# All implemented state child care subsidy programs.
STATE_CHILD_CARE_SUBSIDY_VARIABLES = [
    "ca_child_care_subsidies",
    "co_child_care_subsidies",
    "ma_child_care_subsidies",
    "ne_child_care_subsidies",
]


class child_care_subsidies(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = YEAR
    label = "Child care subsidies"
    unit = USD

    adds = STATE_CHILD_CARE_SUBSIDY_VARIABLES
