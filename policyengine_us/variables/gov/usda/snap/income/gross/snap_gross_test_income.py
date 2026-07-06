from policyengine_us.model_api import *


class snap_gross_test_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "SNAP gross income for the gross income test"
    reference = (
        "https://www.law.cornell.edu/uscode/text/7/2014#c",
        "https://www.law.cornell.edu/cfr/text/7/273.11#c_3_i",
    )
    unit = USD

    def formula(spm_unit, period, parameters):
        # Certain states count the full income of certain ineligible aliens
        # under the gross income test while prorating it under the net
        # income test.
        gross_income = spm_unit("snap_gross_income", period)
        person = spm_unit.members
        full_count_gross = person("is_snap_gross_test_full_income_count_alien", period)
        income = person("snap_earned_income_person", period) + person(
            "snap_unearned_income_person", period
        )
        se_weight = max_(person("snap_gross_self_employment_income_person", period), 0)
        total_weight = spm_unit.sum(se_weight)
        full_count_weight = spm_unit.sum(se_weight * full_count_gross)
        unit_self_employment = spm_unit(
            "snap_self_employment_income_after_expense_deduction", period
        )
        full_count_self_employment = where(
            total_weight > 0,
            unit_self_employment
            * full_count_weight
            / where(total_weight > 0, total_weight, 1),
            0,
        )
        full_count_income = (
            spm_unit.sum(full_count_gross * income) + full_count_self_employment
        )
        fraction = spm_unit("snap_prorated_income_fraction", period)
        return gross_income + full_count_income * (1 - fraction)
