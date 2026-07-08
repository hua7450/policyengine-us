from policyengine_us.model_api import *


class ssi_enrolled(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "SSI enrolled"
    documentation = (
        "Whether the person participates in SSI, for programs whose "
        "eligibility depends on SSI receipt. Usually this is whether "
        "the calculated ssi amount is positive. If use_reported_ssi is "
        "True, this follows the receives_ssi flag alone — even when "
        "the calculated ssi amount is zero, and no matter what "
        "reported_ssi_amount says. The ssi variable itself is never "
        "affected; programs that count SSI dollars use applicable_ssi. "
        "Named consistently with tanf_enrolled and snap_enrolled."
    )
    reference = "https://www.law.cornell.edu/uscode/text/42/1382"

    def formula(person, period, parameters):
        use_reported = person("use_reported_ssi", period.this_year)
        receives = person("receives_ssi", period)
        computed = person("ssi", period) > 0
        return where(use_reported, receives, computed)
