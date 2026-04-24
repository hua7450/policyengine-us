from policyengine_us.model_api import *


class years_since_us_entry(Variable):
    value_type = float
    entity = Person
    label = "Years since US entry or qualified immigration status grant"
    unit = "year"
    definition_period = YEAR
    default_value = 5
    reference = "https://www.law.cornell.edu/uscode/text/8/1613"
    # Default of 5 treats a person as past the federal 5-year bar, which
    # preserves pre-5-year-bar behavior for households that do not set
    # this input. Refugee-like or bar-exempt statuses are handled via
    # separate parameter lists rather than this clock.
