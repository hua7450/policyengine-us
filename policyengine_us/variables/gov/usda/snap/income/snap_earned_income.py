from policyengine_us.model_api import *


class snap_earned_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "SNAP earned income"
    documentation = "Earned income for calculating the SNAP earned income deduction"
    reference = (
        "https://www.law.cornell.edu/cfr/text/7/273.9#b_1",
        "https://www.law.cornell.edu/cfr/text/7/273.11#c",
    )
    unit = USD

    def formula(spm_unit, period, parameters):
        person = spm_unit.members
        employment = person("snap_earned_income_person", period)
        share = person("snap_income_counted_share", period)
        # Self-employment income net of the expense deduction is computed at
        # the SPM unit level; attribute it to members in proportion to their
        # gross self-employment income.
        se_weight = max_(person("snap_gross_self_employment_income_person", period), 0)
        total_weight = spm_unit.sum(se_weight)
        counted_weight = spm_unit.sum(se_weight * share)
        unit_self_employment = spm_unit(
            "snap_self_employment_income_after_expense_deduction", period
        )
        counted_self_employment = where(
            total_weight > 0,
            unit_self_employment
            * counted_weight
            / where(total_weight > 0, total_weight, 1),
            0,
        )
        return spm_unit.sum(employment * share) + counted_self_employment
