from policyengine_us.model_api import *


class state_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "State taxable income (legacy compatibility umbrella)"
    documentation = (
        "Deprecated legacy umbrella for downstream compatibility. "
        "This is not a canonical cross-state PolicyEngine US concept; "
        "prefer state-specific taxable-income variables."
    )
    unit = USD
    definition_period = YEAR
    adds = "gov.states.household.state_taxable_incomes"
