from policyengine_us.model_api import *


class applicable_snap(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    unit = USD
    label = "Applicable SNAP for program income tests"
    documentation = (
        "SNAP amount to use when another program counts SNAP benefits as "
        "income. Usually this is the calculated snap amount. If "
        "use_reported_snap is True, a positive reported_snap_amount is "
        "used first. If no positive reported amount is provided but "
        "receives_snap is True, this uses the calculated snap amount. "
        "If neither is provided, this is zero."
    )

    def formula(spm_unit, period, parameters):
        use_reported = spm_unit("use_reported_snap", period.this_year)
        reported = spm_unit("reported_snap_amount", period)
        enrolled = spm_unit("receives_snap", period)
        computed = spm_unit("snap", period)
        reported_value = where(reported > 0, reported, enrolled * computed)
        return where(use_reported, reported_value, computed)
