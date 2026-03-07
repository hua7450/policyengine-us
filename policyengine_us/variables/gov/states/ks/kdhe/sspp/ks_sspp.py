from policyengine_us.model_api import *


class ks_sspp(Variable):
    value_type = float
    entity = Person
    label = "Kansas State Supplemental Payment"
    unit = USD
    definition_period = YEAR
    defined_for = "ks_sspp_eligible"
    reference = (
        "https://ksrevisor.gov/statutes/chapters/ch39/039_009_0072.html",
        "https://khap.kdhe.ks.gov/kfmam/policydocs/state%20supplemental%20payment%20program%20policy%20memo.pdf",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ks.kdhe.sspp.payment.amount
        return p * MONTHS_IN_YEAR
