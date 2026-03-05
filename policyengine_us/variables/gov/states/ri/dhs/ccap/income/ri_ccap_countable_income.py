from policyengine_us.model_api import *


class ri_ccap_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Rhode Island Child Care Assistance Program countable income"
    reference = (
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.2",
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3",
    )
    unit = USD
    defined_for = StateCode.RI

    # Per 218-RICR-20-00-4.2(A)(30), gross countable income includes
    # wages, self-employment, Social Security, SSI, dividends, interest,
    # pensions, unemployment, workers' compensation, child support,
    # alimony, veterans' benefits, and other sources.
    adds = [
        "employment_income",
        "self_employment_income",
        "farm_income",
        "social_security",
        "ssi",
        "pension_income",
        "retirement_distributions",
        "military_retirement_pay",
        "unemployment_compensation",
        "workers_compensation",
        "child_support_received",
        "alimony_income",
        "interest_income",
        "dividend_income",
        "rental_income",
        "veterans_benefits",
        "disability_benefits",
        "capital_gains",
        "gi_cash_assistance",
    ]
