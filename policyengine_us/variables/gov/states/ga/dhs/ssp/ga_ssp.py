from policyengine_us.model_api import *


class ga_ssp(Variable):
    value_type = float
    entity = SPMUnit
    label = "Georgia State Supplementary Payment"
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.GA
    reference = (
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ga.html",
        "https://odis.dhs.ga.gov/ViewDocument.aspx?docId=3006859&verId=1",
    )

    adds = ["ga_ssp_person"]
