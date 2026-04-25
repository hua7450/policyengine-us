from policyengine_us.model_api import *


class wa_show_all_cash_assistance_programs(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Treat all Washington cash assistance programs as immigration-eligible for display"
    definition_period = MONTH
    defined_for = StateCode.WA
    # Consumer-facing toggle that bypasses immigration-based mutual
    # exclusivity across TANF, SFA, and RCA so that frontend calculators
    # can display all three programs' benefit amounts side by side for the
    # same household. Does not override demographic, income, or resource
    # tests.
