from policyengine_us.model_api import *


class ks_sspp_in_medicaid_institution(Variable):
    value_type = bool
    entity = Person
    label = "Whether the person resides in a Kansas Medicaid-approved institution"
    definition_period = YEAR
    defined_for = StateCode.KS
    default_value = False
    reference = (
        "https://ksrevisor.gov/statutes/chapters/ch39/039_009_0072.html",
    )
