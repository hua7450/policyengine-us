from policyengine_us.model_api import *


class pa_ccw_adjusted_income(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Pennsylvania CCW adjusted annual family income"
    definition_period = YEAR
    defined_for = StateCode.PA
    reference = "https://www.pacodeandbulletin.gov/secure/pacode/data/055/chapter3042/055_3042.pdf#page=18"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.pa.dhs.ccw.income
        gross_annual = add(spm_unit, period, ["pa_ccw_countable_income"])
        gross_monthly = gross_annual / MONTHS_IN_YEAR
        stepparent_deduction = spm_unit(
            "pa_ccw_stepparent_deduction", period.first_month
        )
        alimony_paid = add(spm_unit, period, ["alimony_expense"]) / MONTHS_IN_YEAR
        child_support_paid = (
            add(spm_unit, period, ["child_support_expense"]) / MONTHS_IN_YEAR
        )
        medical_threshold = gross_monthly * p.medical_expense_threshold
        medical_expenses = (
            add(spm_unit, period, ["medical_out_of_pocket_expenses"]) / MONTHS_IN_YEAR
        )
        medical_deduction = max_(medical_expenses - medical_threshold, 0)
        adjusted_monthly = max_(
            gross_monthly
            - stepparent_deduction
            - alimony_paid
            - child_support_paid
            - medical_deduction,
            0,
        )
        return adjusted_monthly * MONTHS_IN_YEAR
