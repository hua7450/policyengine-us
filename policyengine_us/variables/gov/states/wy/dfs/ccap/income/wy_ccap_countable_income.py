from policyengine_us.model_api import *


class wy_ccap_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Wyoming CCAP countable income"
    definition_period = MONTH
    unit = USD
    defined_for = StateCode.WY
    reference = (
        "https://drive.google.com/file/d/1yatL28Yylj62R2cTipV2sGa10TxZplxr/view",  # Wyo. Admin. Rules, DFS, Child Care - Purchase of Service, Ch. 1 §8(e)(iv)(D), eff. 05/07/2025 (PDF p. 19)
        "https://drive.google.com/file/d/1XWs2Q_duALLgJzG88OthnYJ87XApYZzS/view",  # Wyoming DFS Child Care Subsidy Policy Manual §§905, 907 (PDF pp. 5-9)
    )

    def formula(spm_unit, period, parameters):
        # Rules Ch. 1 §8(e)(iv)(D): countable income is gross earned plus
        # gross unearned income from the counted sources, less allowable
        # deductions. Manual §§902-903 deduct 25% of gross self-employment
        # receipts or actual business expenses, whichever benefits the
        # client; self_employment_income is already net of actual expenses,
        # matching the actual-expense branch, and PolicyEngine has no
        # gross-receipts input, so the fixed-25% alternative is not modeled.
        p = parameters(period).gov.states.wy.dfs.ccap.income
        person = spm_unit.members
        # The earned rows of the counted sources
        # (income/countable_income/sources.yaml).
        earned = add(
            person,
            period,
            [
                "employment_income",
                "self_employment_income",
                "sstb_self_employment_income",
                "farm_operations_income",
            ],
        )
        # Appendix B exempts the wages of dependent children under 18; a
        # minor unit head or spouse (a minor parent) remains counted.
        is_minor_dependent = person("is_child", period.this_year) & ~person(
            "is_tax_unit_head_or_spouse", period.this_year
        )
        # Rules Ch. 1 §4(aa), §8(e)(iv)(D)(III)(5.): deduct $200 from the
        # gross earned income of each working adult, capped at that adult's
        # earnings; the per-person zero floor also keeps a self-employment
        # loss from offsetting other income.
        countable_earned = where(
            is_minor_dependent, 0, max_(earned - p.earned_income_disregard, 0)
        )
        unearned = spm_unit("wy_ccap_gross_income", period) - spm_unit.sum(earned)
        # Manual §907.B: deduct child support paid by a parent whose income
        # counts, capped at the monthly court-ordered amount and excluding
        # arrears; the court-ordered amount and arrears are not tracked, so
        # the full support paid is deducted.
        child_support = add(spm_unit, period, ["child_support_expense"])
        return max_(spm_unit.sum(countable_earned) + unearned - child_support, 0)
