from policyengine_us.model_api import *


class receives_tanf(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    default_value = False
    label = "Whether this person currently receives TANF"
