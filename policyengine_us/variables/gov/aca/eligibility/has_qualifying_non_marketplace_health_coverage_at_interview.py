from policyengine_us.model_api import *


class has_qualifying_non_marketplace_health_coverage_at_interview(Variable):
    value_type = bool
    entity = Person
    label = "Person has qualifying non-Marketplace health coverage at interview"
    definition_period = YEAR

    def formula(person, period, parameters):
        return (
            add(
                person,
                period,
                [
                    "has_esi",
                    "medicaid_enrolled",
                    "is_chip_eligible",
                    "medicare_enrolled",
                    "reported_has_non_marketplace_direct_purchase_health_coverage_at_interview",
                    "reported_has_other_means_tested_health_coverage_at_interview",
                    "reported_has_tricare_health_coverage_at_interview",
                    "reported_has_champva_health_coverage_at_interview",
                    "reported_has_va_health_coverage_at_interview",
                ],
            )
            > 0
        )
