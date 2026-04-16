from policyengine_us.model_api import *


class ia_ssa_flh_supplement(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA family-life home supplement"
    unit = USD
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.52.pdf#page=1"
    )

    def formula(person, period, parameters):
        category = person("ia_ssa_category", period)
        in_category = category == category.possible_values.FLH
        p = parameters(period).gov.states.ia.hhs.ssa
        uncapped_ssi = person("uncapped_ssi", period)
        income_excess = max_(0, -uncapped_ssi)
        federal_ssi = person("ssi", period)
        raw_supplement = max_(
            0, p.flh.assistance_standard - income_excess - federal_ssi
        )
        capped_supplement = min_(raw_supplement, p.flh.max_supplement)
        return in_category * capped_supplement
