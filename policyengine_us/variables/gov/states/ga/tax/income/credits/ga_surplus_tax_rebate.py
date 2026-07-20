from policyengine_us.model_api import *


class ga_surplus_tax_rebate(Variable):
    value_type = float
    entity = TaxUnit
    label = "Georgia surplus tax rebate"
    unit = USD
    definition_period = YEAR
    reference = "https://www.legis.ga.gov/api/legislation/document/20232024/217823"
    defined_for = StateCode.GA

    def formula(tax_unit, period, parameters):
        filing_status = tax_unit("filing_status", period)
        p = parameters(period).gov.states.ga.tax.income.credits.surplus_tax_rebate
        cap = p.amount[filing_status]
        # O.C.G.A. 48-7-20.2(b)(1)(A): the refund is capped at the liability
        # "as properly reported on Line 16 of the 2021 Georgia Form 500" -
        # the tax before credits. Credits on Lines 17-21 do not reduce it,
        # and it pays out past a zero balance due.
        line_16_tax = tax_unit("ga_income_tax_before_non_refundable_credits", period)
        return min_(cap, line_16_tax)
