from policyengine_us.model_api import *


class fl_tanf_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Florida Temporary Cash Assistance (TANF)"
    definition_period = MONTH
    reference = "Florida Statute § 414.095"
    documentation = "https://www.flsenate.gov/Laws/Statutes/2024/414.095"
    defined_for = StateCode.FL

    def formula(spm_unit, period, parameters):
        categorical_eligible = spm_unit(
            "fl_tanf_categorically_eligible", period
        )
        income_eligible = spm_unit("fl_tanf_income_eligible", period)
        resource_eligible = spm_unit("fl_tanf_resource_eligible", period)

        return categorical_eligible & income_eligible & resource_eligible
