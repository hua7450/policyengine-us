from policyengine_us.model_api import *


class ri_ccap_quality_rating(Variable):
    value_type = int
    entity = Person
    label = "Rhode Island CCAP child care provider QRIS star rating"
    definition_period = YEAR
    reference = "https://dhs.ri.gov/media/9236/download?language=en#page=63"
    defined_for = StateCode.RI
