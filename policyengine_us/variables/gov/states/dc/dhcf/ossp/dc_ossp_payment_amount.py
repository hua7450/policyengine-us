from policyengine_us.model_api import *
from policyengine_us.variables.gov.states.dc.dhcf.ossp.dc_ossp_living_arrangement import (
    DCOSSPLivingArrangement,
)


class dc_ossp_payment_amount(Variable):
    value_type = float
    entity = Person
    label = "DC OSSP monthly payment amount"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.DC
    reference = (
        "https://code.dccouncil.gov/us/dc/council/code/sections/4-205.49",
        "https://secure.ssa.gov/poms.nsf/lnx/0501415009",
    )

    def formula(person, period, parameters):
        living_arrangement = person("dc_ossp_living_arrangement", period)
        is_married = person.family("is_married", period.this_year)
        p = parameters(period).gov.states.dc.dhcf.ossp.payment
        # Individual amounts
        os_a_ind = p.os_a.individual.amount
        os_b_ind = p.os_b.individual.amount
        os_g_ind = p.os_g.individual.amount
        # Couple amounts (per person = couple amount / 2)
        os_a_couple = p.os_a.couple.amount / 2
        os_b_couple = p.os_b.couple.amount / 2
        os_g_couple = p.os_g.couple.amount / 2
        # Select individual or couple amount
        os_a_amount = where(is_married, os_a_couple, os_a_ind)
        os_b_amount = where(is_married, os_b_couple, os_b_ind)
        os_g_amount = where(is_married, os_g_couple, os_g_ind)
        return select(
            [
                living_arrangement == DCOSSPLivingArrangement.OS_A,
                living_arrangement == DCOSSPLivingArrangement.OS_B,
                living_arrangement == DCOSSPLivingArrangement.OS_G,
            ],
            [os_a_amount, os_b_amount, os_g_amount],
            default=0,
        )
