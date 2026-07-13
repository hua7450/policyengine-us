from policyengine_us.model_api import *


class ok_ccs_gross_income(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Oklahoma Child Care Subsidy gross countable income"
    definition_period = MONTH
    defined_for = StateCode.OK
    reference = "https://okrules.elaws.us/oac/340:40-7-11"
    adds = "gov.states.ok.dhs.ccs.income.sources"
