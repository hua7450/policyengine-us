from policyengine_us.model_api import *


class WYCCAPProviderType(Enum):
    CENTER = "Child care center"
    LICENSED_FAMILY = "Licensed family setting"
    LEGALLY_EXEMPT = "Legally exempt provider"


class wy_ccap_provider_type(Variable):
    value_type = Enum
    entity = Person
    possible_values = WYCCAPProviderType
    default_value = WYCCAPProviderType.CENTER
    definition_period = MONTH
    defined_for = StateCode.WY
    label = "Wyoming CCAP child care provider type"
    reference = (
        "https://drive.google.com/file/d/1yatL28Yylj62R2cTipV2sGa10TxZplxr/view",  # Wyo. Admin. Rules, DFS, Child Care - Purchase of Service, Ch. 1 §14, eff. 05/07/2025 (PDF p. 29)
        "https://drive.google.com/file/d/1T7NWbz6hOlRyAcqwROXExos5JB57NstB/view",  # Wyoming DFS Table I - Child Care Sliding Fee Scale, eff. 04/01/25-03/31/26 (single page)
    )
    # Table I rate columns: the licensed family setting covers family child
    # care homes and family child care centers; legally exempt covers
    # unlicensed relative and non-relative care. University, community
    # college, and Wind River Reservation centers receive the center rate
    # (Manual §1203.G).
