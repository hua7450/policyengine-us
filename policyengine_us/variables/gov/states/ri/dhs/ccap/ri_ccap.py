from policyengine_us.model_api import *


class ri_ccap(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Rhode Island Child Care Assistance Program (CCAP)"
    definition_period = MONTH
    reference = (
        "https://dhs.ri.gov/media/9236/download?language=en#page=30",
        "https://dhs.ri.gov/media/9236/download?language=en#page=63",
    )
    defined_for = "ri_ccap_eligible"

    def formula(spm_unit, period, parameters):
        total_weekly_benefit = add(
            spm_unit, period, ["ri_ccap_weekly_benefit"]
        )
        return total_weekly_benefit * WEEKS_IN_YEAR / MONTHS_IN_YEAR
