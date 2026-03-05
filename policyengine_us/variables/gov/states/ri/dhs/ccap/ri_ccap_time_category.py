from policyengine_us.model_api import *


class RICCAPTimeCategory(Enum):
    FULL_TIME = "Full-time (30+ hours/week)"
    THREE_QUARTER_TIME = "Three-quarter time (20-29 hours/week)"
    HALF_TIME = "Half-time (10-19 hours/week)"
    QUARTER_TIME = "Quarter-time (less than 10 hours/week)"


class ri_ccap_time_category(Variable):
    value_type = Enum
    possible_values = RICCAPTimeCategory
    default_value = RICCAPTimeCategory.FULL_TIME
    entity = Person
    label = "Rhode Island CCAP time authorization category"
    definition_period = MONTH
    defined_for = StateCode.RI
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.12"
