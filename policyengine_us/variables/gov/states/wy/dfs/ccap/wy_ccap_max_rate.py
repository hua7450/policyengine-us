from policyengine_us.model_api import *
from policyengine_us.variables.gov.states.wy.dfs.ccap.wy_ccap_provider_type import (
    WYCCAPProviderType,
)


class wy_ccap_max_rate(Variable):
    value_type = float
    entity = Person
    unit = USD
    label = "Wyoming CCAP maximum daily reimbursement rate"
    definition_period = MONTH
    defined_for = "wy_ccap_eligible_child"
    reference = (
        "https://drive.google.com/file/d/1T7NWbz6hOlRyAcqwROXExos5JB57NstB/view",  # Wyoming DFS Table I - Child Care Sliding Fee Scale, eff. 04/01/25-03/31/26 (single page)
        "https://drive.google.com/file/d/1yatL28Yylj62R2cTipV2sGa10TxZplxr/view",  # Wyo. Admin. Rules, DFS, Child Care - Purchase of Service, Ch. 1 §9(c), eff. 05/07/2025 (PDF p. 23)
    )

    def formula(person, period, parameters):
        # Table I: the DFS maximum daily rate is keyed by facility type, the
        # child's age band, and part- or full-day care; the legally exempt
        # rate is flat across age bands.
        p = parameters(period).gov.states.wy.dfs.ccap.rates
        provider_type = person("wy_ccap_provider_type", period)
        age_band = person("wy_ccap_age_band", period)
        day_length = person("wy_ccap_day_length", period)
        types = WYCCAPProviderType
        return select(
            [
                provider_type == types.CENTER,
                provider_type == types.LICENSED_FAMILY,
                provider_type == types.LEGALLY_EXEMPT,
            ],
            [
                p.center[age_band][day_length],
                p.licensed_family[age_band][day_length],
                p.legally_exempt[day_length],
            ],
        )
