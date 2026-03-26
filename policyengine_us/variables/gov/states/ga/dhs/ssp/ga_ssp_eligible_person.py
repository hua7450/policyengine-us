from policyengine_us.model_api import *


class ga_ssp_eligible_person(Variable):
    value_type = bool
    entity = Person
    label = "Eligible person for Georgia State Supplementary Payment"
    definition_period = MONTH
    defined_for = StateCode.GA
    reference = (
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ga.html",
        "https://odis.dhs.ga.gov/ViewDocument.aspx?docId=3006859&verId=1",
    )

    def formula(person, period, parameters):
        is_ssi_eligible = person("is_ssi_eligible", period.this_year)
        # Must actually receive SSI (income test), not just be categorically eligible.
        receives_ssi = person("uncapped_ssi", period.this_year) > 0
        in_medicaid_facility = person("ga_ssp_in_medicaid_facility", period.this_year)
        return is_ssi_eligible & receives_ssi & in_medicaid_facility
