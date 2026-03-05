from policyengine_us.model_api import *


class ri_ccap_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Rhode Island CCAP based on income"
    definition_period = MONTH
    reference = "https://dhs.ri.gov/media/9236/download?language=en#page=27"
    defined_for = StateCode.RI

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.income
        countable_income = spm_unit("ri_ccap_countable_income", period)
        fpg = spm_unit("spm_unit_fpg", period)
        enrolled = spm_unit("ri_ccap_enrolled", period)
        threshold = where(
            enrolled,
            p.exit_threshold,
            p.entry_threshold,
        )
        return countable_income <= threshold * fpg
