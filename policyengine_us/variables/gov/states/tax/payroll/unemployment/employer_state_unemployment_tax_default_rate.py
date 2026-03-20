from policyengine_us.model_api import *


class employer_state_unemployment_tax_default_rate(Variable):
    value_type = float
    entity = Person
    label = "Default employer state unemployment tax rate"
    documentation = (
        "Default employer-side state unemployment tax rate. Uses the state's "
        "published new-employer rate when a single statewide rate exists, and "
        "falls back to the reported average tax rate on taxable wages when the "
        "state uses industry-average or other employer-specific schedules."
    )
    definition_period = YEAR
    unit = "/1"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.tax.payroll.unemployment
        state_code = person.household("state_code", period)
        return p.default_rate[state_code]
