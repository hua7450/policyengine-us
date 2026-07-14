from policyengine_us.model_api import *


class va_educator_expense_deduction_person(Variable):
    value_type = float
    entity = Person
    label = "Virginia eligible educator expense deduction"
    unit = USD
    definition_period = YEAR
    default_value = 0
    defined_for = StateCode.VA
    # Va. Code 58.1-322.03 allows a deduction of the lesser of $500 or the
    # eligible educator qualifying expenses that were NOT reimbursed nor claimed
    # as a deduction on the federal return. Available for TY2022-2024 and,
    # reinstated by the 2026 Appropriation Act (HB 30), for TY2026 and after;
    # it did not apply for TY2025. Because the baseline data do not identify
    # eligible-educator status or the amount of expenses not already claimed
    # federally (the federal educator deduction is above-the-line and thus
    # already reflected in federal AGI), this remains an explicit input that
    # defaults to $0, matching the Ohio educator-deduction treatment.
    reference = (
        "https://law.lis.virginia.gov/vacodefull/title58.1/chapter3/article2/",  # Va. Code 58.1-322.03 - eligible educator expense deduction
        "https://www.tax.virginia.gov/sites/default/files/inline-files/2026-legislative-summary.pdf",  # 2026 Legislative Summary - reinstatement for TY2026+
    )
