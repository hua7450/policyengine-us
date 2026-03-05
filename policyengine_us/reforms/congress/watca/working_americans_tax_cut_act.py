from policyengine_us.model_api import *
from policyengine_core.periods import period as period_
from policyengine_core.periods import instant

# Working Americans' Tax Cut Act (WATCA)
# Sponsor: Sen. Chris Van Hollen (D-MD), with 15 Senate Democratic
# co-sponsors. Introduced March 5, 2026.
#
# Sources:
#   - Official bill summary (Sen. Van Hollen's office)
#   - Washington Post (Jeff Stein, March 5, 2026):
#     https://www.washingtonpost.com/business/2026/03/05/
#     middle-class-tax-relief-senate-bill/
#   - ITEP analysis: ~130M people receive a tax cut
#   - Yale Budget Lab: surtax impacts 615K filers, raises
#     ~$1.46 trillion over 10 years
#
# Cost of living exemption:
#   Single: $46,000 (2025 nationally aggregated living wage,
#     MIT Living Wage Calculator). Phase-out at 175% = $80,500.
#   HOH: $64,400 (140% of single). Phase-out at $112,700.
#   MFJ: $92,000 (200% of single). Phase-out at $161,000.
#   Benefits phase out linearly between the exemption amount
#   and 175% of that amount.
#
# Millionaire surtax (on AGI, including wages and investment):
#   Single: 5% > $1M, 10% > $2M, 12% > $5M
#   Joint:  5% > $1.5M, 10% > $3M, 12% > $7.5M


def create_watca() -> Reform:
    class watca_cost_of_living_exemption(Variable):
        value_type = float
        entity = TaxUnit
        label = "WATCA cost of living exemption"
        definition_period = YEAR
        unit = USD

        def formula(tax_unit, period, parameters):
            agi = tax_unit("adjusted_gross_income", period)
            filing_status = tax_unit("filing_status", period)
            p = parameters(
                period
            ).gov.contrib.congress.watca.cost_of_living_exemption
            amount = p.amount[filing_status]
            phase_out_end = amount * p.phase_out_multiple
            phase_out_range = phase_out_end - amount
            uncapped = (phase_out_end - agi) / phase_out_range
            fraction = clip(uncapped, 0, 1)
            return amount * fraction

    class watca_millionaire_surtax(Variable):
        value_type = float
        entity = TaxUnit
        label = "WATCA millionaire surtax"
        definition_period = YEAR
        unit = USD

        def formula(tax_unit, period, parameters):
            agi = tax_unit("adjusted_gross_income", period)
            p = parameters(period).gov.contrib.congress.watca.surtax
            filing_status = tax_unit("filing_status", period)
            joint = (filing_status == filing_status.possible_values.JOINT) | (
                filing_status == filing_status.possible_values.SURVIVING_SPOUSE
            )
            return where(
                joint,
                p.rate.joint.calc(agi),
                p.rate.single.calc(agi),
            )

    class taxable_income(Variable):
        value_type = float
        entity = TaxUnit
        label = "IRS taxable income"
        unit = USD
        definition_period = YEAR

        def formula(tax_unit, period, parameters):
            agi = tax_unit("adjusted_gross_income", period)
            exemptions = tax_unit("exemptions", period)
            deductions = tax_unit("taxable_income_deductions", period)
            watca_exemption = tax_unit(
                "watca_cost_of_living_exemption", period
            )
            return max_(0, agi - exemptions - deductions - watca_exemption)

    class income_tax_before_credits(Variable):
        value_type = float
        entity = TaxUnit
        definition_period = YEAR
        label = "income tax before credits"
        unit = USD
        documentation = (
            "Total (regular + AMT) income tax liability before" " credits"
        )

        def formula(tax_unit, period, parameters):
            base = add(
                tax_unit,
                period,
                [
                    "income_tax_main_rates",
                    "capital_gains_tax",
                    "alternative_minimum_tax",
                ],
            )
            p = parameters(period).gov.contrib.congress.watca.surtax
            surtax = where(
                p.in_effect,
                tax_unit("watca_millionaire_surtax", period),
                0,
            )
            return base + surtax

    class reform(Reform):
        def apply(self):
            self.update_variable(watca_cost_of_living_exemption)
            self.update_variable(watca_millionaire_surtax)
            self.update_variable(taxable_income)
            self.update_variable(income_tax_before_credits)

    return reform


def create_watca_reform(parameters, period, bypass: bool = False):
    if bypass is True:
        return create_watca()

    parameter = parameters.gov.contrib.congress.watca
    current_period = period_(period)
    reform_active = False

    for i in range(5):
        if parameter(current_period).in_effect:
            reform_active = True
            break
        current_period = current_period.offset(1, "year")

    if reform_active:
        return create_watca()
    else:
        return None


watca_reform_object = create_watca_reform(None, None, bypass=True)
