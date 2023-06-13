from policyengine_us.model_api import *
import numpy as np


class sc_two_wage_earner_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "South Carolina two wage earner credits"
    defined_for = StateCode.SC
    unit = USD
    definition_period = YEAR
    reference = "https://dor.sc.gov/forms-site/Forms/SC1040TT_2021.pdf"

    def formula(tax_unit, period, parameters):
        # First get their filing status.
        filing_status = tax_unit("filing_status", period)

        # Then get the SC two wage earner credits part of the parameter tree
        p = parameters(
            period
        ).gov.states.sc.tax.income.credits.two_wage_earner.rates

        # Determine the filing status
        joint = filing_status == filing_status.possible_values.JOINT

        # Determine the lesser value
        less_income = min(head_eligible, spouse_eligible)

        # Calculate two wage earner credits
        return np.round(p.calc(less_income) * joint)
