from policyengine_us.model_api import *


class or_erdc_special_needs_rate_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eligible for the Oregon ERDC special needs rate"
    defined_for = StateCode.OR
    reference = "https://www.oregon.gov/delc/providers/Documents/Provider%20Rate%20Increase%20For%20Jan%202026_Phase%202_ENG.pdf#page=1"
