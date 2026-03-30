from policyengine_us.model_api import *


class head_start_use_reported_programs(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    default_value = False
    label = "Use reported program receipt for Head Start categorical eligibility"
