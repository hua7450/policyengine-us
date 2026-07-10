from policyengine_us.model_api import *


class ORERDCTieredProviderType(Enum):
    ENHANCED_FAMILY = "Enhanced Family (QFM)"
    ENHANCED_CENTER = "Enhanced Center (QEC)"
    REGISTERED_FAMILY = "Registered Family (RFM)"
    CERTIFIED_FAMILY = "Certified Family (CFM)"
    CERTIFIED_CENTER = "Certified Center (CNT)"


class or_erdc_tiered_provider_type(Variable):
    value_type = Enum
    entity = Person
    possible_values = ORERDCTieredProviderType
    default_value = ORERDCTieredProviderType.ENHANCED_FAMILY
    definition_period = MONTH
    label = "Oregon ERDC enhanced or licensed provider type"
    defined_for = "or_erdc_eligible_child"
    reference = "https://www.oregon.gov/delc/programs/pages/rates.aspx"

    def formula(person, period, parameters):
        provider_type = person("or_erdc_provider_type", period)
        types = provider_type.possible_values
        return select(
            [
                provider_type == types.ENHANCED_FAMILY,
                provider_type == types.ENHANCED_CENTER,
                provider_type == types.REGISTERED_FAMILY,
                provider_type == types.CERTIFIED_FAMILY,
                provider_type == types.CERTIFIED_CENTER,
            ],
            [
                ORERDCTieredProviderType.ENHANCED_FAMILY,
                ORERDCTieredProviderType.ENHANCED_CENTER,
                ORERDCTieredProviderType.REGISTERED_FAMILY,
                ORERDCTieredProviderType.CERTIFIED_FAMILY,
                ORERDCTieredProviderType.CERTIFIED_CENTER,
            ],
            default=ORERDCTieredProviderType.ENHANCED_FAMILY,
        )
