from policyengine_us.model_api import *


class ORERDCProviderArea(Enum):
    AREA_A = "Area A"
    AREA_B = "Area B"
    AREA_C = "Area C"


class or_erdc_provider_area(Variable):
    value_type = Enum
    entity = Person
    possible_values = ORERDCProviderArea
    default_value = ORERDCProviderArea.AREA_C
    definition_period = MONTH
    label = "Oregon ERDC provider rate area"
    documentation = "Area C is the conservative default until provider ZIP code mapping is implemented."
    defined_for = StateCode.OR
    reference = "https://www.oregon.gov/delc/programs/pages/rates.aspx"
