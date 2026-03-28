from policyengine_us.model_api import *


class detailed_industry_recode(Variable):
    value_type = int
    entity = Person
    label = "CPS detailed industry recode of previous year"
    documentation = (
        "This variable is the A_DTIND detailed industry recode in the "
        "Current Population Survey ASEC when available."
    )
    definition_period = YEAR
