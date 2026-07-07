from policyengine_us.model_api import *


class tanf_reported(Variable):
    value_type = float
    entity = SPMUnit
    label = "TANF (reported)"
    unit = USD
    definition_period = YEAR
    documentation = (
        "Reported amount of Temporary Assistance for Needy Families benefits received."
    )
