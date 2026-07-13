from policyengine_us.model_api import *


class ok_ccs_countable_self_employment_income(Variable):
    value_type = float
    entity = Person
    unit = USD
    label = "Oklahoma Child Care Subsidy countable self-employment income"
    definition_period = MONTH
    defined_for = StateCode.OK
    reference = "https://okrules.elaws.us/oac/340:40-7-11"

    def formula(person, period, parameters):
        # A business loss is not deducted from other household income
        # (OAC 340:40-7-11(b)(3)(B)), so each person's self-employment
        # income is floored at zero before aggregation.
        return max_(person("self_employment_income", period), 0)
