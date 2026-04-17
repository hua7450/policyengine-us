from policyengine_us.model_api import *


class ia_ssa_has_medicare_part_b(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA eligible for Medicare Part B"
    documentation = "Whether the person is enrolled in Medicare Part B, as required for Iowa SSA SMME category (IAC 441—51.7(4)). Defaults to federal medicare_enrolled, which covers Part A and/or B; override for Part-A-only recipients."
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.51.pdf#page=2"
    )

    def formula(person, period, parameters):
        return person("medicare_enrolled", period.this_year)
