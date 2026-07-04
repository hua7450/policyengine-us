from policyengine_us.model_api import *


class snap_prorated_income_fraction(Variable):
    value_type = float
    entity = SPMUnit
    label = "SNAP prorated income fraction"
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/cfr/text/7/273.11#c_2_ii"

    def formula(spm_unit, period, parameters):
        # The ineligible member's income is divided evenly among household
        # members (excluding nonhousehold members such as ineligible
        # students); all but the ineligible members' shares are counted.
        size = spm_unit("spm_unit_size", period)
        students = add(spm_unit, period, ["is_snap_ineligible_student"])
        household_members = size - students
        eligible_members = spm_unit("snap_unit_size", period)
        return where(
            household_members > 0,
            eligible_members / max_(household_members, 1),
            0,
        )
