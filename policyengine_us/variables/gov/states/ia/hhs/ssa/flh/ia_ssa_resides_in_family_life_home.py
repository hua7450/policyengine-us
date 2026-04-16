from policyengine_us.model_api import *


class ia_ssa_resides_in_family_life_home(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA resides in certified family-life home"
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.52.pdf#page=1"
    )
