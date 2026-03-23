from policyengine_us.model_api import *


class pa_ccw_copay(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Pennsylvania CCW family copayment"
    definition_period = MONTH
    defined_for = StateCode.PA
    reference = "https://www.pacodeandbulletin.gov/secure/pacode/data/055/chapter3042/055_3042.pdf#page=34"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.pa.dhs.ccw.copay
        adjusted_income = spm_unit("pa_ccw_adjusted_income", period.this_year)
        fpg = spm_unit("spm_unit_fpg", period.this_year)
        is_homeless = spm_unit.household("is_homeless", period.this_year)

        low_income = adjusted_income <= fpg * p.low_income_threshold
        rate = where(low_income, p.low_income_max_rate, p.max_rate)
        weekly_copay = max_(round_(adjusted_income * rate / WEEKS_IN_YEAR), p.minimum)
        weekly_copay = where(is_homeless, 0, weekly_copay)
        return weekly_copay * WEEKS_IN_YEAR / MONTHS_IN_YEAR
