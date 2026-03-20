from policyengine_us.model_api import *


class ReportedHealthCoverageAtInterview:
    value_type = bool
    entity = Person
    definition_period = YEAR
    default_value = False


class reported_has_direct_purchase_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported direct-purchase health coverage at interview"


class reported_has_marketplace_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported Marketplace health coverage at interview"


class reported_has_subsidized_marketplace_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported subsidized Marketplace health coverage at interview"


class reported_has_unsubsidized_marketplace_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported unsubsidized Marketplace health coverage at interview"


class reported_has_non_marketplace_direct_purchase_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported non-Marketplace direct-purchase health coverage at interview"


class reported_has_employer_sponsored_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported employer-sponsored health coverage at interview"


class reported_has_medicare_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported Medicare health coverage at interview"


class reported_has_medicaid_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported Medicaid health coverage at interview"


class reported_has_means_tested_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported means-tested health coverage at interview"


class reported_has_chip_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported CHIP health coverage at interview"


class reported_has_other_means_tested_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported other means-tested health coverage at interview"


class reported_has_tricare_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported TRICARE health coverage at interview"


class reported_has_champva_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported CHAMPVA health coverage at interview"


class reported_has_va_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported VA health coverage at interview"


class reported_has_indian_health_service_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported Indian Health Service coverage at interview"


class reported_has_private_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported private health coverage at interview"


class reported_has_public_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported public health coverage at interview"


class reported_is_insured_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported insured at interview"


class reported_is_uninsured_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported uninsured at interview"


class reported_has_multiple_health_coverage_at_interview(
    ReportedHealthCoverageAtInterview, Variable
):
    label = "Reported multiple health coverage types at interview"
