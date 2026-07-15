from policyengine_us.model_api import *


class snap(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    documentation = (
        "Final SNAP benefit amount, equal to net income minus food contribution"
    )
    label = "SNAP allotment"
    reference = "https://www.law.cornell.edu/uscode/text/7/2017#a"
    unit = USD
    exhaustive_parameter_dependencies = [
        "gov.usda.snap",
        "gov.ssa",
    ]

    def formula(spm_unit, period, parameters):
        takes_up = spm_unit("takes_up_snap_if_eligible", period.this_year)
        return spm_unit("snap_if_takes_up", period) * takes_up
