from policyengine_us.model_api import *


class ak_ssp_payment_standard(Variable):
    value_type = float
    entity = Person
    label = "Alaska Adult Public Assistance payment standard"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.AK
    reference = (
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ak.pdf#page=2"
    )

    def formula(person, period, parameters):
        living_arrangement = person.household("ak_ssp_living_arrangement", period)
        claim_type = person("ak_ssp_claim_type", period)
        p = parameters(period).gov.states.ak.dpa.ssp.payment_standard
        monthly_amount = p[living_arrangement][claim_type]
        return monthly_amount * MONTHS_IN_YEAR
