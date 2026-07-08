from policyengine_us.model_api import *


class applicable_tanf(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    unit = USD
    label = "Applicable TANF for program income tests"
    documentation = (
        "TANF amount to count when another program includes TANF in an "
        "income test. Usually this is the calculated tanf amount. When "
        "use_reported_tanf is True, the is_tanf_enrolled flag decides "
        "participation: zero without it; with it, a positive "
        "reported_tanf_amount if provided, the calculated tanf amount "
        "otherwise. Programs that only need TANF receipt use "
        "tanf_enrolled instead."
    )

    def formula(spm_unit, period, parameters):
        use_reported = spm_unit("use_reported_tanf", period.this_year)
        reported = spm_unit("reported_tanf_amount", period)
        enrolled = spm_unit("is_tanf_enrolled", period)
        computed = spm_unit("tanf", period)
        reported_value = enrolled * where(reported > 0, reported, computed)
        return where(use_reported, reported_value, computed)
