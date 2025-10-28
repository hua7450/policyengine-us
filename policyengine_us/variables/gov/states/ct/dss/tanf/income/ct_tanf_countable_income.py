from policyengine_us.model_api import *


class ct_tanf_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA countable income"
    unit = USD
    reference = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
    defined_for = StateCode.CT

    adds = [
        "ct_tanf_countable_earned_income",
        "ct_tanf_countable_unearned_income",
    ]
