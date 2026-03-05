from policyengine_us.model_api import *


class ri_ccap_per_child_weekly_payment(Variable):
    value_type = float
    entity = Person
    label = "Rhode Island CCAP per-child weekly payment before copayment"
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.RI
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.12"

    def formula(person, period, parameters):
        is_eligible_child = person("ri_ccap_child_eligible", period)
        provider_rate = person("ri_ccap_provider_rate", period)
        annual_expenses = person(
            "pre_subsidy_childcare_expenses", period.this_year
        )
        weekly_expenses = annual_expenses / WEEKS_IN_YEAR
        # DHS pays lesser of actual charge or established rate
        weekly_payment = min_(provider_rate, weekly_expenses)
        return weekly_payment * is_eligible_child
