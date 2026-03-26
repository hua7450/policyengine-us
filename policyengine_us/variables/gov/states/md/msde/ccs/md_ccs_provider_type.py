from policyengine_us.model_api import *


class MDCCSProviderType(Enum):
    LICENSED_CENTER = "Licensed Child Care Center"
    LICENSED_FAMILY = "Licensed Family Child Care Home"
    INFORMAL = "Informal/License-Exempt"


class md_ccs_provider_type(Variable):
    value_type = Enum
    entity = Person
    possible_values = MDCCSProviderType
    default_value = MDCCSProviderType.LICENSED_CENTER
    definition_period = MONTH
    label = "Maryland CCS child care provider type"
    defined_for = StateCode.MD
    reference = "https://dsd.maryland.gov/regulations/Pages/13A.14.06.11.aspx"
