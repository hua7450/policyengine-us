from policyengine_us.model_api import *


class ct_tanf_countable_earned_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Connecticut TANF countable earned income"
    unit = USD
    definition_period = MONTH
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = StateCode.CT

    adds = ["ct_tanf_earned_income_after_disregard"]
