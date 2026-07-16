from policyengine_us.model_api import *


class ut_ccap_activity_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Utah CCAP activity eligible"
    definition_period = MONTH
    defined_for = StateCode.UT
    reference = "https://utrules.elaws.us/uac/r986-700-709"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ut.dwf.ccap.eligibility
        person = spm_unit.members
        is_parent = person("is_tax_unit_head_or_spouse", period.this_year)
        # weekly_hours_worked_before_lsr avoids the labor-supply feedback loop
        # that weekly_hours_worked (before_lsr + behavioral response) creates
        # in reform runs.
        hours = person("weekly_hours_worked_before_lsr", period.this_year)
        parent_count = spm_unit.sum(is_parent)
        lowest_parent_hours = spm_unit.min(where(is_parent, hours, np.inf))
        highest_parent_hours = spm_unit.max(where(is_parent, hours, 0))
        # A single parent must be employed an average of at least 15 hours
        # per week (R986-700-709(2)); in a two-parent household, one parent
        # must average at least 30 hours per week and the other at least 15
        # (R986-700-709(3)(a)). The requirement that earnings equal at least
        # the minimum wage for the hours worked (R986-700-709) is not
        # modeled.
        single_parent_eligible = highest_parent_hours >= p.single_parent_min_hours
        two_parent_eligible = (
            highest_parent_hours >= p.two_parent_second_min_hours
        ) & (lowest_parent_hours >= p.two_parent_first_min_hours)
        hours_eligible = select(
            [parent_count == 1, parent_count > 1],
            [single_parent_eligible, two_parent_eligible],
            default=False,
        )
        # Fall back to the CCDF activity-test input for approved activities
        # not individually modeled, such as the education and training
        # pathway (R986-700-711).
        meets_ccdf = spm_unit("meets_ccdf_activity_test", period.this_year)
        return hours_eligible | meets_ccdf
