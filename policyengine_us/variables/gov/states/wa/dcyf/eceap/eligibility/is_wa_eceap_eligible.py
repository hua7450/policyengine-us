from policyengine_us.model_api import *


class is_wa_eceap_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Washington ECEAP"
    definition_period = YEAR
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=43.216.505",
        "https://app.leg.wa.gov/RCW/default.aspx?cite=43.216.512",
        "https://app.leg.wa.gov/WAC/default.aspx?cite=110-425-0080",
    )

    def formula(person, period, parameters):
        age_eligible = person("is_wa_eceap_age_eligible", period)
        income_eligible = person("is_wa_eceap_income_eligible", period)
        categorically_eligible = person("is_wa_eceap_categorically_eligible", period)
        risk_factor_eligible = person("is_wa_eceap_risk_factor_eligible", period)
        return age_eligible & (
            income_eligible | categorically_eligible | risk_factor_eligible
        )
