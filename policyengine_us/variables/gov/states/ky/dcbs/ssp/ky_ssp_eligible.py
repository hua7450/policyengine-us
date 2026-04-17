from policyengine_us.model_api import *


class ky_ssp_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Kentucky State Supplementary Payment"
    definition_period = YEAR
    defined_for = StateCode.KY
    reference = (
        "https://apps.legislature.ky.gov/law/kar/titles/921/002/015/",
        "https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=7671",
    )

    def formula(person, period, parameters):
        categorically_eligible = person("is_ssi_eligible", period)
        # 921 KAR 2:015 §4(1)(c) — age ≥ 18 required for all four categories.
        is_adult = person("age", period) >= 18
        category = person.household("ky_ssp_category", period)
        in_qualifying_category = category != category.possible_values.NONE
        # 921 KAR 2:015 §4(1)(b) — insufficient income to meet the standard in §9.
        countable_income = person("ssi_countable_income", period)
        payment_standard = person("ky_ssp_payment_standard", period)
        income_below_standard = countable_income < payment_standard
        return (
            categorically_eligible
            & is_adult
            & in_qualifying_category
            & income_below_standard
        )
