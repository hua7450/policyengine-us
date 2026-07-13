from policyengine_us.model_api import *


class sd_cca_parent_in_eligible_activity(Variable):
    value_type = bool
    entity = Person
    label = "South Dakota CCA parent in an eligible activity"
    definition_period = MONTH
    defined_for = StateCode.SD
    reference = "https://dss.sd.gov/docs/childcare/assistance/Subsidy_Manual.pdf#page=8"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.sd.dss.cca.work_requirement
        min_wage = parameters(period).gov.dol.minimum_wage
        weekly_hours = person("weekly_hours_worked", period.this_year)
        weeks_per_month = WEEKS_IN_YEAR / MONTHS_IN_YEAR
        monthly_hours = weekly_hours * weeks_per_month
        # An employed caretaker must work at least 80 hours per month at a
        # salary equivalent to the federal minimum wage (Manual Sections 3
        # and 5).
        employment_income = person("employment_income", period)
        meets_employment_requirement = (monthly_hours >= p.monthly_hours) & (
            employment_income >= monthly_hours * min_wage
        )
        # A self-employed caretaker must work at least 20 hours per week and
        # receive weekly earnings of at least the federal minimum wage times
        # that hour minimum; a business loss counts as zero earnings (Manual
        # Section 6).
        weekly_self_employment_income = (
            person("self_employment_income", period) / weeks_per_month
        )
        meets_self_employment_requirement = (
            weekly_hours >= p.self_employed_weekly_hours
        ) & (weekly_self_employment_income >= p.self_employed_weekly_hours * min_wage)
        # Full-time students meet the 12-semester-credit-hour minimum; the
        # combined 80-hour work-plus-school path is not separately modeled.
        is_student = person("is_full_time_student", period.this_year)
        is_tanf_enrolled = person.spm_unit("is_tanf_enrolled", period)
        return (
            meets_employment_requirement
            | meets_self_employment_requirement
            | is_student
            | is_tanf_enrolled
        )
