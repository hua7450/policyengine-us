from policyengine_us.model_api import *


class co_sales_tax_refund(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado sales tax refund"
    unit = USD
    definition_period = YEAR
    reference = "https://tax.colorado.gov/sites/tax/files/documents/DR_0104_Book_2022.pdf#page=23"
    defined_for = "co_sales_tax_refund_eligible"

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.co.tax.income.credits.sales_tax_refund.amount
        if p.flat_amount_enabled:
            amount = p.amount
        else:
            agi = tax_unit("co_modified_agi", period)
            amount = p.scale.calc(agi)
        # The refund is claimed per qualifying individual (head and/or spouse),
        # so multiply the per-person amount by the number of eligible filers
        # rather than doubling for every joint return.
        eligible_count = tax_unit.sum(
            tax_unit.members("co_sales_tax_refund_person_eligible", period)
        )
        return eligible_count * amount
