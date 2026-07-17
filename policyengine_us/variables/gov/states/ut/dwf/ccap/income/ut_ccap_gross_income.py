from policyengine_us.model_api import *


class ut_ccap_gross_income(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Utah CCAP gross countable income"
    definition_period = MONTH
    defined_for = StateCode.UT
    reference = (
        "https://www.law.cornell.edu/regulations/utah/Utah-Admin-Code-R986-700-710"
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ut.dwf.ccap.income
        person = spm_unit.members
        # Only the income of the eligible child's parent(s) is counted,
        # regardless of who else lives in the household; if both parents
        # live in the household, both parents' income is counted
        # (R986-700-710(4)(a)). is_parent (own children in the household)
        # rather than a tax-unit role flag identifies parents across
        # tax-unit boundaries and keeps a minor parent's earnings countable.
        # The earned income of a child who is not a parent is not counted
        # (R986-700-710(4)(f)), while a child's unearned income, such as
        # child support paid on the child's behalf, remains countable
        # (R986-700-710(4)(d)(i)); is_child matches Utah Code 15-2-1, which
        # sets the period of minority at ages below 18. A non-parent
        # caretaker client, such as a specified relative caring for a child
        # whose parents are absent (R986-700-710(4)(b)), has
        # is_parent == False, so their income is not captured; this is a
        # known limitation.
        is_parent = person("is_parent", period.this_year)
        is_child = person("is_child", period.this_year)
        earned_income = add(person, period, p.sources.earned)
        unearned_income = add(person, period, p.sources.unearned)
        counted_earned = spm_unit.sum(earned_income * is_parent)
        counted_unearned = spm_unit.sum(unearned_income * (is_parent | is_child))
        return counted_earned + counted_unearned
