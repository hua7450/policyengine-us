from policyengine_us.model_api import *


class in_tip_income_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Indiana tip income deduction"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://iga.in.gov/pdf-documents/124/2026/senate/bills/SB0243/SB0243.05.ENRH.pdf#page=51",
        "https://iga.in.gov/legislative/2026/bills/senate/243",
    )
    defined_for = StateCode.IN

    def formula(tax_unit, period, parameters):
        # IC 6-3-2-31(c) contains a proration rule for when tips are
        # partially excluded from IN AGI by another provision. No such
        # provision currently exists, so the full federal amount is used.
        p = parameters(period).gov.states["in"].tax.income.deductions.obbba_conformity
        available = p.tip_income_deduction_available
        federal_deduction = tax_unit("tip_income_deduction", period)
        return available * federal_deduction
