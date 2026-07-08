from policyengine_us.model_api import *


class reported_tanf_amount(Variable):
    value_type = float
    entity = SPMUnit
    label = "Reported TANF amount"
    unit = USD
    definition_period = YEAR
    documentation = (
        "Amount of Temporary Assistance for Needy Families benefits the "
        "household reports receiving. API partner input; programs only "
        "count this amount when use_reported_tanf is True and "
        "is_tanf_enrolled marks the unit as enrolled, and the "
        "calculated tanf variable is never affected. See applicable_tanf."
    )
