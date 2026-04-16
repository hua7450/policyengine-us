from policyengine_us.model_api import *


class ia_ssa_smme_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA SMME eligible"
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.52.pdf#page=2",
        "https://www.legis.iowa.gov/docs/code/249.3.pdf",
    )

    def formula(person, period, parameters):
        aged_or_disabled = person("is_ssi_aged_blind_disabled", period.this_year)
        has_medicaid = person("ia_ssa_has_full_medicaid", period)
        has_medicare = person("ia_ssa_has_medicare_part_b", period)
        return aged_or_disabled & has_medicaid & has_medicare
