from policyengine_us.model_api import *
from policyengine_us.variables.gov.ssa.ssi.eligibility.status.ssi_federal_living_arrangement import (
    SSIFederalLivingArrangement,
)


class ssi_amount_if_eligible(Variable):
    value_type = float
    entity = Person
    label = "SSI amount if eligible"
    unit = USD
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/uscode/text/42/1382#b"

    def formula(person, period, parameters):
        p = parameters(period).gov.ssa.ssi.amount
        arrangement = person("ssi_federal_living_arrangement", period)

        # Three scenarios for adults:
        # 1. Both spouses eligible (joint claim) → couple rate / 2
        # 2. One eligible, no deeming → individual rate
        # 3. One eligible, deeming applies → couple rate (capped in ssi)
        #
        # Note: In scenario 3, deeming applies when spouse's GROSS income > $483.
        # Income exclusions are applied to the COMBINED income afterwards.
        # This means countable income can be much lower than $483, and the
        # benefit can exceed individual FBR, requiring the cap in ssi.

        is_joint_claim = person("ssi_claim_is_joint", period)
        deeming_applies = person("is_ssi_spousal_deeming_applies", period)

        # Determine FBR to use based on scenario
        individual_or_deeming_amount = where(
            deeming_applies,
            p.couple,
            p.individual,
        )

        base_amount = where(
            is_joint_claim,
            p.couple / 2,
            individual_or_deeming_amount,
        )

        # Children (under 18) always receive individual FBR. A child never
        # files a joint claim with parents — joint claims are between
        # spouses only. Adults 18+ (including students) go through normal
        # couple/deeming logic since they may be married.
        base_amount = where(person("is_child", period), p.individual, base_amount)

        # Status B: Apply the one-third reduction (VTR) per 20 CFR § 416.1131.
        # The VTR applies to the applicable FBR (individual or couple based
        # on deeming), per POMS SI 00835.210.
        is_b = arrangement == SSIFederalLivingArrangement.B
        vtr_rate = p.one_third_reduction_rate
        base_amount = where(
            is_b,
            base_amount * (1 - vtr_rate),
            base_amount,
        )

        # Status D: Medical treatment facility, $30/month per person.
        # Per 20 CFR § 416.414: one spouse in facility gets $30;
        # the community spouse gets full individual FBR.
        is_d = arrangement == SSIFederalLivingArrangement.D
        base_amount = where(is_d, p.medical_facility, base_amount)

        return base_amount * MONTHS_IN_YEAR
