from policyengine_us.model_api import *


class co_sales_tax_refund_person_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible individual for the Colorado sales tax refund"
    definition_period = YEAR
    reference = "https://tax.colorado.gov/sites/tax/files/documents/DR_0104_Book_2022.pdf#page=23"
    defined_for = StateCode.CO

    def formula(person, period, parameters):
        p = parameters(period).gov.states.co.tax.income.credits.sales_tax_refund
        # Only the head and spouse can be eligible filers (not dependents).
        is_filer = person("is_tax_unit_head", period) | person(
            "is_tax_unit_spouse", period
        )
        age_eligible = person("age", period) >= p.age_threshold
        # Filers that had Colorado tax withheld are also eligible; use employment
        # income as a proxy.
        employment_income_eligible = person("irs_employment_income", period) > 0
        # A positive Colorado income tax liability qualifies the tax unit's filers.
        # The liability is a tax-unit value that cannot be split between spouses,
        # so a paying joint unit qualifies both filers.
        tax_unit = person.tax_unit
        income_tax_eligible = (
            tax_unit("co_income_tax_before_non_refundable_credits", period) > 0
        )
        return is_filer & (
            age_eligible | employment_income_eligible | income_tax_eligible
        )
