from policyengine_us.model_api import *


class mt_child_dependent_care_expense_deduction_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Qualifying person for the Montana child dependent care expense deduction"
    definition_period = YEAR
    defined_for = StateCode.MT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.states.mt.tax.income.deductions.child_dependent_care_expense
        age = person("age", period)
        dependent = person("is_tax_unit_dependent", period)
        spouse = person("is_tax_unit_spouse", period)
        eligible_child = dependent & (age < p.age_limit)
        # MCA 15-30-2131(1)(c) waives the age limit for a dependent "unable
        # to provide self-care because of physical or mental illness" and
        # also includes a spouse who is unable to provide self-care.
        incapable_of_self_care = person("is_incapable_of_self_care", period)
        eligible_adult = (dependent | spouse) & incapable_of_self_care
        return eligible_child | eligible_adult
