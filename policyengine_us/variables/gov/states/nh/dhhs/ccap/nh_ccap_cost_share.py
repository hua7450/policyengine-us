from policyengine_us.model_api import *


class nh_ccap_cost_share(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "New Hampshire Child Care Scholarship Program weekly family cost share"
    definition_period = MONTH
    defined_for = StateCode.NH
    reference = "https://www.law.cornell.edu/regulations/new-hampshire/N.H.Code.Admin.R.He-C.6910.18"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.nh.dhhs.ccap.cost_share
        countable_income = spm_unit("nh_ccap_countable_income", period)
        fpg = spm_unit("spm_unit_fpg", period)
        weeks_per_month = WEEKS_IN_YEAR / MONTHS_IN_YEAR

        # He-C 6910.18, Table 6910.19: stepped cost share
        step_1_threshold = fpg * p.step_1_fpg_rate
        step_2_threshold = fpg * p.step_2_fpg_rate

        step_3_weekly = countable_income * p.step_3_rate / weeks_per_month
        return select(
            [
                countable_income <= step_1_threshold,
                countable_income <= step_2_threshold,
            ],
            [
                0,
                p.step_2_amount,
            ],
            default=step_3_weekly,
        )
