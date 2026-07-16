from policyengine_us.model_api import *


class ut_ccap_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Utah CCAP countable income"
    definition_period = MONTH
    defined_for = StateCode.UT
    reference = "https://utrules.elaws.us/uac/r986-700-710"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ut.dwf.ccap.income
        gross_income = spm_unit("ut_ccap_gross_income", period)
        person = spm_unit.members
        age = person("age", period.this_year)
        # is_parent (own children in the household) rather than a tax-unit
        # role flag, which is never true for an under-18 person and would
        # make the minor-parent carve-out unreachable.
        is_parent = person("is_parent", period.this_year)
        earned_income = add(
            person, period, ["employment_income", "self_employment_income"]
        )
        # The earned income of a minor child who is not a parent is excluded
        # (R986-700-710(1)(b)(i)); a minor parent's earnings stay countable.
        is_excluded_minor = (age < p.child_earned_income_exclusion_age) & ~is_parent
        excluded_minor_earnings = spm_unit.sum(is_excluded_minor * earned_income)
        # The first $50 of child support received by the family is deducted
        # (R986-700-710(2)(a)).
        child_support_received = add(spm_unit, period, ["child_support_received"])
        child_support_deduction = min_(
            child_support_received,
            p.deductions.child_support_received_deduction,
        )
        # Court-ordered child support and alimony paid out by the household
        # are deducted (R986-700-710(2)).
        support_paid = add(
            spm_unit, period, ["child_support_expense", "alimony_expense"]
        )
        # $100 is deducted for each person with countable earned income
        # (R986-700-710(2)(c)); excluded minors' earnings are not countable.
        counted_earners = spm_unit.sum((earned_income > 0) & ~is_excluded_minor)
        earned_income_deduction = p.deductions.earned_income_deduction * counted_earners
        # A $100 automatic medical deduction applies without proof of
        # expenditure (R986-700-710(2)(d)).
        deductions = (
            child_support_deduction
            + support_paid
            + earned_income_deduction
            + p.deductions.medical_deduction
        )
        return max_(gross_income - excluded_minor_earnings - deductions, 0)
