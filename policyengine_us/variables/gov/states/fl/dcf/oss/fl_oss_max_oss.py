from policyengine_us.model_api import *


class fl_oss_max_oss(Variable):
    value_type = float
    entity = Person
    label = "Florida OSS maximum payment"
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.FL
    reference = "https://www.myflfamilies.com/sites/default/files/2024-10/Appendix%20A-12%20OSS%20Payment%20Standards.pdf"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.fl.dcf.oss
        track = person.household("fl_oss_program_track", period)
        is_redesign = track == track.possible_values.REDESIGN
        joint_claim = person("ssi_claim_is_joint", period)
        # Select the max OSS cap by track and couple status.
        # Couple caps are total for both spouses; divide by 2
        # for per-person amount.
        individual_cap = where(
            is_redesign,
            p.redesign.max_oss.individual,
            p.protected.max_oss.individual,
        )
        couple_cap = where(
            is_redesign,
            p.redesign.max_oss.couple,
            p.protected.max_oss.couple,
        )
        return where(joint_claim, couple_cap / 2, individual_cap)
