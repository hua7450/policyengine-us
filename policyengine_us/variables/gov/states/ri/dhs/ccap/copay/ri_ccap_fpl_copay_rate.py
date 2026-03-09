from policyengine_us.model_api import *


class ri_ccap_fpl_copay_rate(Variable):
    value_type = float
    entity = SPMUnit
    label = "Rhode Island CCAP co-share rate based on FPL level"
    definition_period = YEAR
    unit = "/1"
    defined_for = StateCode.RI
    reference = "https://rules.sos.ri.gov/regulations/part/218-20-00-4#4.6.1"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.copay
        countable_income = spm_unit("ri_ccap_countable_income", period)
        fpg = spm_unit("spm_unit_fpg", period)
        fpl_ratio = where(fpg > 0, countable_income / fpg, 0)
        return p.rate.calc(fpl_ratio)
