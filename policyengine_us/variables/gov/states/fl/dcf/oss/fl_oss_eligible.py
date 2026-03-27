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
        categorically_eligible = person("is_ssi_eligible", period)
        facility_type = person.household("fl_oss_facility_type", period)
        in_facility = facility_type != facility_type.possible_values.NONE
        program_track = person.household("fl_oss_program_track", period)
        has_track = program_track != program_track.possible_values.NONE
        # Coverage Group 1: SSI recipients
        receives_ssi = person("uncapped_ssi", period) > 0
        # Coverage Group 2: non-SSI recipients within income standard
        income_standard = person("fl_oss_income_standard", period)
        countable_income = person("ssi_countable_income", period)
        income_within_standard = countable_income <= income_standard
        income_eligible = receives_ssi | income_within_standard
        return categorically_eligible & in_facility & has_track & income_eligible
