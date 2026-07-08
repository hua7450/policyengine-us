from policyengine_us.model_api import *


class use_reported_snap(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = YEAR
    default_value = False
    label = "Use reported SNAP in program eligibility and income tests"
    documentation = (
        "API partner opt-in toggle for reported SNAP. When True, programs "
        "that check snap_enrolled use the reported receives_snap input (or "
        "a positive reported_snap_amount) instead of the calculated snap "
        "amount, and programs that count SNAP benefits as income use "
        "applicable_snap. This lets API partners pass through actual SNAP "
        "participation while still receiving the calculated snap "
        "entitlement as an output."
    )
