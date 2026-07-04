from policyengine_us.model_api import *


class snap_earned_income_person(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "SNAP earned income per person"
    reference = "https://www.law.cornell.edu/cfr/text/7/273.9#b_1"
    unit = USD
    defined_for = "snap_countable_earner"

    def formula(person, period, parameters):
        p = parameters(period).gov.usda.snap.income.sources
        employment = add(person, period, p.earned_person)
        # Self-employment income net of the expense deduction is computed at
        # the SPM unit level; attribute it to members in proportion to their
        # gross self-employment income.
        self_employment = add(
            person,
            period,
            [
                "self_employment_income_before_lsr",
                "sstb_self_employment_income_before_lsr",
            ],
        )
        weight = max_(self_employment, 0)
        unit_weight = person.spm_unit.sum(weight)
        unit_self_employment = person.spm_unit(
            "snap_self_employment_income_after_expense_deduction", period
        )
        attributed_self_employment = where(
            unit_weight > 0,
            unit_self_employment * weight / where(unit_weight > 0, unit_weight, 1),
            0,
        )
        return employment + attributed_self_employment
