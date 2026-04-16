from policyengine_us.model_api import *


class ky_ssp_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Kentucky State Supplementary Payment"
    definition_period = YEAR
    defined_for = StateCode.KY
    reference = (
        "https://apps.legislature.ky.gov/law/kar/titles/921/002/015/",
        "https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=46358",
    )

    def formula(person, period, parameters):
        categorically_eligible = person("is_ssi_eligible", period)
        # Per CLAUDE.md, use uncapped_ssi > 0 to confirm actual SSI receipt
        # (income low enough for a positive federal benefit).
        receives_ssi = person("uncapped_ssi", period) > 0
        category = person.household("ky_ssp_category", period)
        in_qualifying_category = category != category.possible_values.NONE
        return categorically_eligible & receives_ssi & in_qualifying_category
