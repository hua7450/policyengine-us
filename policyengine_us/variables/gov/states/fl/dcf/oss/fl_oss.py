from policyengine_us.model_api import *


class fl_oss(Variable):
    value_type = float
    entity = Person
    label = "Florida Optional State Supplementation"
    unit = USD
    definition_period = MONTH
    defined_for = "fl_oss_eligible"
    reference = (
        "https://www.flrules.org/gateway/RuleNo.asp?title=PUBLIC%20ASSISTANCE&ID=65A-2.036",
        "https://www.myflfamilies.com/sites/default/files/2024-10/Appendix%20A-12%20OSS%20Payment%20Standards.pdf",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.fl.dcf.oss
        living_arrangement = person("fl_oss_living_arrangement", period)
        LA = living_arrangement.possible_values
        in_medicaid_facility = living_arrangement == LA.MEDICAID_FACILITY
        # Medicaid facility: flat state supplement
        joint_claim = person("ssi_claim_is_joint", period)
        medicaid_supplement = where(
            joint_claim,
            p.medicaid_facility.supplement.couple / 2,
            p.medicaid_facility.supplement.individual,
        )
        # Community care: provider rate + PNA - income, capped at max OSS
        provider_rate = person("fl_oss_provider_rate", period)
        total_needs = provider_rate + p.pna
        countable_income = person("ssi_countable_income", period)
        max_oss = person("fl_oss_max_oss", period)
        community_benefit = min_(max_(total_needs - countable_income, 0), max_oss)
        return where(in_medicaid_facility, medicaid_supplement, community_benefit)
