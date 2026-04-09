from policyengine_us.model_api import *


class ga_caps_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Georgia CAPS countable income"
    definition_period = MONTH
    unit = USD
    defined_for = StateCode.GA
    reference = "https://caps.decal.ga.gov/assets/downloads/CAPS/04-CAPS_Policy-Chapter_8.pdf#page=3"

    adds = "gov.states.ga.decal.caps.income.countable_income.sources"
