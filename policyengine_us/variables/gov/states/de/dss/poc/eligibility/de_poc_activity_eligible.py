from policyengine_us.model_api import *


class de_poc_activity_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Delaware Purchase of Care based on activity requirements"
    definition_period = MONTH
    defined_for = StateCode.DE
    reference = "https://regulations.delaware.gov/AdminCode/title16/Department%20of%20Health%20and%20Social%20Services/Division%20of%20Social%20Services/11003.shtml"

    def formula(spm_unit, period, parameters):
        person = spm_unit.members
        is_head_or_spouse = person("is_tax_unit_head_or_spouse", period.this_year)
        has_employment = (person("employment_income", period) > 0) | (
            person("self_employment_income", period) > 0
        )
        is_student = person("is_full_time_student", period.this_year)
        individually_eligible = has_employment | is_student
        return spm_unit.any(is_head_or_spouse & individually_eligible)
