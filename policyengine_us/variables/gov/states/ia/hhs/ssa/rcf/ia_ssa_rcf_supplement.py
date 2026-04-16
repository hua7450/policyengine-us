from policyengine_us.model_api import *


class ia_ssa_rcf_supplement(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA residential care facility supplement"
    unit = USD
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.52.pdf#page=1"
    )

    def formula(person, period, parameters):
        category = person("ia_ssa_category", period)
        in_category = category == category.possible_values.RCF
        p = parameters(period).gov.states.ia.hhs.ssa
        cost_per_diem = person("ia_ssa_rcf_cost_per_diem", period)
        capped_per_diem = min_(cost_per_diem, p.rcf.max_per_diem)
        cost_of_care = capped_per_diem * p.rcf.days_multiplier
        uncapped_ssi = person("uncapped_ssi", period)
        income_after_ssi_disregards = max_(0, -uncapped_ssi)
        federal_ssi = person("ssi", period)
        total_rcf_income = income_after_ssi_disregards + federal_ssi
        client_participation = max_(
            0, total_rcf_income - p.rcf.personal_needs_allowance
        )
        return in_category * max_(0, cost_of_care - client_participation)
