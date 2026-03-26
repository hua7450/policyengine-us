from policyengine_us.model_api import *


class in_ssp_rcap(Variable):
    value_type = float
    entity = Person
    label = "Indiana Residential Care Assistance Program"
    unit = USD
    definition_period = MONTH
    defined_for = "in_ssp_rcap_eligible"
    reference = (
        "https://www.law.cornell.edu/regulations/indiana/455-IAC-1-3-3",
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/in.html",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states["in"].fssa.ssp
        living_arrangement = person.household("in_ssp_living_arrangement", period)
        is_licensed = (
            living_arrangement
            == living_arrangement.possible_values.LICENSED_RESIDENTIAL
        )
        per_diem = where(
            is_licensed, p.rcap.per_diem.licensed, p.rcap.per_diem.unlicensed
        )
        average_days_per_month = 365 / MONTHS_IN_YEAR
        room_and_board = per_diem * average_days_per_month
        state_standard = room_and_board + p.personal_needs_allowance
        uncapped_ssi = person("uncapped_ssi", period)
        federal_ssi = max_(uncapped_ssi, 0)
        return max_(state_standard - federal_ssi, 0)
