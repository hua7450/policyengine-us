from policyengine_us.model_api import *


class RICCAPStarRating(Enum):
    STAR_1 = "BrightStars Star 1"
    STAR_2 = "BrightStars Star 2"
    STAR_3 = "BrightStars Star 3"
    STAR_4 = "BrightStars Star 4"
    STAR_5 = "BrightStars Star 5"


class ri_ccap_star_rating(Variable):
    value_type = Enum
    possible_values = RICCAPStarRating
    default_value = RICCAPStarRating.STAR_1
    entity = Person
    label = "Rhode Island CCAP provider BrightStars quality rating"
    definition_period = MONTH
    defined_for = StateCode.RI
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.12"
