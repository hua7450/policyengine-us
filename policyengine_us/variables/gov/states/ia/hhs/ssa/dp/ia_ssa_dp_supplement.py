from policyengine_us.model_api import *


class ia_ssa_dp_supplement(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA dependent person supplement"
    unit = USD
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.52.pdf#page=1",
        "https://hhs.iowa.gov/assistance-programs/state-supplementary-assistance",
    )

    def formula(person, period, parameters):
        category = person("ia_ssa_category", period)
        in_category = category == category.possible_values.DP
        p = parameters(period).gov.states.ia.hhs.ssa
        configuration = person("ia_ssa_dp_configuration", period)
        payment_standard = p.dp.assistance_standard[configuration]
        uncapped_ssi = person("uncapped_ssi", period)
        income_excess = max_(0, -uncapped_ssi)
        federal_ssi = person("ssi", period)
        raw_supplement = max_(0, payment_standard - income_excess - federal_ssi)
        capped_supplement = min_(raw_supplement, p.dp.max_per_person_cap)
        dependent_income = person("ia_ssa_dp_dependent_countable_income", period)
        dependent_income_eligible = dependent_income < p.dp.dependent_income_limit
        return in_category * dependent_income_eligible * capped_supplement
