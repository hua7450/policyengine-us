from policyengine_us.model_api import *


class ks_sspp_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Whether the person is eligible for Kansas SSPP"
    definition_period = YEAR
    defined_for = StateCode.KS
    reference = (
        "https://ksrevisor.gov/statutes/chapters/ch39/039_009_0072.html",
        "https://khap.kdhe.ks.gov/kfmam/policydocs/state%20supplemental%20payment%20program%20policy%20memo.pdf",
    )

    def formula(person, period, parameters):
        receives_ssi = person("ssi", period) > 0
        in_medicaid_institution = person(
            "ks_sspp_in_medicaid_institution", period
        )
        age = person("age", period)
        return receives_ssi & in_medicaid_institution & (age >= 18)
