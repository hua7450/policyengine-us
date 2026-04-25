from policyengine_us.model_api import *


class wa_eceap_family_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Washington ECEAP family income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=43.216.505",
        "https://app.leg.wa.gov/WAC/default.aspx?cite=110-425-0080",
    )
    adds = [
        "market_income",
        "tanf",
        "ssi",
        "social_security",
        "child_support_received",
        "unemployment_compensation",
        "alimony_income",
        "veterans_benefits",
        "workers_compensation",
    ]
