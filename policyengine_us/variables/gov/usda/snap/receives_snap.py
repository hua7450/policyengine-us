from policyengine_us.model_api import *


class receives_snap(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = YEAR
    default_value = False
    label = "Whether this SPM unit currently receives SNAP"
