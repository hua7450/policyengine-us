from policyengine_us.model_api import *


class RICCAPStepRating(Enum):
    STEP_1 = "Step 1"
    STEP_2 = "Step 2"
    STEP_3 = "Step 3"
    STEP_4 = "Step 4"


class ri_ccap_step_rating(Variable):
    value_type = Enum
    possible_values = RICCAPStepRating
    default_value = RICCAPStepRating.STEP_1
    entity = Person
    label = "Rhode Island CCAP licensed exempt provider step rating"
    definition_period = MONTH
    defined_for = StateCode.RI
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.12"
