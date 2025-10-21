from policyengine_us.model_api import *


class fl_tanf_categorically_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Categorically eligible for Florida Temporary Cash Assistance"
    definition_period = MONTH
    reference = (
        "Florida Statute § 414.095; Florida Administrative Code Rule 65A-4.208"
    )
    documentation = "Families with children under 18 (or under 19 if full-time high school student) or pregnant women are categorically eligible."
    defined_for = StateCode.FL

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.fl.dcf.tanf.age_thresholds

        # Children under child_max_age or under student_max_age and in high school
        person = spm_unit.members
        age = person("age", period)
        is_student = person("is_full_time_student", period)

        is_qualifying_child = (age < p.child_max_age) | (
            (age < p.student_max_age) & is_student
        )
        has_qualifying_child = spm_unit.any(is_qualifying_child)

        # Pregnant women
        is_pregnant = person("is_pregnant", period)
        has_pregnant_member = spm_unit.any(is_pregnant)

        return has_qualifying_child | has_pregnant_member
