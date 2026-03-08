from policyengine_us.model_api import *


class hi_oss_payment_amount(Variable):
    value_type = float
    entity = Person
    label = "Hawaii OSS monthly payment amount"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.HI
    reference = (
        "https://secure.ssa.gov/POMS.NSF/lnx/0501415057",
    )

    def formula(person, period, parameters):
        living_arrangement = person("hi_oss_living_arrangement", period)
        is_married = person.family("is_married", period.this_year)
        p = parameters(period).gov.states.hi.dhs.oss.payment
        individual_amount = p.individual.amount[living_arrangement]
        couple_amount = p.couple.amount[living_arrangement] / 2
        return where(is_married, couple_amount, individual_amount)
