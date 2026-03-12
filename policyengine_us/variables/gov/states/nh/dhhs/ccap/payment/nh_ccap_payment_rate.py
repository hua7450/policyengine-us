from policyengine_us.model_api import *
from policyengine_us.variables.gov.states.nh.dhhs.ccap.nh_ccap_provider_type import (
    NHCCAPProviderType,
)


class nh_ccap_payment_rate(Variable):
    value_type = float
    entity = Person
    unit = USD
    label = "New Hampshire Child Care Scholarship Program weekly payment rate"
    definition_period = MONTH
    defined_for = "nh_ccap_eligible_child"
    reference = "https://www.law.cornell.edu/regulations/new-hampshire/N.H.Code.Admin.R.He-C.6910.17"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.nh.dhhs.ccap.payment
        provider_type = person("nh_ccap_provider_type", period)
        age_category = person("nh_ccap_child_age_category", period)
        service_level = person("nh_ccap_service_level", period)

        licensed_center_rate = p.rates.licensed_center[age_category][service_level]
        licensed_family_rate = p.rates.licensed_family[age_category][service_level]
        # He-C 6910.17(c): exempt in-home = 70% of licensed family rate
        exempt_in_home_rate = licensed_family_rate * p.exempt_in_home_rate
        # He-C 6910.17(d): exempt center = 50% of licensed center rate
        exempt_center_rate = licensed_center_rate * p.exempt_center_rate

        return select(
            [
                provider_type == NHCCAPProviderType.LICENSED_CENTER,
                provider_type == NHCCAPProviderType.LICENSED_FAMILY,
                provider_type == NHCCAPProviderType.LICENSE_EXEMPT_IN_HOME,
            ],
            [
                licensed_center_rate,
                licensed_family_rate,
                exempt_in_home_rate,
            ],
            default=exempt_center_rate,
        )
