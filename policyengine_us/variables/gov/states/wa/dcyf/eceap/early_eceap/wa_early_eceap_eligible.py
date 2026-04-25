from policyengine_us.model_api import *


class wa_early_eceap_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Washington Early ECEAP"
    definition_period = YEAR
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=43.216.505",
        "https://www.startearly.org/app/uploads/2021/06/Final-Summary-of-Fair-Start-for-Kids-Act.pdf#page=9",
    )

    def formula(person, period, parameters):
        age_eligible = person("wa_early_eceap_age_eligible", period)
        income_eligible = person("wa_early_eceap_income_eligible", period)
        categorically_eligible = person("wa_eceap_categorically_eligible", period)
        return age_eligible & (income_eligible | categorically_eligible)
