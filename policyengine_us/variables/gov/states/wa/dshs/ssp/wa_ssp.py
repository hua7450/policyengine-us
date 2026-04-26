from policyengine_us.model_api import *


class wa_ssp(Variable):
    value_type = float
    entity = Person
    label = "Washington State Supplementary Payment"
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/wac/default.aspx?cite=388-478-0055",
        "https://app.leg.wa.gov/wac/default.aspx?cite=388-474-0012",
    )

    def formula(person, period, parameters):
        category = person("wa_ssp_payment_category", period)
        return parameters(period).gov.states.wa.dshs.ssp.amount[category]
