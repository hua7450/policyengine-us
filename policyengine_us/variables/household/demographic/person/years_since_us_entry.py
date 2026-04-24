from policyengine_us.model_api import *


class years_since_us_entry(Variable):
    value_type = float
    entity = Person
    label = "Years since US entry or qualified immigration status grant"
    unit = "year"
    definition_period = YEAR
    default_value = 5
    reference = "https://www.law.cornell.edu/uscode/text/8/1613"
