from policyengine_us.model_api import *


class ak_ssp(Variable):
    value_type = float
    entity = Person
    label = "Alaska Adult Public Assistance"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.AK
    exhaustive_parameter_dependencies = "gov.states.ak.dpa.ssp"
    reference = (
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ak.pdf#page=1",
        "https://www.akleg.gov/basis/statutes.asp#47.25.430",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ak.dpa.ssp
        # uncapped_ssi can be negative when countable income exceeds the
        # federal SSI benefit. The negative portion reduces the state supplement.
        uncapped_ssi = person("uncapped_ssi", period)
        payment_standard = person("ak_ssp_payment_standard", period)
        income_excess = max_(0, -uncapped_ssi)
        normal_supplement = max_(0, payment_standard - income_excess)

        # Pre-2020: separate need standard creates a $1/month minimum zone.
        if p.separate_need_standard_in_effect:
            living_arrangement = person.household("ak_ssp_living_arrangement", period)
            claim_type = person("ak_ssp_claim_type", period)
            annual_need_std = (
                p.need_standard[living_arrangement][claim_type] * MONTHS_IN_YEAR
            )
            countable_income = person("ssi_countable_income", period)
            exceeds_need = countable_income >= annual_need_std
            annual_min_benefit = p.min_benefit * MONTHS_IN_YEAR
            in_minimum_zone = (normal_supplement <= 0) & ~exceeds_need
            state_supplement = select(
                [exceeds_need, in_minimum_zone],
                [0, annual_min_benefit],
                default=normal_supplement,
            )
        else:
            state_supplement = normal_supplement

        state_supplement = state_supplement * person("ak_ssp_eligible", period)
        return where(
            person("ssi_claim_is_joint", period),
            person.marital_unit.sum(state_supplement) / 2,
            state_supplement,
        )
