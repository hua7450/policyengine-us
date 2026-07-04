from policyengine_us.model_api import *


class snap_expense_counted_share(Variable):
    value_type = float
    entity = SPMUnit
    label = "SNAP share of expenses counted toward deductions"
    definition_period = MONTH
    reference = (
        "https://www.law.cornell.edu/cfr/text/7/273.11#c_2_iii",
        "https://www.law.cornell.edu/cfr/text/7/273.11#d_1",
    )

    def formula(spm_unit, period, parameters):
        # Shared expenses are assumed to be paid evenly per capita; the
        # shares of nonhousehold members and prorated ineligible members
        # are not deductible.
        size = spm_unit("spm_unit_size", period)
        students = add(spm_unit, period, ["is_snap_ineligible_student"])
        prorated = add(spm_unit, period, ["is_snap_prorated_income_member"])
        counted_members = size - students - prorated
        return where(size > 0, counted_members / max_(size, 1), 1)
