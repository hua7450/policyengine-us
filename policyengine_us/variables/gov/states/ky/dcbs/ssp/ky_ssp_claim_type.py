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
        "https://www.chfs.ky.gov/agencies/dcbs/dfs/Documents/OMVOLV.pdf#page=41",
    )

    def formula(person, period, parameters):
        # 921 KAR 2:015 §9(1)(c) ties couple rates to "eligible couple, both
        # aged, blind, or having a disability" — i.e. both actually SSI-eligible
        # (ABD + resource test + immigration), not merely both ABD.
        is_eligible = person("is_ssi_eligible", period)
        eligible_count = person.marital_unit.sum(is_eligible)
        marital_unit_size = person.marital_unit.nb_persons()
        both_eligible = (eligible_count == 2) & is_eligible
        # §9(1)(c)1: eligible individual with an ineligible spouse in a
        # 2-person marital unit uses the individual standard.
        one_eligible_couple = (
            (eligible_count == 1) & is_eligible & (marital_unit_size == 2)
        )
        return select(
            [both_eligible, one_eligible_couple],
            [
                KYSSPClaimType.COUPLE_BOTH_ELIGIBLE,
                KYSSPClaimType.COUPLE_ONE_ELIGIBLE,
            ],
            default=KYSSPClaimType.INDIVIDUAL,
        )
