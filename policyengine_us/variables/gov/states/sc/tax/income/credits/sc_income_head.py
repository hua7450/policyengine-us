from policyengine_us.model_api import *


class sc_income_head(Variable):
    value_type = float
    entity = TaxUnit
    label = "South Carolina head's income"
    defined_for = StateCode.SC
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        head = person("is_tax_unit_head", period)
        income = tax_unit("sc_taxable_income", period)
        return tax_unit.sum(head * income)
