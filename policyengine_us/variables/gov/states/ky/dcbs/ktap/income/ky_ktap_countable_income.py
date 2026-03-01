from policyengine_us.model_api import *


class ky_ktap_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Kentucky K-TAP countable income"
    unit = USD
    definition_period = MONTH
    reference = "https://apps.legislature.ky.gov/law/kar/titles/921/002/016/"
    defined_for = StateCode.KY

    adds = [
        "ky_ktap_countable_earned_income",
        "ky_ktap_countable_unearned_income",
    ]
