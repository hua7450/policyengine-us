from policyengine_us.model_api import *


class sc_ira_deduction_spouse(Variable):
    value_type = float
    entity = TaxUnit
    label = "South Carolina IRA deduction of spouse"
    defined_for = StateCode.SC
    unit = USD
    definition_period = YEAR