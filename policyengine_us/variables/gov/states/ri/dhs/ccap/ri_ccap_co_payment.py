from policyengine_us.model_api import *


class ri_ccap_co_payment(Variable):
    value_type = float
    entity = SPMUnit
    label = (
        "Rhode Island Child Care Assistance Program (CCAP) weekly copayment"
    )
    definition_period = MONTH
    unit = USD
    defined_for = StateCode.RI
    reference = (
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.6",
        "https://dhs.ri.gov/media/10606/download?language=en",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.co_payment
        countable_income = spm_unit("ri_ccap_countable_income", period)
        fpg = spm_unit("spm_unit_fpg", period)
        fpl_ratio = where(fpg > 0, countable_income / fpg, 0)
        copay_rate = p.rate.calc(fpl_ratio)
        annual_income = countable_income * MONTHS_IN_YEAR
        weekly_copay = annual_income * copay_rate / WEEKS_IN_YEAR
        # RI Works recipients and housing insecure pay $0
        is_tanf_enrolled = spm_unit("is_tanf_enrolled", period)
        is_homeless = spm_unit.household("is_homeless", period.this_year)
        exempt = is_tanf_enrolled | is_homeless
        return where(exempt, 0, weekly_copay)
