from policyengine_us.model_api import *


class reported_snap_amount(Variable):
    value_type = float
    entity = SPMUnit
    label = "Reported SNAP amount"
    unit = USD
    definition_period = YEAR
    documentation = (
        "Amount of Supplemental Nutrition Assistance Program benefits the "
        "household reports receiving. API partner input; programs only "
        "count this amount when use_reported_snap is True, and the "
        "calculated snap variable is never affected. See applicable_snap."
    )
