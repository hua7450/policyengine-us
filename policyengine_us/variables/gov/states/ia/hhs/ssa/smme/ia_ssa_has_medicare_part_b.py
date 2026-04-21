from policyengine_us.model_api import *


class ia_ssa_has_medicare_part_b(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA eligible for Medicare Part B"
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.51.pdf#page=2"
    )

    def formula(person, period, parameters):
        return person("medicare_enrolled", period.this_year)
