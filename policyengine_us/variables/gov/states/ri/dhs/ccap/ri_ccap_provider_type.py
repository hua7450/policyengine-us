from policyengine_us.model_api import *


class RICCAPProviderType(Enum):
    LICENSED_CENTER = "Licensed child care center"
    LICENSED_FAMILY = "Licensed family child care"
    LICENSED_EXEMPT = "Licensed exempt child care"


class ri_ccap_provider_type(Variable):
    value_type = Enum
    possible_values = RICCAPProviderType
    default_value = RICCAPProviderType.LICENSED_CENTER
    entity = Person
    label = "Rhode Island CCAP child care provider type"
    definition_period = MONTH
    defined_for = StateCode.RI
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.12"
