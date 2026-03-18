from policyengine_us.model_api import *


class al_ssp(Variable):
    value_type = float
    entity = Person
    label = "Alabama State Supplementary Payment"
    unit = USD
    definition_period = MONTH
    defined_for = "al_ssp_eligible"
    reference = "https://admincode.legislature.state.al.us/api/chapter/660-2-4#page=24"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.al.dhr.ssp.amount
        living_arrangement = person("al_ssp_living_arrangement", period)
        la = living_arrangement.possible_values
        # Look up monthly amount by living arrangement.
        # Specialized IHC uses same amount as Level A.
        monthly_amount = select(
            [
                living_arrangement == la.IHC_LEVEL_A,
                living_arrangement == la.IHC_LEVEL_B,
                living_arrangement == la.FOSTER_CARE,
                living_arrangement == la.CEREBRAL_PALSY,
                living_arrangement == la.SPECIALIZED_IHC,
            ],
            [
                p.level_a,
                p.level_b,
                p.foster_care,
                p.cerebral_palsy,
                p.level_a,  # Specialized IHC = Level A amount
            ],
        )
        # Double for joint SSI claims (both spouses are ABD).
        joint_claim = person("ssi_claim_is_joint", period.this_year)
        return monthly_amount * (1 + joint_claim)
