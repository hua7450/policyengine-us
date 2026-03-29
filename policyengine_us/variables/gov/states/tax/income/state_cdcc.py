from policyengine_us.model_api import *


class state_cdcc(Variable):
    value_type = float
    entity = TaxUnit
    label = "State child and dependent care tax credit (legacy compatibility umbrella)"
    documentation = (
        "Deprecated legacy umbrella for downstream compatibility. "
        "Prefer state-specific child care credit variables."
    )
    unit = USD
    definition_period = YEAR
    adds = "gov.states.household.state_cdccs"
