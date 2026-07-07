from policyengine_us.model_api import *


class applicable_tanf(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = YEAR
    unit = USD
    label = "Applicable TANF for program income tests"
    documentation = (
        "TANF amount that programs count in income tests and receipt "
        "checks. By default this equals the calculated tanf, so "
        "microsimulation results are unchanged. When an API partner "
        "sets use_reported_tanf to True, it resolves in order: (1) a "
        "positive tanf_reported amount is used as given; (2) otherwise, "
        "if is_tanf_enrolled is True, the calculated tanf is used; (3) "
        "otherwise the household is treated as receiving no TANF and "
        "this is zero."
    )

    def formula(spm_unit, period, parameters):
        use_reported = spm_unit("use_reported_tanf", period)
        reported = spm_unit("tanf_reported", period)
        enrolled = spm_unit("is_tanf_enrolled", period.first_month)
        computed = spm_unit("tanf", period)
        reported_value = where(reported > 0, reported, enrolled * computed)
        return where(use_reported, reported_value, computed)
