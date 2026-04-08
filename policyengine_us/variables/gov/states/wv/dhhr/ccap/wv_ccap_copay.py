from policyengine_us.model_api import *


class wv_ccap_copay(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "West Virginia CCAP family co-payment"
    definition_period = MONTH
    defined_for = StateCode.WV
    reference = (
        "https://bfa.wv.gov/media/6826/download?inline",
        "https://bfa.wv.gov/media/39915/download?inline#page=42",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.wv.dhhr.ccap.copayment
        countable_income = spm_unit("wv_ccap_countable_income", period)
        fpg = spm_unit("spm_unit_fpg", period)
        mask = fpg > 0
        fpl_ratio = np.divide(
            countable_income,
            fpg,
            out=np.zeros_like(countable_income, dtype=float),
            where=mask,
        )
        has_foster_child = add(spm_unit, period, ["is_in_foster_care"]) > 0
        copay_rate = p.rate.calc(fpl_ratio)
        uncapped_copay = countable_income * copay_rate
        capped_copay = min_(uncapped_copay, countable_income * p.max_share)
        return where(has_foster_child, 0, capped_copay)
