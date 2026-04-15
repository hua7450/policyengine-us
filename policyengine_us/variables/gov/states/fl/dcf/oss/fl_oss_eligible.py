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
        # Community care requires a valid program track
        program_track = person("fl_oss_program_track", period)
        has_track = program_track != program_track.possible_values.NONE
        is_protected = program_track == program_track.possible_values.PROTECTED
        track_valid = where(is_protected, p.protected.in_effect, has_track)
        # Medicaid facility has no track requirement
        track_ok = where(in_medicaid_facility, True, track_valid)
        # FAC 65A-2.033(1): "receiving SSI checks"
        receives_ssi = person("ssi", period) > 0
        # FAC 65A-2.033(2): meets all criteria except income ≤ income standard
        income_standard = person("fl_oss_income_standard", period)
        countable_income = person("ssi_countable_income", period)
        income_within_standard = countable_income <= income_standard
        income_eligible = receives_ssi | income_within_standard
        return categorically_eligible & in_facility & track_ok & income_eligible
