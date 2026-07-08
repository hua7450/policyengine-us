from policyengine_us.model_api import *


class receives_tanf(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Receives TANF"
    documentation = (
        "Whether the family currently receives Temporary Assistance for "
        "Needy Families benefits. Reported input, named consistently "
        "with receives_snap; state TANF programs also use it to "
        "distinguish existing recipients from new applicants."
    )
