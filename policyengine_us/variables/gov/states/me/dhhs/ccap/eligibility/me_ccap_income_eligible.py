from policyengine_us.model_api import *


class me_ccap_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Income eligible for Maine CCAP"
    definition_period = MONTH
    defined_for = StateCode.ME
    reference = "https://www.maine.gov/sos/cec/rules/10/ch6.pdf#page=7"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.me.dhhs.ccap.income
        countable_income = spm_unit("me_ccap_countable_income", period)
        monthly_smi = spm_unit("me_ccap_smi", period)
        income_limit = monthly_smi * p.smi_limit
        return countable_income <= income_limit
