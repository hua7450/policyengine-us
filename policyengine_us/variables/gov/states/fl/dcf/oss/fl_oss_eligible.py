from policyengine_us.model_api import *


class fl_oss_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Florida OSS eligible"
    definition_period = MONTH
    defined_for = StateCode.FL
    reference = (
        "https://www.flrules.org/gateway/RuleNo.asp?title=PUBLIC%20ASSISTANCE&ID=65A-2.032",
        "https://www.flrules.org/gateway/RuleNo.asp?title=PUBLIC%20ASSISTANCE&ID=65A-2.033",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.fl.dcf.oss
        categorically_eligible = person("is_ssi_eligible", period)
        living_arrangement = person("fl_oss_living_arrangement", period)
        LA = living_arrangement.possible_values
        in_facility = living_arrangement != LA.NONE
        in_medicaid_facility = living_arrangement == LA.MEDICAID_FACILITY
        # Medicaid facility: only requires SSI eligibility + facility
        # Community care: also requires valid program track + income check
        program_track = person("fl_oss_program_track", period)
        has_track = program_track != program_track.possible_values.NONE
        is_protected = program_track == program_track.possible_values.PROTECTED
        track_valid = where(is_protected, p.protected.in_effect, has_track)
        # Coverage Group 1: SSI recipients
        receives_ssi = person("uncapped_ssi", period) > 0
        # Coverage Group 2: non-SSI recipients within income standard
        income_standard = person("fl_oss_income_standard", period)
        countable_income = person("ssi_countable_income", period)
        income_within_standard = countable_income <= income_standard
        income_eligible = receives_ssi | income_within_standard
        community_eligible = track_valid & income_eligible
        return (
            categorically_eligible
            & in_facility
            & where(in_medicaid_facility, receives_ssi, community_eligible)
        )
