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
        # IAC 441—51.7(4) requires SMME recipients to be currently eligible for
        # Medicare Part B. PolicyEngine's medicare_enrolled does not distinguish
        # Part A from Part B, so this uses it as the closest proxy — accepting
        # that Part A-only enrollees are not filtered out. In practice, the
        # SMME target population is dual-eligibles whose Part B premiums are
        # paid by Medicaid, so enrollment in Medicare correlates strongly with
        # Part B enrollment.
        return person("medicare_enrolled", period.this_year)
