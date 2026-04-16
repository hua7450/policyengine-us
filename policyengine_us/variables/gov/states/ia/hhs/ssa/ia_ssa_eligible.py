from policyengine_us.model_api import *


class ia_ssa_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA eligible"
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/code/249.3.pdf",
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.51.pdf",
    )

    def formula(person, period, parameters):
        categorically_eligible = person("is_ssi_eligible", period.this_year)
        resources_eligible = person("ia_ssa_resources_eligible", period)
        return categorically_eligible & resources_eligible
