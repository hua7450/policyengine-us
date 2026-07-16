from policyengine_us.model_api import *


class ut_ccap_gross_income(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Utah CCAP gross countable income"
    definition_period = MONTH
    defined_for = StateCode.UT
    reference = "https://utrules.elaws.us/uac/r986-700-710"
    adds = "gov.states.ut.dwf.ccap.income.sources"
