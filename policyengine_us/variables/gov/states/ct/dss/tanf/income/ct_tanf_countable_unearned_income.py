from policyengine_us.model_api import *


class ct_tanf_countable_unearned_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA countable unearned income"
    documentation = "Total countable unearned income for the household. Unearned income is counted dollar-for-dollar with no disregards. SSI and EITC are excluded at the source."
    unit = USD
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    # Use federal TANF gross unearned income baseline
    adds = ["tanf_gross_unearned_income"]
