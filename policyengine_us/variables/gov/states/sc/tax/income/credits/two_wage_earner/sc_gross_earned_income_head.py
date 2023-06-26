from policyengine_us.model_api import *


class sc_gross_earned_income_head(Variable):
    value_type = float
    entity = SPMUnit
    label = "South Carolina gross earned income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.SC

    def formula(spm_unit, period, parameters):
        person = spm_unit.members
        is_head = person("is_tax_unit_head", period)
        earned_income = person("sc_gross_earned_income", period)
        return spm_unit.any(is_head * earned_income)
    