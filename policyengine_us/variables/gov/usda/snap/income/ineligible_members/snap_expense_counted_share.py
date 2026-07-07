from policyengine_us.model_api import *


class snap_expense_counted_share(Variable):
    value_type = float
    entity = SPMUnit
    label = "SNAP share of expenses counted toward deductions"
    definition_period = MONTH
    unit = "/1"
    reference = (
        "https://www.law.cornell.edu/cfr/text/7/273.11#c_2_iii",
        "https://www.law.cornell.edu/cfr/text/7/273.11#d_1",
    )

    def formula(spm_unit, period, parameters):
        # Shared expenses are assumed to be paid evenly per capita.
        # Ineligible students are nonhousehold members, so their per capita
        # payments are not the household's expense (273.11(d)(1)). The
        # portion paid by prorated ineligible members is divided evenly
        # among household members, and all but the ineligible members'
        # shares count (273.11(c)(2)(iii)): with n household members and i
        # prorated members, the eligible-paid portion (n - i)/size counts
        # in full and the prorated-paid portion contributes
        # (i/size) x (n - i)/n.
        size = spm_unit("spm_unit_size", period)
        students = add(spm_unit, period, ["is_snap_ineligible_student"])
        prorated = add(spm_unit, period, ["is_snap_prorated_income_member"])
        household_members = size - students
        eligible_members = household_members - prorated
        return where(
            household_members > 0,
            (eligible_members * (household_members + prorated))
            / (size * max_(household_members, 1)),
            0,
        )
