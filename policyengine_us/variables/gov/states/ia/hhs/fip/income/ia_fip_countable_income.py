from policyengine_us.model_api import *


class ia_fip_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Iowa FIP countable income"
    unit = USD
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/regulations/iowa/Iowa-Admin-Code-r-441-41-27"
    defined_for = StateCode.IA

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ia.hhs.fip.income
        countable_earned = spm_unit("ia_fip_countable_earned_income", period)
        unearned = add(spm_unit, period, ["tanf_gross_unearned_income"])
        child_support = add(spm_unit, period, ["child_support_received"])
        child_support_exemption = min_(
            child_support, p.child_support_exemption.amount
        )
        return max_(countable_earned + unearned - child_support_exemption, 0)
