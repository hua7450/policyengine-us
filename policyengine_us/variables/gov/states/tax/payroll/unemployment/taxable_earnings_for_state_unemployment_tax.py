from policyengine_us.model_api import *


class taxable_earnings_for_state_unemployment_tax(Variable):
    value_type = float
    entity = Person
    label = "Taxable earnings for state unemployment tax"
    documentation = (
        "Earnings subject to the employer-side state unemployment insurance "
        "tax base, using household state as a proxy for work state."
    )
    definition_period = YEAR
    unit = USD

    def formula(person, period, parameters):
        p = parameters(period).gov.states.tax.payroll.unemployment
        state_code = person.household("state_code", period)
        wage_base = p.taxable_wage_base[state_code]
        return min_(person("payroll_tax_gross_wages", period), wage_base)
