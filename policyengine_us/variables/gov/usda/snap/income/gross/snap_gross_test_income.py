from policyengine_us.model_api import *


class snap_gross_test_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "SNAP gross income for the gross income test"
    reference = (
        "https://www.law.cornell.edu/uscode/text/7/2014#c",
        "https://www.law.cornell.edu/cfr/text/7/273.11#c_3_i",
    )
    unit = USD

    def formula(spm_unit, period, parameters):
        # Certain states count the full income of certain ineligible aliens
        # under the gross income test while prorating it under the net
        # income test.
        gross_income = spm_unit("snap_gross_income", period)
        person = spm_unit.members
        full_count = person("is_snap_gross_test_full_income_count_alien", period)
        share = person("snap_income_counted_share", period)
        employment = person("snap_earned_income_person", period)
        unearned = person("snap_unearned_income_person", period)
        uncounted_income = spm_unit.sum(
            full_count * (employment + unearned) * (1 - share)
        )
        # Add back the uncounted portion of these aliens' self-employment
        # income, attributed by signed gross self-employment income as in
        # snap_earned_income.
        countable = person("snap_countable_earner", period)
        gross_self_employment = person(
            "snap_gross_self_employment_income_person", period
        )
        unit_gross = spm_unit.sum(gross_self_employment)
        unit_net = spm_unit(
            "snap_self_employment_income_after_expense_deduction", period
        )
        uncounted_weight = spm_unit.sum(
            gross_self_employment * countable * full_count * (1 - share)
        )
        uncounted_self_employment = where(
            unit_gross > 0,
            unit_net * uncounted_weight / where(unit_gross > 0, unit_gross, 1),
            0,
        )
        # Count these aliens' child support payments in full as well, in
        # states that deduct child support when computing gross income.
        child_support = person("child_support_expense", period)
        uncounted_child_support = spm_unit.sum(full_count * child_support * (1 - share))
        state = spm_unit.household("state_code_str", period)
        p = parameters(period).gov.usda.snap.income.deductions
        cs_deductible = p.child_support[state]
        return (
            gross_income
            + uncounted_income
            + uncounted_self_employment
            - cs_deductible * uncounted_child_support
        )
