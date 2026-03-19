from policyengine_us.model_api import *


class nj_ccap_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for New Jersey CCAP based on income"
    definition_period = MONTH
    defined_for = StateCode.NJ
    reference = (
        "https://www.childcarenj.gov/ChildCareNJ/media/media_library/Income_Eligibility_Schedule.pdf",
        "https://www.childcarenj.gov/ChildCareNJ/media/media_library/CCDF_State_Plan_for_New_Jersey_FFY25-27.pdf#page=23",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.nj.njdhs.ccap.income.fpl_rate
        countable_income = spm_unit("nj_ccap_countable_income", period)
        fpg = spm_unit("spm_unit_fpg", period)
        enrolled = spm_unit("nj_ccap_enrolled", period)
        initial_limit = fpg * p.initial_eligibility
        continuing_limit = fpg * p.continuing_eligibility
        fpl_limit = where(enrolled, continuing_limit, initial_limit)
        smi = spm_unit("nj_ccap_smi", period)
        return (countable_income <= fpl_limit) & (countable_income <= smi)
