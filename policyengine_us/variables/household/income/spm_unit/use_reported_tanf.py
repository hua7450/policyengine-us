from policyengine_us.model_api import *


class use_reported_tanf(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = YEAR
    default_value = False
    label = "Use reported TANF in program income tests"
    documentation = (
        "When True, programs that count applicable_tanf use tanf_reported "
        "if provided, calculated tanf if is_tanf_enrolled is True, and "
        "zero otherwise. This lets API partners report actual TANF "
        "receipt without overriding the calculated tanf amount."
    )
