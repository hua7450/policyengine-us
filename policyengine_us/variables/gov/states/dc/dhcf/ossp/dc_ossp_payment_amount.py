from policyengine_us.model_api import *
from policyengine_us.variables.gov.states.dc.dhcf.ossp.dc_ossp_living_arrangement import (
    DCOSSPLivingArrangement,
)


class dc_ossp_payment_amount(Variable):
    value_type = float
    entity = Person
    label = "DC OSSP monthly payment amount"
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.DC
    reference = (
        "https://code.dccouncil.gov/us/dc/council/code/sections/4-205.49",
        "https://www.ssa.gov/pubs/EN-05-11162.pdf#page=2",
    )

    def formula(person, period, parameters):
        living_arrangement = person("dc_ossp_living_arrangement", period)
        is_married = person.family("is_married", period.this_year)
        p = parameters(period).gov.states.dc.dhcf.ossp.payment

        os_a = where(is_married, p.os_a.couple / 2, p.os_a.individual)
        os_b = where(is_married, p.os_b.couple / 2, p.os_b.individual)
        os_g = where(is_married, p.os_g.couple / 2, p.os_g.individual)

        return select(
            [
                living_arrangement == DCOSSPLivingArrangement.OS_A,
                living_arrangement == DCOSSPLivingArrangement.OS_B,
                living_arrangement == DCOSSPLivingArrangement.OS_G,
            ],
            [os_a, os_b, os_g],
            default=0,
        )
