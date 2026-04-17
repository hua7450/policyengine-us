from policyengine_us.model_api import *


class ia_ssa_ihhrc_supplement(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA in-home health-related care supplement"
    unit = USD
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.177.pdf#page=2"
    )

    def formula(person, period, parameters):
        category = person("ia_ssa_category", period)
        in_category = category == category.possible_values.IHHRC
        p = parameters(period).gov.states.ia.hhs.ssa
        cost = person("ia_ssa_ihhrc_cost_of_care", period)
        both_need_care = person("ia_ssa_ihhrc_both_need_care", period)
        max_cost = where(
            both_need_care,
            p.ihhrc.max_cost_couple,
            p.ihhrc.max_cost_single,
        )
        return in_category * min_(cost, max_cost)
