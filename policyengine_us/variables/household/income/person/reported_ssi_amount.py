from policyengine_us.model_api import *


class reported_ssi_amount(Variable):
    value_type = float
    entity = Person
    label = "Reported SSI amount"
    unit = USD
    definition_period = YEAR
    documentation = (
        "Amount of Supplemental Security Income the person reports "
        "receiving. API partner input, named consistently with "
        "reported_tanf_amount; it replaces the ssi_reported input, "
        "which earlier package versions read and which remains as a "
        "survey-data variable. Programs only count this amount when "
        "use_reported_ssi is True and receives_ssi marks the person as "
        "a recipient; see applicable_ssi."
    )
