from policyengine_us.model_api import *


class AKSSPClaimType(Enum):
    INDIVIDUAL = "Individual"
    COUPLE_BOTH_ELIGIBLE = "Couple, both eligible"
    COUPLE_ONE_ELIGIBLE = "Couple, one eligible with ineligible spouse"


class ak_ssp_claim_type(Variable):
    value_type = Enum
    entity = Person
    label = "Alaska Adult Public Assistance claim type"
    definition_period = YEAR
    defined_for = StateCode.AK
    possible_values = AKSSPClaimType
    default_value = AKSSPClaimType.INDIVIDUAL
    reference = (
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ak.pdf#page=2"
    )

    def formula(person, period, parameters):
        joint_claim = person("ssi_claim_is_joint", period)
        deeming_applies = person("is_ssi_spousal_deeming_applies", period)
        return select(
            [joint_claim, deeming_applies],
            [
                AKSSPClaimType.COUPLE_BOTH_ELIGIBLE,
                AKSSPClaimType.COUPLE_ONE_ELIGIBLE,
            ],
            default=AKSSPClaimType.INDIVIDUAL,
        )
