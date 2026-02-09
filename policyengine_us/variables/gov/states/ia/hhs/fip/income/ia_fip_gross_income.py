from policyengine_us.model_api import *


class ia_fip_gross_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Iowa FIP gross income"
    unit = USD
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/regulations/iowa/Iowa-Admin-Code-r-441-41-27"
    defined_for = StateCode.IA
    adds = ["tanf_gross_earned_income", "tanf_gross_unearned_income"]
