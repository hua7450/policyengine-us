from policyengine_us.model_api import *


class wa_sfa_immigration_status_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Washington State Family Assistance immigration status eligible"
    definition_period = MONTH
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/wac/default.aspx?cite=388-400-0010",
        "https://app.leg.wa.gov/wac/default.aspx?cite=388-424-0015",
        "https://app.leg.wa.gov/rcw/default.aspx?cite=74.08A.010",
    )

    def formula(person, period, parameters):
        is_qualified = person("is_citizen_or_legal_immigrant", period.this_year)
        tanf_immigration_eligible = person(
            "wa_tanf_immigration_status_eligible", period
        )
        return is_qualified & ~tanf_immigration_eligible
