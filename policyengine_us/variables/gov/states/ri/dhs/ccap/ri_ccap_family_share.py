from policyengine_us.model_api import *


class ri_ccap_family_share(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Rhode Island CCAP weekly family share (co-payment)"
    definition_period = MONTH
    reference = (
        "https://dhs.ri.gov/media/9236/download?language=en#page=30",
        "https://dhs.ri.gov/media/9236/download?language=en#page=25",
    )
    defined_for = StateCode.RI

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap
        ri_works = spm_unit("ri_works_eligible", period)
        housing_insecure = spm_unit.household("is_homeless", period.this_year)
        zero_copay = ri_works | housing_insecure
        countable_income = spm_unit("ri_ccap_countable_income", period)
        fpg = spm_unit("spm_unit_fpg", period)
        fpl_ratio = np.divide(
            countable_income,
            fpg,
            out=np.zeros_like(countable_income),
            where=fpg > 0,
        )
        share_rate = p.family_share.rates.calc(fpl_ratio)
        weekly_income = countable_income * MONTHS_IN_YEAR / WEEKS_IN_YEAR
        weekly_share = weekly_income * share_rate
        return where(zero_copay, 0, weekly_share)
