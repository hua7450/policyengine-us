from policyengine_us.model_api import *


class ia_fip_countable_earned_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Iowa FIP countable earned income"
    unit = USD
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/regulations/iowa/Iowa-Admin-Code-r-441-41-27"
    defined_for = StateCode.IA

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ia.hhs.fip.income
        gross_earned = add(spm_unit, period, ["tanf_gross_earned_income"])
        after_eid = gross_earned * (1 - p.earned_income_deduction.rate)
        return max_(after_eid * (1 - p.work_incentive_disregard.rate), 0)
