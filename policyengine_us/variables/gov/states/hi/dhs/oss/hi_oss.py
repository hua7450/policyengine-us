from policyengine_us.model_api import *


class hi_oss(Variable):
    value_type = float
    entity = Person
    label = "Hawaii Optional State Supplementation"
    unit = USD
    definition_period = YEAR
    defined_for = "hi_oss_eligible"
    reference = (
        "https://secure.ssa.gov/apps10/poms.nsf/lnx/0501415200SF",
        "https://secure.ssa.gov/POMS.NSF/lnx/0501415057",
    )

    def formula(person, period, parameters):
        monthly_amount = person("hi_oss_payment_amount", period)
        return monthly_amount * MONTHS_IN_YEAR
