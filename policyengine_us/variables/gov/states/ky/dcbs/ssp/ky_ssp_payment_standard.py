from policyengine_us.model_api import *


class ky_ssp_payment_standard(Variable):
    value_type = float
    entity = Person
    label = "Kentucky SSP payment standard"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KY
    reference = (
        "https://apps.legislature.ky.gov/law/kar/titles/921/002/015/",
        "https://www.chfs.ky.gov/agencies/dcbs/dfs/Documents/OMVOLV.pdf#page=5",
    )

    def formula(person, period, parameters):
        category = person.household("ky_ssp_category", period)
        claim_type = person("ky_ssp_claim_type", period)
        care_receivers = person.household("ky_ssp_care_receivers", period)
        p = parameters(period).gov.states.ky.dcbs.ssp.payment_standard
        monthly_amount = p[category][claim_type][care_receivers]
        # Couples claiming jointly split the couple rate 50/50 across spouses.
        monthly_amount = where(
            claim_type == claim_type.possible_values.COUPLE_BOTH_ELIGIBLE,
            monthly_amount / 2,
            monthly_amount,
        )
        return monthly_amount * MONTHS_IN_YEAR
