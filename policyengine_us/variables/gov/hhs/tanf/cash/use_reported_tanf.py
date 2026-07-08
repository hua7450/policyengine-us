from policyengine_us.model_api import *


class use_reported_tanf(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = YEAR
    default_value = False
    label = "Use reported TANF in program income tests"
    documentation = (
        "API partner opt-in toggle for reported TANF. When False (the "
        "default, including all microsimulation runs), applicable_tanf "
        "equals the calculated tanf and tanf_enrolled reflects whether "
        "it is positive. When True, the is_tanf_enrolled flag decides "
        "participation: tanf_enrolled follows it directly, and "
        "applicable_tanf is zero without it — with it, applicable_tanf "
        "counts a positive reported_tanf_amount if provided, the "
        "calculated tanf amount otherwise."
    )
