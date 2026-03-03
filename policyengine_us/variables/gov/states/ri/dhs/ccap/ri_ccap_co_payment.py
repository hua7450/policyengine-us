from policyengine_us.model_api import *


class ri_ccap_co_payment(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Rhode Island Child Care Assistance Program co-payment"
    reference = (
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3",
        "https://dhs.ri.gov/media/10606/download?language=en",
    )
    unit = USD
    defined_for = "ri_ccap_eligible"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ri.dhs.ccap.co_payment
        income = spm_unit("ri_ccap_countable_income", period)
        # spm_unit_fpg is annual; requesting with monthly period
        # auto-converts to monthly
        fpg = spm_unit("spm_unit_fpg", period)
        # Per 218-RICR-20-00-4.6.1(C)(1)(c): co-payment rate is
        # based on income as a ratio of FPL
        fpl_ratio = income / fpg
        co_payment_rate = p.rate.calc(fpl_ratio)
        return co_payment_rate * income
