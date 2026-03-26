from policyengine_us.model_api import *


class ga_ssp_person(Variable):
    value_type = float
    entity = Person
    label = "Georgia State Supplementary Payment per person"
    unit = USD
    definition_period = MONTH
    defined_for = "ga_ssp_eligible_person"
    reference = (
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ga.html",
        "https://odis.dhs.ga.gov/ViewDocument.aspx?docId=3006859&verId=1",
    )

    def formula(person, period, parameters):
        return parameters(period).gov.states.ga.dhs.ssp.amount
