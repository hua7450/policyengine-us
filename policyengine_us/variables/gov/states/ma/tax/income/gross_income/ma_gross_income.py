from policyengine_us.model_api import *


class ma_gross_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "MA gross income"
    unit = USD
    definition_period = YEAR
    reference = "https://www.mass.gov/info-details/mass-general-laws-c62-ss-2"
    defined_for = StateCode.MA

    def formula(tax_unit, period, parameters):
        # MA Form 1 5.0% income (lines 3-10).
        # irs_gross_income floors each source at zero (max_(0, ...)),
        # dropping losses. But MA Form 1 allows losses on:
        #   Line 6a: Business/profession income or loss (Schedule C)
        #   Line 6b: Farm income or loss (Schedule F)
        #   Line 7:  Rental, royalty, partnership, S-corp, trust
        #            income or loss
        # Line 10 instruction: "Be sure to subtract any losses
        # in lines 6 or 7."
        # We start from irs_gross_income then add back losses that
        # the federal variable dropped.
        federal_gross_income = add(tax_unit, period, ["irs_gross_income"])
        # Line 6a/6b: business and farm losses
        se_income = add(tax_unit, period, ["self_employment_income"])
        farm_income = add(tax_unit, period, ["farm_income"])
        # Line 7: rental, partnership, S-corp losses
        rental_income = add(tax_unit, period, ["rental_income"])
        partnership_income = add(tax_unit, period, ["partnership_s_corp_income"])
        farm_rent_income = add(tax_unit, period, ["farm_rent_income"])
        loss_adjustment = (
            min_(se_income, 0)
            + min_(farm_income, 0)
            + min_(rental_income, 0)
            + min_(partnership_income, 0)
            + min_(farm_rent_income, 0)
        )
        # Exclude foreign earned income and Social Security
        # (not part of MA gross income)
        foreign_earned_income = tax_unit("foreign_earned_income_exclusion", period)
        social_security_in_agi = add(tax_unit, period, ["taxable_social_security"])
        deductions = foreign_earned_income + social_security_in_agi
        return max_(0, federal_gross_income + loss_adjustment - deductions)
