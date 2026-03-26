from policyengine_us.model_api import *


class ct_ssp_shelter_allowance(Variable):
    value_type = float
    entity = Person
    label = "Connecticut SSP shelter allowance"
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.CT
    reference = (
        "https://www.ctdssmap.com/CTPortal/Information/Get/UPM#4520.10",
        "https://portal.ct.gov/dss/common-elements/program-standards-charts",
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ct.html",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ct.dss.ssp.shelter_allowance
        arrangement = person("ct_ssp_living_arrangement", period.this_year)
        arrangements = arrangement.possible_values
        rent = person("rent", period)

        max_allowance = select(
            [
                arrangement == arrangements.COMMUNITY_ALONE,
                arrangement == arrangements.COMMUNITY_SHARED,
                arrangement == arrangements.BOARDING_HOME,
                arrangement == arrangements.SNF,
            ],
            [
                p.living_alone,
                p.shared,
                0,
                0,
            ],
            default=p.living_alone,
        )
        return min_(rent, max_allowance)
