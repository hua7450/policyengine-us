from policyengine_us.model_api import *


class pa_ccw_activity_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Pennsylvania CCW based on activity requirements"
    definition_period = MONTH
    defined_for = StateCode.PA
    reference = "https://www.pacodeandbulletin.gov/secure/pacode/data/055/chapter3042/055_3042.pdf#page=15"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.pa.dhs.ccw.activity_requirements
        person = spm_unit.members
        is_head_or_spouse = person("is_tax_unit_head_or_spouse", period.this_year)
        hours_worked = person("weekly_hours_worked", period.this_year)
        meets_work_requirement = hours_worked >= p.weekly_hours
        age = person("age", period.this_year)
        is_teen_parent_student = person("is_full_time_student", period.this_year) & (
            age < p.teen_parent_max_age
        )
        meets_training_combo = hours_worked >= p.training_combo_min_work_hours
        individually_eligible = (
            meets_work_requirement | is_teen_parent_student | meets_training_combo
        )
        return spm_unit.sum(is_head_or_spouse & ~individually_eligible) == 0
