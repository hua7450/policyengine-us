from policyengine_us.model_api import *


class ia_ssa_has_full_medicaid(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA receives full Medicaid"
    documentation = "Whether the person receives full Medicaid without a spend down or premium, as required for Iowa SSA SMME category (IAC 441—51.7(1)). Defaults to federal medicaid_enrolled, which does not distinguish full vs partial coverage; override for spend-down recipients."
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.51.pdf#page=2"
    )

    def formula(person, period, parameters):
        return person("medicaid_enrolled", period.this_year)
