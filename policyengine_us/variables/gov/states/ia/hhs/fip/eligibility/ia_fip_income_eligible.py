from policyengine_us.model_api import *


class ia_fip_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Iowa FIP income eligible"
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/regulations/iowa/Iowa-Admin-Code-r-441-41-27"
    defined_for = StateCode.IA

    def formula(spm_unit, period, parameters):
        countable_income = spm_unit("ia_fip_countable_income", period)
        payment_standard = spm_unit("ia_fip_payment_standard", period)
        return countable_income < payment_standard
