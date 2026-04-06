from policyengine_us.model_api import *


class va_ccsp_income_test_waived(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Income test waived for Virginia Child Care Subsidy Program"
    definition_period = MONTH
    defined_for = StateCode.VA
    reference = (
        "https://law.lis.virginia.gov/admincode/title8/agency20/chapter790/section30/",
        "https://doe.virginia.gov/home/showpublisheddocument/56270#page=92",
    )

    def formula(spm_unit, period, parameters):
        is_tanf = spm_unit("is_tanf_enrolled", period)
        has_medicaid = add(spm_unit, period, ["receives_medicaid"]) > 0
        has_wic = add(spm_unit, period, ["receives_wic"]) > 0
        return is_tanf | has_medicaid | has_wic
