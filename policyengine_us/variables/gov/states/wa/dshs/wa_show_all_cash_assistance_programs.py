from policyengine_us.model_api import *


class wa_show_all_cash_assistance_programs(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Treat all Washington cash assistance programs as immigration-eligible for display"
    definition_period = MONTH
    default_value = False
    defined_for = StateCode.WA
