from policyengine_us.model_api import *


class ia_ssa_has_full_medicaid(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA receives full Medicaid"
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.51.pdf#page=2"
    )

    def formula(person, period, parameters):
        return person("medicaid_enrolled", period.this_year)
