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
        # IAC 441—177.10(2)(a): payment equals cost of care (capped per person
        # at the single cap from 441—177.10(3)) minus client participation,
        # where client participation is countable income after the basic SSI
        # standard disregard (the applicable FBR for a single or joint claim).
        # Compute participation at the marital-unit level and split evenly
        # across members so the aggregated SPM-unit total is correct without
        # double-counting.
        countable_monthly = (
            person("ssi_countable_income", period.this_year) / MONTHS_IN_YEAR
        )
        individual_fbr = parameters(period).gov.ssa.ssi.amount.individual
        couple_fbr = parameters(period).gov.ssa.ssi.amount.couple
        joint_claim = person("ssi_claim_is_joint", period.this_year)
        disregard = where(joint_claim, couple_fbr, individual_fbr)
        combined_countable = person.marital_unit.sum(countable_monthly)
        combined_participation = max_(0, combined_countable - disregard)
        # Split evenly across marital-unit members (1 person unmarried, 2 if
        # married) so the person-level values sum back to the combined total.
        client_participation = combined_participation / person.marital_unit.nb_persons()
        # IAC 441—177.10(3): maximum benefit payable is $480.55 per client,
        # inclusive of all services for all providers.
        eligible_cost = min_(cost, p.ihhrc.max_cost_single)
        return in_category * max_(0, eligible_cost - client_participation)
