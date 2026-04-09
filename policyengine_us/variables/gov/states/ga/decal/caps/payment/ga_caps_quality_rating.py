from policyengine_us.model_api import *


class GACAPSQualityRating(Enum):
    ONE_STAR = "1 Star"
    TWO_STAR = "2 Stars"
    THREE_STAR = "3 Stars"
    NONE = "None"


class ga_caps_quality_rating(Variable):
    value_type = Enum
    entity = Person
    possible_values = GACAPSQualityRating
    default_value = GACAPSQualityRating.NONE
    definition_period = MONTH
    label = "Georgia CAPS provider Quality Rated designation"
    defined_for = StateCode.GA
    reference = "https://www.acf.hhs.gov/sites/default/files/documents/occ/georgia_2025_2027_ccdf_state_plan.pdf#page=110"
