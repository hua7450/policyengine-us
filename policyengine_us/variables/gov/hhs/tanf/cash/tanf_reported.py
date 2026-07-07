from policyengine_us.model_api import *


class tanf_reported(Variable):
    value_type = float
    entity = SPMUnit
    label = "TANF (reported)"
    unit = USD
    definition_period = YEAR
    documentation = (
        "Amount of Temporary Assistance for Needy Families benefits the "
        "household reports receiving. Programs only count this amount "
        "when use_reported_tanf is True; see applicable_tanf."
    )
