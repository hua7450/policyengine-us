from policyengine_us.model_api import *
from policyengine_core.periods import period as period_


def create_wa_sb6346() -> Reform:
    """
    WA SSB 6346 - 9.9% income tax on high earners.

    Imposes a 9.9% tax on Washington taxable income (federal AGI minus
    a $1M standard deduction and capped charitable deduction).

    Reference: https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf
    """

    class wa_income_tax_base_income(Variable):
        value_type = float
        entity = TaxUnit
        label = "Washington base income under SSB 6346"
        unit = USD
        definition_period = YEAR
        reference = "https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf#page=17"
        defined_for = StateCode.WA

        def formula(tax_unit, period, parameters):
            return tax_unit("adjusted_gross_income", period)

    class wa_income_tax_charitable_deduction(Variable):
        value_type = float
        entity = TaxUnit
        label = "Washington income tax charitable deduction under SSB 6346"
        unit = USD
        definition_period = YEAR
        reference = "https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf#page=21"
        defined_for = StateCode.WA

        def formula(tax_unit, period, parameters):
            p = parameters(period).gov.contrib.states.wa.sb6346.charitable_deduction.cap
            filing_status = tax_unit("filing_status", period)
            charitable = add(
                tax_unit,
                period,
                ["charitable_cash_donations", "charitable_non_cash_donations"],
            )
            is_joint = filing_status == filing_status.possible_values.JOINT
            cap = where(is_joint, p.joint, p.individual)
            return min_(charitable, cap)

    class wa_income_tax_standard_deduction(Variable):
        value_type = float
        entity = TaxUnit
        label = "Washington income tax standard deduction under SSB 6346"
        unit = USD
        definition_period = YEAR
        reference = "https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf#page=22"
        defined_for = StateCode.WA

        def formula(tax_unit, period, parameters):
            p = parameters(period).gov.contrib.states.wa.sb6346.standard_deduction
            return p.amount

    class wa_income_tax_taxable_income(Variable):
        value_type = float
        entity = TaxUnit
        label = "Washington taxable income under SSB 6346"
        unit = USD
        definition_period = YEAR
        reference = (
            "https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf#page=21",
            "https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf#page=22",
        )
        defined_for = StateCode.WA

        def formula(tax_unit, period, parameters):
            base_income = tax_unit("wa_income_tax_base_income", period)
            charitable_deduction = tax_unit(
                "wa_income_tax_charitable_deduction", period
            )
            standard_deduction = tax_unit("wa_income_tax_standard_deduction", period)
            return max_(base_income - charitable_deduction - standard_deduction, 0)

    class wa_income_tax(Variable):
        value_type = float
        entity = TaxUnit
        label = "Washington income tax"
        unit = USD
        definition_period = YEAR
        reference = "https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf#page=16"
        defined_for = StateCode.WA

        def formula(tax_unit, period, parameters):
            p = parameters(period).gov.contrib.states.wa.sb6346
            taxable_income = tax_unit("wa_income_tax_taxable_income", period)
            sb6346_tax = taxable_income * p.rate
            capital_gains_tax = tax_unit("wa_capital_gains_tax", period)
            refundable_credits = tax_unit("wa_refundable_credits", period)
            return sb6346_tax + capital_gains_tax - refundable_credits

    class reform(Reform):
        def apply(self):
            self.add_variable(wa_income_tax_base_income)
            self.add_variable(wa_income_tax_charitable_deduction)
            self.add_variable(wa_income_tax_standard_deduction)
            self.add_variable(wa_income_tax_taxable_income)
            self.update_variable(wa_income_tax)

    return reform


def create_wa_sb6346_reform(parameters, period, bypass=False):
    if bypass:
        return create_wa_sb6346()

    p = parameters.gov.contrib.states.wa.sb6346

    reform_active = False
    current_period = period_(period)

    for _ in range(5):
        if p(current_period).in_effect:
            reform_active = True
            break
        current_period = current_period.offset(1, "year")

    if reform_active:
        return create_wa_sb6346()
    else:
        return None


wa_sb6346 = create_wa_sb6346_reform(None, None, bypass=True)
