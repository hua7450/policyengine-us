from policyengine_us.model_api import *


class sc_two_wage_earner_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "South Carolina two wage earner credit"
    defined_for = StateCode.SC
    unit = USD
    definition_period = YEAR
    reference = "https://dor.sc.gov/forms-site/Forms/SC1040TT_2021.pdf"

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        # First get their filing status.
        filing_status = tax_unit("filing_status", period)

        # Then get the SC two wage earner credits part of the parameter tree
        p = parameters(
            period
        ).gov.states.sc.tax.income.credits.two_wage_earner.rates

        # Determine the filing status
        joint = filing_status == filing_status.possible_values.JOINT

        # get head eligible amount and spouse eligible amount
        head_eligible = tax_unit.max(
            person("sc_gross_earned_income_head", period)
        )
        spouse_eligible = tax_unit.max(
            person("sc_gross_earned_income_spouse", period)
        )

        # Determine the lesser value
        less_income = min_(head_eligible, spouse_eligible)

        # Calculate two wage earner credits
        return p.calc(less_income) * joint
