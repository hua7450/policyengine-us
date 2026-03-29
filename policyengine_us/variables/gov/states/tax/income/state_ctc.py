from policyengine_us.model_api import *


class state_ctc(Variable):
    value_type = float
    entity = TaxUnit
    label = "State child tax credit (legacy compatibility umbrella)"
    documentation = (
        "Deprecated legacy umbrella for downstream compatibility. "
        "Prefer state-specific child tax credit variables."
    )
    unit = USD
    definition_period = YEAR
    adds = "gov.states.household.state_ctcs"
