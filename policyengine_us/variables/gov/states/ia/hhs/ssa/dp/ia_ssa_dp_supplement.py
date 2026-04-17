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
        # Iowa DP is federally-administered per POMS SI 01415.050.F. For
        # federally-administered SSP, the state supplement equals
        # max(0, total_standard − max(countable_income, FBR)): it stays at
        # the full state amount while income is below the FBR and then phases
        # down dollar-for-dollar as income rises above the FBR.
        countable_monthly = (
            person("ssi_countable_income", period.this_year) / MONTHS_IN_YEAR
        )
        fbr = parameters(period).gov.ssa.ssi.amount.individual
        raw_supplement = max_(0, payment_standard - max_(countable_monthly, fbr))
        capped_supplement = min_(raw_supplement, p.dp.max_per_person_cap)
        dependent_income = person("ia_ssa_dp_dependent_countable_income", period)
        dependent_income_eligible = dependent_income < p.dp.dependent_income_limit
        return in_category * dependent_income_eligible * capped_supplement
