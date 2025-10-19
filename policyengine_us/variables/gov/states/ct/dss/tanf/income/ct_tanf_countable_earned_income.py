from policyengine_us.model_api import *


class ct_tanf_countable_earned_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA countable earned income"
    documentation = "Total countable earned income for the household after applying per-person disregards. This uses the $90 initial disregard; full implementation would use 100% FPL exclusion for continuing recipients."
    unit = USD
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        # Sum person-level earned income after disregards
        return add(
            spm_unit,
            period,
            ["ct_tanf_earned_income_after_disregard"],
        )
