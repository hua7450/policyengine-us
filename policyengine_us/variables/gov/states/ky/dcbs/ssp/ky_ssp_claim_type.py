from policyengine_us.model_api import *


class KYSSPClaimType(Enum):
    INDIVIDUAL = "Individual"
    COUPLE_BOTH_ELIGIBLE = "Couple, both eligible"
    COUPLE_ONE_ELIGIBLE = "Couple, one eligible with ineligible spouse"


class ky_ssp_claim_type(Variable):
    value_type = Enum
    entity = Person
    label = "Kentucky SSP claim type"
    definition_period = YEAR
    defined_for = StateCode.KY
    possible_values = KYSSPClaimType
    default_value = KYSSPClaimType.INDIVIDUAL
    reference = (
        "https://apps.legislature.ky.gov/law/kar/titles/921/002/015/",
        "https://www.chfs.ky.gov/agencies/dcbs/dfs/Documents/OMVOLV.pdf#page=43",
    )

    def formula(person, period, parameters):
        joint_claim = person("ssi_claim_is_joint", period)
        marital_unit_size = person.marital_unit.sum(person("age", period) >= 0)
        is_eligible_individual = person("is_ssi_aged_blind_disabled", period)
        one_eligible_couple = (
            ~joint_claim & is_eligible_individual & (marital_unit_size == 2)
        )
        return select(
            [joint_claim, one_eligible_couple],
            [
                KYSSPClaimType.COUPLE_BOTH_ELIGIBLE,
                KYSSPClaimType.COUPLE_ONE_ELIGIBLE,
            ],
            default=KYSSPClaimType.INDIVIDUAL,
        )
