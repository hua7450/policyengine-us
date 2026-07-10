from policyengine_us.model_api import *


class ORERDCBillingTier(Enum):
    HOURLY = "Hourly"
    PART_TIME = "Part-time"
    MONTHLY = "Monthly"


class or_erdc_billing_tier(Variable):
    value_type = Enum
    entity = Person
    possible_values = ORERDCBillingTier
    default_value = ORERDCBillingTier.HOURLY
    definition_period = MONTH
    label = "Oregon ERDC provider billing tier"
    defined_for = "or_erdc_eligible_child"
    reference = "https://www.oregon.gov/delc/programs/pages/rates.aspx"

    def formula(person, period, parameters):
        p = parameters(period).gov.states["or"].delc.erdc.hours
        hours = person("or_erdc_monthly_care_hours", period)
        provider_type = person("or_erdc_provider_type", period)
        types = provider_type.possible_values
        standard_provider = (provider_type == types.STANDARD_FAMILY) | (
            provider_type == types.STANDARD_CENTER
        )
        return where(
            standard_provider,
            p.standard_tier.calc(hours),
            p.tiered.calc(hours),
        )
