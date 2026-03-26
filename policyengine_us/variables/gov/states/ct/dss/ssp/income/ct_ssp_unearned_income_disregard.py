from policyengine_us.model_api import *


class ct_ssp_unearned_income_disregard(Variable):
    value_type = float
    entity = Person
    label = "Connecticut SSP unearned income disregard"
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.CT
    reference = (
        "https://www.ctdssmap.com/CTPortal/Information/Get/UPM#5030.15",
        "https://portal.ct.gov/dss/common-elements/program-standards-charts",
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ct.html",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ct.dss.ssp.disregard.unearned
        arrangement = person("ct_ssp_living_arrangement", period.this_year)
        arrangements = arrangement.possible_values

        return select(
            [
                arrangement == arrangements.COMMUNITY_ALONE,
                arrangement == arrangements.COMMUNITY_SHARED,
                arrangement == arrangements.BOARDING_HOME,
                arrangement == arrangements.SNF,
            ],
            [
                p.community,
                p.shared_living,
                p.boarding_home,
                p.community,
            ],
            default=p.community,
        )
