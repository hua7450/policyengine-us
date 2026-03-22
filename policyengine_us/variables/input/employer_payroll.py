from policyengine_us.model_api import *


class employer_state_unemployment_tax_rate_override(Variable):
    value_type = float
    entity = Person
    label = "Employer state unemployment tax rate override"
    documentation = (
        "Optional employer-specific override for the employer-side state "
        "unemployment tax rate. Set to a non-negative rate to replace the "
        "model default."
    )
    unit = "/1"
    definition_period = YEAR
    default_value = -1


class employer_headcount(Variable):
    value_type = int
    entity = Person
    label = "Employer headcount"
    documentation = (
        "Employer employee count used as a proxy for size-based payroll "
        "contribution rules, including paid leave and similar programs."
    )
    definition_period = YEAR
    default_value = 100


class employer_quarterly_payroll_expense_override(Variable):
    value_type = float
    entity = Person
    label = "Employer quarterly payroll expense override"
    documentation = (
        "Optional override for employer quarterly payroll expense used by "
        "payroll-expense taxes such as New York's MCTMT. Set to a non-negative "
        "amount to replace the model proxy."
    )
    unit = USD
    definition_period = YEAR
    default_value = -1
