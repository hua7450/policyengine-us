from policyengine_us.model_api import *


class wa_early_eceap_age_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Age-eligible for Washington Early ECEAP"
    definition_period = YEAR
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=43.216.505",
        "https://www.startearly.org/app/uploads/2021/06/Final-Summary-of-Fair-Start-for-Kids-Act.pdf#page=9",
    )

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(period).gov.states.wa.dcyf.eceap.early_eceap.eligibility
        return age < p.age_limit
