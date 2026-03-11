from policyengine_us.model_api import *
from policyengine_us.variables.gov.states.me.dhhs.ccap.payment.me_ccap_provider_type import (
    MECCAPProviderType,
)


class me_ccap_market_rate(Variable):
    value_type = float
    entity = Person
    label = "Maine CCAP weekly market rate per child"
    unit = USD
    definition_period = MONTH
    defined_for = "me_ccap_eligible_child"
    reference = "https://www.maine.gov/sos/cec/rules/10/ch6.pdf#page=12"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.me.dhhs.ccap.market_rate
        region = person.household("me_ccap_region", period)
        age_group = person("me_ccap_age_group", period)
        time_category = person("me_ccap_time_category", period)
        provider_type = person("me_ccap_provider_type", period)

        center_rate = p.licensed_center[region][age_group][time_category]
        family_rate = p.licensed_family[region][age_group][time_category]
        exempt_rate = p.license_exempt[region][age_group][time_category]

        return select(
            [
                provider_type == MECCAPProviderType.LICENSED_CENTER,
                provider_type == MECCAPProviderType.LICENSED_FAMILY,
                provider_type == MECCAPProviderType.LICENSE_EXEMPT,
            ],
            [
                center_rate,
                family_rate,
                exempt_rate,
            ],
            default=center_rate,
        )
