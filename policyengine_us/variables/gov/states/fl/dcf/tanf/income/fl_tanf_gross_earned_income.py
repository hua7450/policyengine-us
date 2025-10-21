from policyengine_us.model_api import *


class fl_tanf_gross_earned_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Florida TANF gross earned income"
    unit = USD
    definition_period = MONTH
    reference = "Florida Administrative Code Rule 65A-4.209"
    documentation = "Gross earned income for Florida TANF, excluding certain student earnings and WIOA income."
    defined_for = StateCode.FL

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.fl.dcf.tanf.age_thresholds

        person = spm_unit.members

        # Get individual earned income
        earned_income = person("employment_income", period)

        # Exclusions for students
        age = person("age", period)
        is_student = person("is_full_time_student", period)

        # Exclude earnings of full-time students under student_max_age in high school
        is_excluded_student = is_student & (age < p.student_max_age)

        # Apply exclusions
        countable_earned = where(is_excluded_student, 0, earned_income)

        return spm_unit.sum(countable_earned)
