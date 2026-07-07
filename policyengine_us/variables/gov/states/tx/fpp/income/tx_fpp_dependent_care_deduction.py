from policyengine_us.model_api import *


class tx_fpp_dependent_care_deduction(Variable):
    value_type = float
    entity = SPMUnit
    label = "Texas Family Planning Program dependent care deduction"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.law.cornell.edu/regulations/texas/1-Tex-Admin-Code-SS-382-109"
    )
    defined_for = StateCode.TX

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.tx.fpp.income
        person = spm_unit.members
        expenses = person("pre_subsidy_childcare_expenses", period)
        age = person("age", period)
        # The same $175 monthly cap applies to dependents age two or
        # older and to dependent adults with a disability under
        # 1 TAC 382.109(2)(A)-(B).
        monthly_cap = p.dependent_care.calc(age)
        return spm_unit.sum(min_(expenses, monthly_cap * MONTHS_IN_YEAR))
