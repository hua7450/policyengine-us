from policyengine_us.model_api import *


class wa_eceap_eligible(Variable):
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
        # The Indian-child pathway under RCW 43.216.505 (income up to 100% SMI
        # for tribal children, entitlement starts 2026-07-01) is not modeled
        # because we don't track tribal enrollment at the moment. is_on_tribal_land
        # is a geographic household flag, not enrollment in a federally recognized
        # tribe, so it is not an acceptable proxy.
        age_eligible = person("wa_eceap_age_eligible", period)
        income_eligible = person("wa_eceap_income_eligible", period)
        categorically_eligible = person("wa_eceap_categorically_eligible", period)
        risk_factor_eligible = person("wa_eceap_risk_factor_eligible", period)
        return age_eligible & (
            income_eligible | categorically_eligible | risk_factor_eligible
        )
