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
        # FAC 65A-2.033(1): "receiving SSI checks"
        receives_ssi = person("ssi", period) > 0
        # Medicaid facility: Group 1 only (no income standard defined
        # in FAC 65A-2.036 for Medicaid facility; the $30 medical
        # facility SSI rate is the only payment path).
        # Community care: Group 1 OR Group 2 (income ≤ income standard),
        # plus requires a valid program track.
        program_track = person("fl_oss_program_track", period)
        has_track = program_track != program_track.possible_values.NONE
        is_protected = program_track == program_track.possible_values.PROTECTED
        track_valid = where(is_protected, p.protected.in_effect, has_track)
        # FAC 65A-2.033(2): income ≤ OSS income standard
        income_standard = person("fl_oss_income_standard", period)
        countable_income = person("ssi_countable_income", period)
        income_within_standard = countable_income <= income_standard
        community_eligible = track_valid & (receives_ssi | income_within_standard)
        return (
            categorically_eligible
            & in_facility
            & where(in_medicaid_facility, receives_ssi, community_eligible)
        )
