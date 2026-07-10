from policyengine_us.model_api import *


class ORERDCProviderType(Enum):
    STANDARD_FAMILY = "Standard Family (FAM)"
    STANDARD_CENTER = "Standard Center (NQC)"
    ENHANCED_FAMILY = "Enhanced Family (QFM)"
    ENHANCED_CENTER = "Enhanced Center (QEC)"
    REGISTERED_FAMILY = "Registered Family (RFM)"
    CERTIFIED_FAMILY = "Certified Family (CFM)"
    CERTIFIED_CENTER = "Certified Center (CNT)"


class or_erdc_provider_type(Variable):
    value_type = Enum
    entity = Person
    possible_values = ORERDCProviderType
    default_value = ORERDCProviderType.CERTIFIED_CENTER
    definition_period = MONTH
    label = "Oregon ERDC provider type"
    defined_for = StateCode.OR
    reference = "https://www.oregon.gov/delc/programs/pages/rates.aspx"
