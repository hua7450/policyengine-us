from policyengine_us.model_api import *
from policyengine_core.periods import period as period_
from policyengine_core.periods import instant

WATCA_REFERENCES = [
    {
        "title": "Working Americans' Tax Cut Act",
        "href": "https://www.vanhollen.senate.gov/imo/media/doc/working_americans_tax_cut_act_bill_text.pdf",
    },
]


def create_watca() -> Reform:
    class watca_alternative_tax_magi(Variable):
        value_type = float
        entity = TaxUnit
        label = "WATCA alternative tax modified AGI"
        definition_period = YEAR
        unit = USD
        reference = WATCA_REFERENCES
        documentation = "Section 1A(d): AGI + foreign income exclusions (sec 911, 931, 933) + non-taxable Social Security."

        def formula(tax_unit, period, parameters):
            agi = tax_unit("adjusted_gross_income", period)
            foreign_earned_income = tax_unit("foreign_earned_income_exclusion", period)
            possession_income = tax_unit("specified_possession_income", period)
            puerto_rico = tax_unit("puerto_rico_income", period)
            nontaxable_ss = tax_unit("tax_exempt_social_security", period)
            return (
                agi
                + foreign_earned_income
                + possession_income
                + puerto_rico
                + nontaxable_ss
            )

    class watca_surtax_magi(Variable):
        value_type = float
        entity = TaxUnit
        label = "WATCA surtax modified AGI"
        definition_period = YEAR
        unit = USD
        reference = WATCA_REFERENCES
        documentation = (
            "Section 59B(d): AGI - investment interest deduction (sec 163(d))."
        )

        def formula(tax_unit, period, parameters):
            agi = tax_unit("adjusted_gross_income", period)
            investment_interest = add(tax_unit, period, ["investment_interest_expense"])
            return agi - investment_interest

    class watca_alternative_tax_eligible(Variable):
        value_type = bool
        entity = TaxUnit
        label = "Eligible for WATCA alternative maximum tax"
        definition_period = YEAR
        reference = WATCA_REFERENCES
        documentation = "Section 1A(b): MAGI < 175% of exemption, and not claimed as dependent on another return."

        def formula(tax_unit, period, parameters):
            magi = tax_unit("watca_alternative_tax_magi", period)
            filing_status = tax_unit("filing_status", period)
            p = parameters(period).gov.contrib.congress.watca.cost_of_living_exemption
            exemption_amount = p.amount[filing_status]
            income_limit = exemption_amount * p.income_limit_multiple
            income_eligible = magi < income_limit
            head_dependent = tax_unit("head_is_dependent_elsewhere", period)
            spouse_dependent = tax_unit("spouse_is_dependent_elsewhere", period)
            not_dependent = ~head_dependent & ~spouse_dependent
            return income_eligible & not_dependent

    class watca_alternative_max_tax(Variable):
        value_type = float
        entity = TaxUnit
        label = "WATCA alternative maximum tax"
        definition_period = YEAR
        unit = USD
        reference = WATCA_REFERENCES
        documentation = (
            "Section 1A(a): 25.5% of MAGI above the cost of living exemption."
        )

        def formula(tax_unit, period, parameters):
            magi = tax_unit("watca_alternative_tax_magi", period)
            filing_status = tax_unit("filing_status", period)
            p = parameters(period).gov.contrib.congress.watca.cost_of_living_exemption
            exemption_amount = p.amount[filing_status]
            rate = p.alternative_tax_rate
            return max_(0, magi - exemption_amount) * rate

    class watca_millionaire_surtax(Variable):
        value_type = float
        entity = TaxUnit
        label = "WATCA millionaire surtax"
        definition_period = YEAR
        unit = USD
        reference = WATCA_REFERENCES
        documentation = (
            "Section 59B: Surtax on high income individuals based on modified AGI."
        )

        def formula(tax_unit, period, parameters):
            magi = tax_unit("watca_surtax_magi", period)
            p = parameters(period).gov.contrib.congress.watca.surtax
            filing_status = tax_unit("filing_status", period)
            joint = (filing_status == filing_status.possible_values.JOINT) | (
                filing_status == filing_status.possible_values.SURVIVING_SPOUSE
            )
            return where(
                joint,
                p.rate.joint.calc(magi),
                p.rate.single.calc(magi),
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
            self.update_variable(watca_alternative_tax_magi)
            self.update_variable(watca_surtax_magi)
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
