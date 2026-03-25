from policyengine_us.model_api import *
from policyengine_us.variables.gov.states.de.dss.poc.de_poc_provider_type import (
    DEPOCProviderType,
)


class de_poc_maximum_weekly_benefit(Variable):
    value_type = float
    entity = Person
    unit = USD
    label = "Delaware Purchase of Care maximum weekly benefit per child"
    definition_period = MONTH
    defined_for = "de_poc_eligible_child"
    reference = (
        "https://www.dhss.delaware.gov/dhss/dss/files/pocbillingguidance.pdf#page=2",
        "https://www.dhss.delaware.gov/dhss/dss/childcare.html",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.de.dss.poc.rates
        provider_type = person("de_poc_provider_type", period)
        age_group = person("de_poc_age_group", period)
        base_rate = where(
            provider_type == DEPOCProviderType.CENTER,
            p.center[age_group],
            p.family_home[age_group],
        )
        return where(
            person("is_disabled", period.this_year),
            base_rate * (1 + p.special_needs_rate_increase),
            base_rate,
        )
