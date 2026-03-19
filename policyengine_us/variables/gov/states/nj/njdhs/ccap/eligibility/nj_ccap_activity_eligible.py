from policyengine_us.model_api import *


class nj_ccap_activity_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for New Jersey CCAP based on activity requirements"
    definition_period = MONTH
    defined_for = StateCode.NJ
    reference = (
        "https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-10-15-5-2",
        "https://www.childcarenj.gov/ChildCareNJ/media/media_library/CCDF_State_Plan_for_New_Jersey_FFY25-27.pdf#page=14",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.nj.njdhs.ccap.activity_requirements
        person = spm_unit.members
        is_head_or_spouse = person("is_tax_unit_head_or_spouse", period.this_year)
        hours_worked = person("weekly_hours_worked", period.this_year)
        meets_work_requirement = hours_worked >= p.weekly_hours
        is_student = person("is_full_time_student", period.this_year)
        individually_eligible = meets_work_requirement | is_student
        return spm_unit.sum(is_head_or_spouse & ~individually_eligible) == 0
