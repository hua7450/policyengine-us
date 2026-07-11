from policyengine_us.model_api import *


class ORERDCProviderArea(Enum):
    AREA_A = "Area A"
    AREA_B = "Area B"
    AREA_C = "Area C"


class or_erdc_provider_area(Variable):
    value_type = Enum
    entity = Person
    possible_values = ORERDCProviderArea
    # Area C is the conservative (lowest-rate) default until provider ZIP code
    # mapping is implemented. In population runs this understates rates on its
    # own, partly offsetting the highest-rate CERTIFIED_CENTER provider-type
    # default; the remedy is populating provider area from data, not changing
    # this default.
    default_value = ORERDCProviderArea.AREA_C
    definition_period = MONTH
    label = "Oregon ERDC provider rate area"
    defined_for = StateCode.OR
    reference = "https://www.oregon.gov/delc/programs/pages/rates.aspx"
