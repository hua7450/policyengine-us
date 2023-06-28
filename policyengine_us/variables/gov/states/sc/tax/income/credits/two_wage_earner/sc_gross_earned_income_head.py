from policyengine_us.model_api import *


class sc_gross_earned_income_head(Variable):
    value_type = float
    entity = Person
    label = "South Carolina head gross earned income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.SC

    def formula(person, period, parameters):
        is_head = person("is_tax_unit_head", period)
        earned_income = person("sc_gross_earned_income", period)
        return is_head * earned_income
