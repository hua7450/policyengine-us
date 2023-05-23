from policyengine_us.model_api import *


class sc_income_head(Variable):
    value_type = float
    entity = TaxUnit
    label = "South Carolina head's income"
    defined_for = StateCode.SC
    unit = USD
    definition_period = YEAR