from policyengine_us.model_api import *


class RICCAPProviderType(Enum):
    CENTER = "Licensed Center"
    FAMILY = "Licensed Family"
    EXEMPT = "License Exempt"


class ri_ccap_provider_type(Variable):
    value_type = Enum
    possible_values = RICCAPProviderType
    default_value = RICCAPProviderType.CENTER
    entity = Person
    label = "Rhode Island CCAP child care provider type"
    definition_period = YEAR
    reference = "https://dhs.ri.gov/media/9236/download?language=en#page=63"
    defined_for = StateCode.RI
