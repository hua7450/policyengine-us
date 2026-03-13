from policyengine_us.model_api import *


class ct_c4k_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = YEAR
    defined_for = StateCode.CT
    label = "Eligible for Connecticut Care 4 Kids"
    reference = "https://eregulations.ct.gov/eRegsPortal/Browse/RCSA/Title_17bSubtitle_17b-749Section_17b-749-04/"

    def formula(spm_unit, period, parameters):
        has_eligible_child = add(spm_unit, period, ["ct_c4k_eligible_child"]) > 0
        income_eligible = spm_unit("ct_c4k_income_eligible", period)
        asset_eligible = spm_unit("is_ccdf_asset_eligible", period)
        activity_eligible = spm_unit("meets_ccdf_activity_test", period)

        regular_eligible = (
            has_eligible_child & income_eligible & asset_eligible & activity_eligible
        )
        tfa_eligible = spm_unit("ct_tfa_eligible", period.first_month)
        return regular_eligible | tfa_eligible
