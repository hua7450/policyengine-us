from policyengine_us.model_api import *


class employer_payroll_tax(Variable):
    value_type = float
    entity = Person
    label = "Employer payroll tax"
    documentation = (
        "Employer-side payroll tax liability, including Social Security, "
        "Medicare, federal unemployment tax, and state unemployment tax."
    )
    definition_period = YEAR
    unit = USD

    def formula(person, period, parameters):
        return add(
            person,
            period,
            [
                "employer_social_security_tax",
                "employer_medicare_tax",
                "employer_federal_unemployment_tax",
                "employer_state_unemployment_tax",
            ],
        )
