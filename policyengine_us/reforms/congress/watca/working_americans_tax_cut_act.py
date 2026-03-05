from policyengine_us.model_api import *
from policyengine_core.periods import period as period_
from policyengine_core.periods import instant


def create_watca_exemption() -> Reform:
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
            # Linear phase-out between amount and phase_out_end
            phase_out_range = phase_out_end - amount
            uncapped = (phase_out_end - agi) / phase_out_range
            fraction = clip(uncapped, 0, 1)
            return amount * fraction

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

    class reform(Reform):
        def apply(self):
            self.update_variable(watca_cost_of_living_exemption)
            self.update_variable(taxable_income)

    return reform


def create_watca_surtax() -> Reform:
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

    class income_tax_before_credits(Variable):
        value_type = float
        entity = TaxUnit
        definition_period = YEAR
        label = "income tax before credits"
        unit = USD
        documentation = (
            "Total (regular + AMT) income tax liability before credits"
        )

        adds = [
            "income_tax_main_rates",
            "capital_gains_tax",
            "alternative_minimum_tax",
            "watca_millionaire_surtax",
        ]

    class reform(Reform):
        def apply(self):
            self.update_variable(watca_millionaire_surtax)
            self.update_variable(income_tax_before_credits)

    return reform


def create_watca_reform(parameters, period, bypass: bool = False):
    if bypass is True:
        exemption = create_watca_exemption()
        surtax = create_watca_surtax()

        class combined(Reform):
            def apply(self):
                exemption.apply(self)
                surtax.apply(self)

        return combined

    parameter = parameters.gov.contrib.congress.watca
    current_period = period_(period)
    reform_active = False

    for i in range(5):
        if parameter(current_period).in_effect:
            reform_active = True
            break
        current_period = current_period.offset(1, "year")

    if not reform_active:
        return None

    surtax_active = False
    check_period = period_(period)
    for i in range(5):
        if parameter(check_period).surtax.in_effect:
            surtax_active = True
            break
        check_period = check_period.offset(1, "year")

    exemption = create_watca_exemption()

    if surtax_active:
        surtax = create_watca_surtax()

        class combined(Reform):
            def apply(self):
                exemption.apply(self)
                surtax.apply(self)

        return combined

    return exemption


watca_reform_object = create_watca_reform(None, None, bypass=True)
