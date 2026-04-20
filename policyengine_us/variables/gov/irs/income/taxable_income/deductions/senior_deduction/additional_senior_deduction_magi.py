from policyengine_us.model_api import *


class additional_senior_deduction_magi(Variable):
    value_type = float
    entity = TaxUnit
    label = "Modified adjusted gross income for the senior deduction"
    unit = USD
    definition_period = YEAR
    reference = "https://www.congress.gov/bill/119th-congress/house-bill/1/text"

    def formula(tax_unit, period, parameters):
        agi = tax_unit("adjusted_gross_income", period)
        excluded_income = add(
            tax_unit,
            period,
            [
                "foreign_earned_income_exclusion",
                "specified_possession_income",
                "puerto_rico_income",
            ],
        )
        return agi + excluded_income
