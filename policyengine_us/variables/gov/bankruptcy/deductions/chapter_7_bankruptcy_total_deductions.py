from policyengine_us.model_api import *


class chapter_7_bankruptcy_total_deductions(Variable):
    value_type = float
    entity = SPMUnit
    label = "Total deductions from Income"
    unit = USD
    definition_period = YEAR

    adds = [
        "chapter_7_bankruptcy_food_clothing_and_others_deduction",
        "chapter_7_bankruptcy_out_of_pocket_health_care_deduction",
        "chapter_7_bankruptcy_local_standards_deductions",
        "chapter_7_bankruptcy_vehicle_operation_expense_deduction",
        "chapter_7_bankruptcy_other_necessary_expenses_deductions",
        "chapter_7_bankruptcy_additional_expense_deductions",
        "chapter_7_bankruptcy_debt_payment_deductions",
    ]