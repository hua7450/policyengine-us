from policyengine_us.model_api import *

# All implemented state child care subsidy programs.
STATE_CHILD_CARE_SUBSIDY_VARIABLES = [
    "ca_child_care_subsidies",  # California Child Care
    "co_child_care_subsidies",  # Colorado Child Care Assistance Program
    "ma_child_care_subsidies",  # Massachusetts Child Care Financial Assistance
    "ne_child_care_subsidies",  # Nebraska Child Care Subsidy
]


class child_care_subsidies(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = YEAR
    label = "Child care subsidies"
    unit = USD

    adds = STATE_CHILD_CARE_SUBSIDY_VARIABLES
