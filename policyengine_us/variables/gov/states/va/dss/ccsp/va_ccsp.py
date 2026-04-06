from policyengine_us.model_api import *


class va_ccsp(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Virginia Child Care Subsidy Program benefit"
    definition_period = MONTH
    defined_for = "va_ccsp_eligible"
    reference = (
        "https://law.lis.virginia.gov/admincode/title8/agency20/chapter790/section40/",
        "https://doe.virginia.gov/home/showpublisheddocument/56270#page=92",
    )

    def formula(spm_unit, period, parameters):
        expenses = spm_unit("spm_unit_pre_subsidy_childcare_expenses", period)
        copay = spm_unit("va_ccsp_copay", period)
        return max_(expenses - copay, 0)
