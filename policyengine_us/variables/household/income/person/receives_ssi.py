from policyengine_us.model_api import *


class receives_ssi(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = "Receives SSI"
    documentation = (
        "Whether the person currently receives Supplemental Security "
        "Income. API partner input, named consistently with "
        "receives_snap and receives_tanf. When use_reported_ssi is "
        "True, this flag decides participation: applicable_ssi is zero "
        "without it, regardless of any reported amount."
    )
