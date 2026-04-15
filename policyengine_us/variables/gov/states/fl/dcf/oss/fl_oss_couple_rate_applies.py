from policyengine_us.model_api import *


class fl_oss_couple_rate_applies(Variable):
    value_type = bool
    entity = Person
    label = "Florida OSS couple rate applies"
    definition_period = MONTH
    defined_for = StateCode.FL
    reference = "https://www.myflfamilies.com/sites/default/files/2025-05/Appendix%20A-12%20-%20State%20Funded%20Programs%20Eligibility%20Standards.pdf"

    def formula(person, period, parameters):
        # Requires: both spouses are an SSI eligible couple
        # (ssi_claim_is_joint handles Title XIX separation per
        # 20 CFR 416.1149 — see #8003), both pass SSI categorical
        # eligibility (resources + immigration), and both reside
        # in a qualifying OSS facility.
        joint_claim = person("ssi_claim_is_joint", period)
        both_ssi_eligible = (
            person.marital_unit.sum(person("is_ssi_eligible", period))
            == person.marital_unit.nb_persons()
        )
        living_arrangement = person("fl_oss_living_arrangement", period)
        in_facility = living_arrangement != living_arrangement.possible_values.NONE
        both_in_facility = (
            person.marital_unit.sum(in_facility) == person.marital_unit.nb_persons()
        )
        return joint_claim & both_ssi_eligible & both_in_facility
