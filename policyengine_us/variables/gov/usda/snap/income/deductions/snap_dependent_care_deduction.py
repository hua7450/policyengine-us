from policyengine_us.model_api import *


class snap_dependent_care_deduction(Variable):
    value_type = float
    entity = SPMUnit
    label = "SNAP dependent care deduction"
    unit = USD
    documentation = "Deduction from SNAP gross income for dependent care"
    definition_period = MONTH
    reference = (
        "https://www.law.cornell.edu/uscode/text/7/2014#e_3",
        "https://www.law.cornell.edu/cfr/text/7/273.9#d_4",
    )

    # Per 7 CFR 273.9(d)(4), deductible costs cover care of a child under
    # age 18 or an incapacitated person of any age.
    adds = ["childcare_expenses", "care_expenses"]
