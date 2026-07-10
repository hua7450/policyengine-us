from policyengine_us.model_api import *


class sd_cca_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "South Dakota CCA countable income"
    definition_period = MONTH
    defined_for = StateCode.SD
    reference = (
        "https://dss.sd.gov/docs/childcare/assistance/Subsidy_Manual.pdf#page=10"
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.sd.dss.cca.income
        gross_income = spm_unit("sd_cca_gross_income", period)
        person = spm_unit.members
        person_earned = add(
            person, period, ["employment_income", "self_employment_income"]
        )
        is_child = person("age", period.this_year) < p.child_earned_income_exclusion_age
        # The earned income of children is excluded entirely.
        child_earned_income = spm_unit.sum(is_child * person_earned)
        # A 4% standard deduction applies to the remaining (adult) earned income.
        adult_earned_income = spm_unit.sum(~is_child * person_earned)
        earned_disregard = max_(adult_earned_income, 0) * p.earned_income_disregard
        # Court-ordered child support paid out is deducted.
        child_support_expense = add(spm_unit, period, ["child_support_expense"])
        return max_(
            gross_income
            - child_earned_income
            - earned_disregard
            - child_support_expense,
            0,
        )
