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
    # CERTIFIED_CENTER (CNT) is the highest-rate provider type, so as a
    # population default it biases modeled rates upward; it partly offsets the
    # lowest-rate AREA_C area default. The remedy is populating provider type
    # from data, not changing this default.
    default_value = ORERDCProviderType.CERTIFIED_CENTER
    definition_period = MONTH
    label = "Oregon ERDC provider type"
    defined_for = StateCode.OR
    reference = "https://www.oregon.gov/delc/programs/pages/rates.aspx"
