from policyengine_us.model_api import *


class ok_ccs_activity_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Oklahoma Child Care Subsidy activity eligible"
    definition_period = MONTH
    defined_for = StateCode.OK
    reference = "https://okrules.elaws.us/oac/340:40-7-8"

    def formula(spm_unit, period, parameters):
        # The need factor requires each parent or caretaker to be employed or
        # attending an education or training program (OAC 340:40-7-8). A
        # parent qualifies with positive wages, nonzero self-employment income
        # (a business loss still evidences active self-employment), or
        # full-time student status. The minimum wage requirement on employment
        # is not modeled.
        person = spm_unit.members
        is_head_or_spouse = person("is_tax_unit_head_or_spouse", period.this_year)
        has_earnings = (person("employment_income", period) > 0) | (
            person("self_employment_income", period) != 0
        )
        is_student = person("is_full_time_student", period.this_year)
        in_activity = has_earnings | is_student
        has_head_or_spouse = spm_unit.sum(is_head_or_spouse) >= 1
        all_covered = spm_unit.sum(is_head_or_spouse & ~in_activity) == 0
        modeled_eligible = has_head_or_spouse & all_covered
        # TANF Work activities under a TANF Work/Personal Responsibility
        # Agreement establish the need factor for TANF recipients.
        is_tanf_enrolled = spm_unit("is_tanf_enrolled", period)
        # Protective or preventive child care covers families experiencing
        # homelessness, medical hardship, or natural disasters; the 30-day
        # initial approval limit is not tracked at the moment.
        protective = (
            add(
                spm_unit,
                period.this_year,
                ["receives_or_needs_protective_services"],
            )
            > 0
        )
        # Fall back to the CCDF activity-test input for approved activities not
        # individually modeled (SNAP E&T assigned activities and the
        # enrichment pathway for children receiving SSI; OAC 340:40-7-8).
        meets_ccdf = spm_unit("meets_ccdf_activity_test", period.this_year)
        return modeled_eligible | is_tanf_enrolled | protective | meets_ccdf
