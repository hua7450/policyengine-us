from policyengine_us.model_api import *


class ky_ktap_countable_earned_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Kentucky K-TAP countable earned income"
    unit = USD
    definition_period = MONTH
    reference = (
        "https://apps.legislature.ky.gov/law/kar/titles/921/002/016/",
        "https://apps.legislature.ky.gov/law/kar/titles/921/002/016/10142/",
    )
    defined_for = StateCode.KY

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ky.dcbs.ktap.income.deductions
        gross_earned = add(spm_unit, period, ["tanf_gross_earned_income"])
        after_work_expense = max_(gross_earned - p.work_expense, 0)
        dependent_care = spm_unit("ky_ktap_dependent_care_disregard", period)
        earned_after_deductions = max_(after_work_expense - dependent_care, 0)
        if p.earned_income_flat_disregard_in_effect:
            # Pre-2023 (AFDC-era): $30 flat + 1/3 of remainder
            flat = p.earned_income_flat_disregard
            remainder = max_(earned_after_deductions - flat, 0)
            disregard = flat + p.earned_income_disregard_rate * remainder
        else:
            # Post-2023: simple percentage disregard
            disregard = (
                p.earned_income_disregard_rate * earned_after_deductions
            )
        return max_(earned_after_deductions - disregard, 0)
