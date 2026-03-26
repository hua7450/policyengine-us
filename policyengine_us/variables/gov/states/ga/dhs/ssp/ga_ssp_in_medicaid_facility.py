from policyengine_us.model_api import *


class ga_ssp_in_medicaid_facility(Variable):
    value_type = bool
    entity = Person
    label = "Whether the person resides in a Medicaid facility"
    definition_period = YEAR
    defined_for = StateCode.GA
    reference = (
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ga.html",
        "https://pamms.dhs.ga.gov/dfcs/medicaid/2578/",
    )
