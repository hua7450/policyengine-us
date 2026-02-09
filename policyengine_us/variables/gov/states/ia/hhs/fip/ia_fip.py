from policyengine_us.model_api import *


class ia_fip(Variable):
    value_type = float
    entity = SPMUnit
    label = "Iowa FIP"
    unit = USD
    definition_period = MONTH
    reference = (
        "https://www.law.cornell.edu/regulations/iowa/Iowa-Admin-Code-r-441-41-27",
        "https://www.law.cornell.edu/regulations/iowa/Iowa-Admin-Code-r-441-41-28",
    )
    defined_for = "ia_fip_eligible"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ia.hhs.fip
        payment_standard = spm_unit("ia_fip_payment_standard", period)
        countable_income = spm_unit("ia_fip_countable_income", period)
        benefit = max_(payment_standard - countable_income, 0)
        return where(benefit >= p.benefit.minimum_benefit, benefit, 0)
