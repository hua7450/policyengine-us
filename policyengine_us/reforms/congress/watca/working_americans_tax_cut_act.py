from policyengine_us.model_api import *
from policyengine_core.periods import period as period_
from policyengine_core.periods import instant

WATCA_REFERENCES = [
    {
        "title": "Working Americans' Tax Cut Act bill summary (via Jeff Stein, WaPo)",
        "href": "https://x.com/JStein_WaPo/status/2029621495295619363",
    },
    {
        "title": "Democrat's plan would eliminate federal income"
        " taxes for half of U.S. workers",
        "href": "https://www.washingtonpost.com/business/"
        "2026/03/05/middle-class-tax-relief-senate-bill/",
    },
]


def create_watca() -> Reform:
    class watca_alternative_tax_eligible(Variable):
        value_type = bool
        entity = TaxUnit
        label = "Eligible for WATCA alternative maximum tax"
        definition_period = YEAR
        reference = WATCA_REFERENCES

        def formula(tax_unit, period, parameters):
            agi = tax_unit("adjusted_gross_income", period)
            filing_status = tax_unit("filing_status", period)
            p = parameters(period).gov.contrib.congress.watca.cost_of_living_exemption
            exemption_amount = p.amount[filing_status]
            income_limit = exemption_amount * p.income_limit_multiple
            return agi < income_limit

    class watca_alternative_max_tax(Variable):
        value_type = float
        entity = TaxUnit
        label = "WATCA alternative maximum tax"
        definition_period = YEAR
        unit = USD
        reference = WATCA_REFERENCES
        documentation = "The alternative maximum tax under WATCA: 25.5% of MAGI above the cost of living exemption."

        def formula(tax_unit, period, parameters):
            agi = tax_unit("adjusted_gross_income", period)
            filing_status = tax_unit("filing_status", period)
            p = parameters(period).gov.contrib.congress.watca.cost_of_living_exemption
            exemption_amount = p.amount[filing_status]
            rate = p.alternative_tax_rate
            return max_(0, agi - exemption_amount) * rate

    class watca_millionaire_surtax(Variable):
        value_type = float
        entity = TaxUnit
        label = "WATCA millionaire surtax"
        definition_period = YEAR
        unit = USD
        reference = WATCA_REFERENCES

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

        def formula(tax_unit, period, parameters):
            standard_tax = add(
                tax_unit,
                period,
                [
                    "income_tax_main_rates",
                    "capital_gains_tax",
                    "alternative_minimum_tax",
                ],
            )
            alternative_max = tax_unit("watca_alternative_max_tax", period)
            eligible = tax_unit("watca_alternative_tax_eligible", period)
            tax_after_cap = where(
                eligible,
                min_(standard_tax, alternative_max),
                standard_tax,
            )
            p = parameters(period).gov.contrib.congress.watca.surtax
            surtax = where(
                p.in_effect,
                tax_unit("watca_millionaire_surtax", period),
                0,
            )
            return tax_after_cap + surtax

    class reform(Reform):
        def apply(self):
            self.update_variable(watca_alternative_tax_eligible)
            self.update_variable(watca_alternative_max_tax)
            self.update_variable(watca_millionaire_surtax)
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
