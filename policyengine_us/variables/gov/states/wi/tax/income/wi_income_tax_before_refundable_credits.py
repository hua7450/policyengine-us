from policyengine_us.model_api import *


class wi_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Wisconsin income tax before refundable credits"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.revenue.wi.gov/TaxForms2021/2021-Form1f.pdf",
        "https://www.revenue.wi.gov/TaxForms2021/2021-Form1-Inst.pdf",
        "https://www.revenue.wi.gov/TaxForms2022/2022-Form1f.pdf",
        "https://www.revenue.wi.gov/TaxForms2022/2022-Form1-Inst.pdf",
        "https://docs.legis.wisconsin.gov/misc/lfb/informational_papers/january_2023/0002_individual_income_tax_informational_paper_2.pdf",
        "https://docs.legis.wisconsin.gov/statutes/statutes/71/i/05/6/b/54m/a",
    )
    defined_for = StateCode.WI

    def formula(tax_unit, period, parameters):
        income_tax_before = tax_unit("wi_income_tax_before_credits", period)
        nonrefundable_credits = tax_unit("wi_non_refundable_credits", period)
        standard = max_(0, income_tax_before - nonrefundable_credits)
        # Wisconsin retirement income exclusion (Schedule SB Line 16):
        # The final tax is the lesser of the standard path (with credits)
        # and the exclusion path (no credits). Since state_income_tax
        # decomposes as before_refundable - refundable, we adjust here so
        # that: min(standard, exclusion + refundable) - refundable
        #      = min(standard - refundable, exclusion) = wi_income_tax
        p = parameters(
            period
        ).gov.states.wi.tax.income.subtractions.retirement_income.exclusion
        if not p.in_effect:
            return standard
        exclusion_tax = tax_unit("wi_retirement_income_exclusion_tax", period)
        refundable = tax_unit("wi_refundable_credits", period)
        return min_(standard, exclusion_tax + refundable)
