from policyengine_us.model_api import *


class ia_ssa_ihhrc_cost_of_care(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA in-home health-related care monthly cost"
    unit = USD
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.177.pdf#page=2"
    )
