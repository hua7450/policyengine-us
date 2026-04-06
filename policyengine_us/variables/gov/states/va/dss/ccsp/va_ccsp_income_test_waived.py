from policyengine_us.model_api import *


class va_ccsp_income_test_waived(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Income test waived for Virginia Child Care Subsidy Program"
    definition_period = MONTH
    defined_for = StateCode.VA
    reference = (
        "https://law.lis.virginia.gov/admincode/title8/agency20/chapter790/section30/",
        "https://doe.virginia.gov/home/showpublisheddocument/56270#page=29",
    )

    def formula(spm_unit, period, parameters):
        return spm_unit("is_tanf_enrolled", period)
