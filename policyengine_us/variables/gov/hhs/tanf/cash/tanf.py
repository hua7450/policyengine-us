from policyengine_us.model_api import *


class tanf(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = YEAR
    label = "TANF"
    documentation = (
        "Value of Temporary Assistance for Needy Families benefit received, "
        "summing all state-specific TANF programs."
    )
    unit = USD

    def formula(spm_unit, period, parameters):
        takes_up = spm_unit("takes_up_tanf_if_eligible", period)
        return spm_unit("tanf_if_takes_up", period) * takes_up
