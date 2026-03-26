from policyengine_us.model_api import *


class ct_ssp_gross_income(Variable):
    value_type = float
    entity = Person
    label = "Connecticut SSP gross income"
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.CT
    reference = "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ct.html"

    # Per UPM 5030.15: CT SSP counts SSI payments as unearned income.
    adds = ["ssi_earned_income", "ssi_unearned_income", "ssi"]
