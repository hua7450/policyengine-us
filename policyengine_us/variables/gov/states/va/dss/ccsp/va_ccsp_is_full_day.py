from policyengine_us.model_api import *


class va_ccsp_is_full_day(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    default_value = True
    label = "Virginia CCSP full day care"
    defined_for = StateCode.VA
