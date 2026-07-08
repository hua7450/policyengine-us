from policyengine_us.model_api import *


class applicable_tanf(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    unit = USD
    label = "Applicable TANF for program income tests"
    documentation = (
        "TANF amount to count when another program includes TANF in an "
        "income test. Usually this is the calculated tanf amount. If "
        "use_reported_tanf is True, a positive reported_tanf_amount is "
        "used first. If no positive reported amount is provided but "
        "is_tanf_enrolled is True, this uses the calculated tanf "
        "amount. If neither is provided, this is zero. Programs that "
        "only need TANF receipt use tanf_enrolled instead."
    )

    def formula(spm_unit, period, parameters):
        use_reported = spm_unit("use_reported_tanf", period.this_year)
        reported = spm_unit("reported_tanf_amount", period)
        enrolled = spm_unit("is_tanf_enrolled", period)
        computed = spm_unit("tanf", period)
        reported_value = where(reported > 0, reported, enrolled * computed)
        return where(use_reported, reported_value, computed)
