from policyengine_us.model_api import *


class use_reported_snap(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = YEAR
    default_value = False
    label = "Use reported SNAP participation in program eligibility tests"
    documentation = (
        "When True, programs that check snap_enrolled use the reported "
        "receives_snap input instead of the calculated snap amount. This "
        "lets API partners pass through actual SNAP participation while "
        "still receiving the calculated snap entitlement as an output."
    )
