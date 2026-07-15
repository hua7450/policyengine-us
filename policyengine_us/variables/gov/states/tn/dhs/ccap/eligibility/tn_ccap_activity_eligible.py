from policyengine_us.model_api import *


class tn_ccap_activity_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Tennessee CCAP based on activity requirements"
    definition_period = MONTH
    defined_for = StateCode.TN
    reference = "https://www.tn.gov/content/dam/tn/human-services/documents/CCDF%20State%20Plan%20FFY%202025-2027%20Tennessee.pdf#page=26"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.tn.dhs.ccap.activity
        person = spm_unit.members
        is_head_or_spouse = person("is_tax_unit_head_or_spouse", period.this_year)
        hours_worked = person("weekly_hours_worked_before_lsr", period.this_year)
        meets_work_requirement = hours_worked >= p.weekly_hours
        is_student = person("is_full_time_student", period.this_year)
        individually_eligible = meets_work_requirement | is_student
        # Both parents must meet an activity: employment averaging at least
        # 30 hours per week or full-time post-secondary education.
        n_parents = spm_unit.sum(is_head_or_spouse)
        n_qualifying = spm_unit.sum(is_head_or_spouse & individually_eligible)
        all_parents_qualify = (n_parents >= 1) & (n_qualifying >= n_parents)
        # Fallback for approved activities not individually modeled (job
        # search, training, temporary leave, protective-services referrals).
        fallback = spm_unit("meets_ccdf_activity_test", period.this_year)
        return all_parents_qualify | fallback
