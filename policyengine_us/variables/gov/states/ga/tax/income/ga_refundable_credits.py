from policyengine_us.model_api import *


class ga_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Georgia refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.GA
    # The HB 162 surplus tax rebate is capped at Form 500 Line 16 and pays
    # out past a zero balance due (O.C.G.A. 48-7-20.2(b), (d)), so it
    # applies after the nonrefundable credits rather than inside their
    # ordered stack. Its amount parameter is nonzero only for tax year 2021.
    adds = ["ga_surplus_tax_rebate"]
