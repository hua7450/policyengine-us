from policyengine_us.model_api import *


class sd_cca_parent_in_eligible_activity(Variable):
    value_type = bool
    entity = Person
    label = "South Dakota CCA parent in an eligible activity"
    definition_period = MONTH
    defined_for = StateCode.SD
    reference = (
        "https://dss.sd.gov/docs/childcare/assistance/Subsidy_Manual.pdf#page=12"
    )

    def formula(person, period, parameters):
        # Approved activities are employment, self-employment, and school or
        # training enrollment. A parent qualifies with positive wages, nonzero
        # self-employment income (a business loss still evidences active
        # self-employment), full-time student status, or enrollment in the
        # Temporary Assistance for Needy Families program. The exact hour and
        # credit thresholds are not modeled because activity hours are not
        # tracked.
        has_earnings = (person("employment_income", period) > 0) | (
            person("self_employment_income", period) != 0
        )
        is_student = person("is_full_time_student", period.this_year)
        is_tanf_enrolled = person.spm_unit("is_tanf_enrolled", period)
        return has_earnings | is_student | is_tanf_enrolled
