from policyengine_us.model_api import *


class wv_ccap_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for West Virginia CCAP based on income"
    definition_period = MONTH
    defined_for = StateCode.WV
    reference = (
        "https://bfa.wv.gov/media/6766/download?inline#page=49",
        "https://bfa.wv.gov/media/39915/download?inline#page=20",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.wv.dhhr.ccap.income
        countable_income = spm_unit("wv_ccap_countable_income", period)
        fpg = spm_unit("spm_unit_fpg", period)
        enrolled = spm_unit("wv_ccap_enrolled", period)
        is_tanf = spm_unit("is_tanf_enrolled", period)
        fpl_rate = where(enrolled, p.fpl_limit.ongoing, p.fpl_limit.initial)
        fpl_limit = fpg * fpl_rate
        smi = spm_unit("hhs_smi", period)
        smi_limit = smi * p.smi_rate
        return is_tanf | (
            (countable_income <= fpl_limit) & (countable_income <= smi_limit)
        )
