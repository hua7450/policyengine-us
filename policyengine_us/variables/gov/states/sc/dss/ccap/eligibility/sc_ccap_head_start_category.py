from policyengine_us.model_api import *


class sc_ccap_head_start_category(Variable):
    value_type = bool
    entity = SPMUnit
    label = "South Carolina CCAP Head Start wraparound category"
    definition_period = MONTH
    defined_for = StateCode.SC
    reference = (
        "https://www.scchildcare.org/media/ubhdm1at/1-13-2025_policy-manual.pdf#page=91"
    )

    def formula(spm_unit, period, parameters):
        return add(spm_unit, period.this_year, ["is_enrolled_in_head_start"]) > 0
