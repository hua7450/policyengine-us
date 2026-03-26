from policyengine_us.model_api import *


class ct_ssp_personal_needs_allowance(Variable):
    value_type = float
    entity = Person
    label = "Connecticut SSP personal needs allowance"
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.CT
    reference = (
        "https://portal.ct.gov/dss/common-elements/program-standards-charts",
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ct.html",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ct.dss.ssp.personal_needs_allowance
        arrangement = person("ct_ssp_living_arrangement", period.this_year)
        arrangements = arrangement.possible_values
        is_joint_claim = person("ssi_claim_is_joint", period.this_year)

        community_pna = where(
            is_joint_claim,
            p.community_married,
            p.community_individual,
        )

        return select(
            [
                arrangement == arrangements.COMMUNITY_ALONE,
                arrangement == arrangements.COMMUNITY_SHARED,
                arrangement == arrangements.BOARDING_HOME,
                arrangement == arrangements.SNF,
            ],
            [
                community_pna,
                community_pna,
                p.boarding_home,
                p.snf,
            ],
            default=community_pna,
        )
