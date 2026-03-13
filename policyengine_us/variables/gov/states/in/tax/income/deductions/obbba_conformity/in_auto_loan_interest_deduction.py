from policyengine_us.model_api import *


class in_auto_loan_interest_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Indiana auto loan interest deduction"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://iga.in.gov/pdf-documents/124/2026/senate/bills/SB0243/SB0243.05.ENRH.pdf#page=52",
        "https://iga.in.gov/legislative/2026/bills/senate/243",
    )
    defined_for = StateCode.IN

    def formula(tax_unit, period, parameters):
        # IC 6-3-2-33(c) requires IN residency (covered by defined_for)
        # and has spouse attribution rules for joint filers. IC 6-3-2-33(d)
        # excludes estates/trusts. These are not separately modeled.
        p = parameters(period).gov.states["in"].tax.income.deductions.obbba_conformity
        available = p.auto_loan_interest_deduction_available
        federal_deduction = tax_unit("auto_loan_interest_deduction", period)
        return available * federal_deduction
