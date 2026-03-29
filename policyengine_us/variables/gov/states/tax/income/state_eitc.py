from policyengine_us.model_api import *


class state_eitc(Variable):
    value_type = float
    entity = TaxUnit
    label = "State earned income tax credit (legacy compatibility umbrella)"
    documentation = (
        "Deprecated legacy umbrella for downstream compatibility. "
        "Prefer state-specific EITC variables."
    )
    unit = USD
    definition_period = YEAR
    adds = "gov.states.household.state_eitcs"
