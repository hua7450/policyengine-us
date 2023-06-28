from policyengine_us.model_api import *


class sc_gross_earned_income_spouse(Variable):
    value_type = float
    entity = Person
    label = "South Carolina spouse gross earned income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.SC

    def formula(person, period, parameters):
        is_spouse = person("is_tax_unit_spouse", period)
        earned_income = person("sc_gross_earned_income", period)
        return is_spouse * earned_income
