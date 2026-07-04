from policyengine_us.model_api import *


class snap_dependent_care_deduction(Variable):
    value_type = float
    entity = SPMUnit
    label = "SNAP dependent care deduction"
    unit = USD
    documentation = "Deduction from SNAP gross income for dependent care"
    definition_period = MONTH
    reference = (
        "https://www.law.cornell.edu/uscode/text/7/2014#e_3",
        "https://www.law.cornell.edu/cfr/text/7/273.11#c_2_iii",
    )

    def formula(spm_unit, period, parameters):
        expenses = add(spm_unit, period, ["childcare_expenses"])
        share = spm_unit("snap_expense_counted_share", period)
        return expenses * share
