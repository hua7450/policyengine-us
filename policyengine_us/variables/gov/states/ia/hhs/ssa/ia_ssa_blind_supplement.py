from policyengine_us.model_api import *


class ia_ssa_blind_supplement(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA blind supplement"
    documentation = "Iowa SSA blind supplement. Per IAC 441—52.1(4), a blind recipient receives this supplement only if they are not receiving another type of state supplementary assistance; this is enforced via ia_ssa_category returning BLIND only when no higher-priority category applies."
    unit = USD
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.52.pdf#page=2"
    )

    def formula(person, period, parameters):
        category = person("ia_ssa_category", period)
        in_category = category == category.possible_values.BLIND
        p = parameters(period).gov.states.ia.hhs.ssa
        return in_category * p.blind
