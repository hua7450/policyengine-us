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
        eligible = person("dc_ossp_eligible", period)
        joint_claim = person("ssi_claim_is_joint", period.this_year)
        both_eligible = person.marital_unit.sum(eligible) == 2
        # Couple rate requires joint SSI claim, both spouses OSSP-eligible,
        # and both in the same arrangement category.
        is_os_a = living_arrangement == DCOSSPLivingArrangement.OS_A
        is_os_b = living_arrangement == DCOSSPLivingArrangement.OS_B
        is_os_g = living_arrangement == DCOSSPLivingArrangement.OS_G
        both_same = (
            (person.marital_unit.sum(is_os_a) == 2)
            | (person.marital_unit.sum(is_os_b) == 2)
            | (person.marital_unit.sum(is_os_g) == 2)
        )
        is_couple = joint_claim & both_eligible & both_same
        p = parameters(period).gov.states.dc.dhcf.ossp.payment

        os_a = where(is_couple, p.os_a.couple / 2, p.os_a.individual)
        os_b = where(is_couple, p.os_b.couple / 2, p.os_b.individual)
        os_g = where(is_couple, p.os_g.couple / 2, p.os_g.individual)

        return select(
            [is_os_a, is_os_b, is_os_g],
            [os_a, os_b, os_g],
            default=0,
        )
