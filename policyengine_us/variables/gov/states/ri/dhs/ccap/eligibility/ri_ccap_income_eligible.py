from policyengine_us.model_api import *


class ri_ccap_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = (
        "Income eligible for the Rhode Island Child Care Assistance Program"
    )
    reference = (
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3",
        "https://dhs.ri.gov/media/10606/download?language=en",
    )
    defined_for = StateCode.RI

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.eligibility.income_limit
        income = spm_unit("ri_ccap_countable_income", period)
        # spm_unit_fpg is annual; requesting with monthly period
        # auto-converts to monthly
        fpg = spm_unit("spm_unit_fpg", period)
        # Per 218-RICR-20-00-4.6.1(A)(1)(a):
        # New applicants: income <= entry_rate * FPG (261% FPL)
        # Enrolled families (transitional): income <= transitional_rate * FPG (300% FPL)
        enrolled = spm_unit("is_ri_ccap_enrolled", period)
        income_limit = where(
            enrolled,
            p.transitional_rate * fpg,
            p.entry_rate * fpg,
        )
        return income <= income_limit
