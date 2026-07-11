from policyengine_us.model_api import *


class or_erdc_activity_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Eligible for Oregon ERDC based on caretaker activity"
    defined_for = StateCode.OR
    reference = "https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=7871"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states["or"].delc.erdc
        categorical = spm_unit("or_erdc_categorically_eligible", period)
        person = spm_unit.members
        caretaker = person("is_tax_unit_head_or_spouse", period.this_year)
        caretaker_count = spm_unit.sum(caretaker)
        working = person("weekly_hours_worked_before_lsr", period.this_year) > 0
        postsecondary_student = person(
            "is_full_time_college_student", period.this_year
        ) | person("is_part_time_college_student", period.this_year)
        education_age_eligible = (
            person("age", period.this_year) <= p.age_threshold.education
        )
        secondary_student = (
            person("is_in_secondary_school", period.this_year)
            | person("or_erdc_in_ged_program", period.this_year)
        ) & education_age_eligible
        medical_leave = person("or_erdc_on_medical_leave", period.this_year)
        unable_to_care = person("or_erdc_unable_to_provide_care", period.this_year)
        supervised_contact = person(
            "or_erdc_supervised_contact_required", period.this_year
        )
        multiple_caretakers = spm_unit.project(caretaker_count > 1)
        caretaker_eligible = (
            working
            | postsecondary_student
            | secondary_student
            | medical_leave
            | (multiple_caretakers & (unable_to_care | supervised_contact))
        )
        has_caretaker = caretaker_count > 0
        all_caretakers_eligible = spm_unit.sum(caretaker & ~caretaker_eligible) == 0
        return categorical | (has_caretaker & all_caretakers_eligible)
