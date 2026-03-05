from policyengine_us.model_api import *


class ri_ccap_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Rhode Island Child Care Assistance Program (CCAP) based on income"
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.6"
    defined_for = StateCode.RI

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.income.income_limit
        countable_income = spm_unit("ri_ccap_countable_income", period)
        fpg = spm_unit("spm_unit_fpg", period)
        enrolled = spm_unit("is_ri_ccap_enrolled", period)
        fpg_rate = where(
            enrolled,
            p.transitional_rate,
            p.entry_rate,
        )
        income_limit = fpg_rate * fpg
        return countable_income <= income_limit
