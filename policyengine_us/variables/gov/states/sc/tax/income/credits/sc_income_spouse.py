from policyengine_us.model_api import *


class sc_income_spouse(Variable):
    value_type = float
    entity = TaxUnit
    label = "South Carolina spouse's income"
    defined_for = StateCode.SC
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        spouse = person("is_tax_unit_spouse", period)
        income = tax_unit("sc_taxable_income", period)
        return tax_unit.sum(spouse * income)
