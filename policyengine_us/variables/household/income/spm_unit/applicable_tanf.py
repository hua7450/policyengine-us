from policyengine_us.model_api import *


class applicable_tanf(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = YEAR
    unit = USD
    label = "Applicable TANF for program income tests"
    documentation = (
        "TANF amount counted in program income tests. Uses calculated "
        "tanf by default. When use_reported_tanf is True, uses "
        "tanf_reported if positive, calculated tanf if is_tanf_enrolled "
        "is True, and zero otherwise."
    )

    def formula(spm_unit, period, parameters):
        use_reported = spm_unit("use_reported_tanf", period)
        reported = spm_unit("tanf_reported", period)
        enrolled = spm_unit("is_tanf_enrolled", period.first_month)
        computed = spm_unit("tanf", period)
        reported_value = where(reported > 0, reported, enrolled * computed)
        return where(use_reported, reported_value, computed)
