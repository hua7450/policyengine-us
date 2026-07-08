from policyengine_us.model_api import *


class use_reported_ssi(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    default_value = False
    label = "Use reported SSI in program income tests"
    documentation = (
        "When True, programs that count applicable_ssi follow the "
        "partner-reported information instead of calculated ssi: the "
        "receives_ssi flag decides participation, and a positive "
        "reported_ssi_amount (or the calculated ssi when no amount is "
        "provided) supplies the dollar value. This lets API partners "
        "show federal SSI entitlement and program eligibility in a "
        "single response."
    )
