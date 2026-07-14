from policyengine_us.model_api import *


class mt_child_dependent_care_expense_deduction(Variable):
    value_type = float
    entity = Person
    label = "Montana child dependent care expense deduction"
    unit = USD
    definition_period = YEAR
    reference = "https://casetext.com/statute/montana-code/title-15-taxation/chapter-30-individual-income-tax/part-21-rate-and-general-provisions/section-15-30-2131-repealed-effective-112024-temporary-deductions-allowed-in-computing-net-income"
    defined_for = StateCode.MT

    def formula(person, period, parameters):
        tax_unit = person.tax_unit
        # Line 1
        eligible_children = tax_unit(
            "mt_child_dependent_care_expense_deduction_eligible_children",
            period,
        )
        p = parameters(
            period
        ).gov.states.mt.tax.income.deductions.child_dependent_care_expense
        if not p.in_effect:
            return 0
        childcare_expenses = tax_unit("tax_unit_childcare_expenses", period)
        childcare_cap = p.cap.calc(eligible_children)
        capped_childcare_expenses = min_(childcare_expenses, childcare_cap)
        person = tax_unit.members
        age = person("age", period)
        # `care_expenses` represents in-home services for this deduction.
        care_expenses = person("care_expenses", period)
        qualifying_person = person(
            "mt_child_dependent_care_expense_deduction_eligible_child",
            period,
        )
        qualifying_adult = qualifying_person & (age >= p.age_limit)
        qualifying_adult_care_expenses = tax_unit.sum(care_expenses * qualifying_adult)
        # Line 2
        qualifying_expenses = capped_childcare_expenses + qualifying_adult_care_expenses
        capped_expenses = min_(qualifying_expenses, p.overall_cap)
        # Line 3
        agi = person("mt_agi_indiv", period)
        # Line 6
        reduction = p.phase_out.calc(agi)
        # The deduction has to be allocated equally between spouses
        head_or_spouse = person("is_tax_unit_head_or_spouse", period)
        return head_or_spouse * (max_(0, capped_expenses - reduction) * 0.5)
