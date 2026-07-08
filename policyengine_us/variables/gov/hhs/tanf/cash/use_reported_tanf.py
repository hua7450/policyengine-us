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
        "it is positive. When True, both follow the partner-reported "
        "information instead: applicable_tanf counts "
        "reported_tanf_amount when one is provided, the calculated "
        "tanf when the household is flagged as enrolled via "
        "is_tanf_enrolled, and zero when neither is provided; "
        "tanf_enrolled is True when a positive reported_tanf_amount or "
        "the is_tanf_enrolled flag is provided."
    )
