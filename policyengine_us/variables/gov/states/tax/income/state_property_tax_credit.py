from policyengine_us.model_api import *


class state_property_tax_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "State property tax credit (legacy compatibility umbrella)"
    documentation = (
        "Deprecated legacy umbrella for downstream compatibility. "
        "Prefer state-specific property tax credit variables."
    )
    unit = USD
    definition_period = YEAR
    adds = "gov.states.household.state_property_tax_credits"
