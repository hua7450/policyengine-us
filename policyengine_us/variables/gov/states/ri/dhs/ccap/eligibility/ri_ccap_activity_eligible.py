from policyengine_us.model_api import *


class ri_ccap_activity_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Rhode Island CCAP based on activity requirements"
    definition_period = MONTH
    reference = "https://dhs.ri.gov/media/9236/download?language=en#page=33"
    defined_for = StateCode.RI

    def formula(spm_unit, period, parameters):
        person = spm_unit.members
        head_or_spouse = person("is_tax_unit_head_or_spouse", period.this_year)
        is_working = (
            add(
                person,
                period,
                ["employment_income", "self_employment_income"],
            )
            > 0
        )
        is_student = person("is_full_time_student", period.this_year)
        ineligible_parent = head_or_spouse & ~(is_working | is_student)
        return spm_unit.sum(ineligible_parent) == 0
