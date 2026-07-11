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
    reference = (
        "https://secure.sos.state.or.us/oard/view.action?ruleNumber=414-175-0075"
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states["or"].delc.erdc.hours
        hours = person("or_erdc_monthly_care_hours", period)
        provider_type = person("or_erdc_provider_type", period)
        types = provider_type.possible_values
        standard_provider = (provider_type == types.STANDARD_FAMILY) | (
            provider_type == types.STANDARD_CENTER
        )
        # OAR 414-175-0075(3)(b),(c),(e): an enhanced or licensed provider is
        # paid the part-time monthly rate below the full-time threshold only
        # when it customarily bills all families part-time and is the primary
        # provider; otherwise that care is paid hourly. When the provider does
        # not bill part-time, collapse the part-time band into the hourly tier.
        bills_part_time = person("or_erdc_provider_bills_part_time", period)
        tiered = p.tiered.calc(hours)
        tiered_without_part_time = where(
            tiered == ORERDCBillingTier.PART_TIME.index,
            ORERDCBillingTier.HOURLY.index,
            tiered,
        )
        enhanced_tier = where(bills_part_time, tiered, tiered_without_part_time)
        return where(
            standard_provider,
            p.standard_tier.calc(hours),
            enhanced_tier,
        )
