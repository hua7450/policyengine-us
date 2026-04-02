from policyengine_us.model_api import *


class sc_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "South Carolina taxable income"
    defined_for = StateCode.SC
    unit = USD
    definition_period = YEAR
    reference = (
        "https://dor.sc.gov/forms-site/Forms/IITPacket_2022.pdf#page=33",
        "https://www.scstatehouse.gov/sess126_2025-2026/bills/4216.htm",
    )

    def formula(tax_unit, period, parameters):
        # Check if we're in H4216 era (2026+)
        # H4216 Section 2: SC does not adopt federal standard/itemized deductions
        # H4216 Section 3: SC uses SCIAD instead, starting from AGI
        year = period.start.year
        subtractions = tax_unit("sc_subtractions", period)

        if year >= 2026:
            # For 2026+: Start from AGI (SC ignores federal std/itemized deductions)
            # Additions are not needed since they correct for federal deductions
            # that are no longer relevant when starting from AGI
            agi = tax_unit("adjusted_gross_income", period)
            return max_(0, agi - subtractions)
        else:
            # Before 2026: Traditional calculation from federal taxable income
            taxable_income = tax_unit("taxable_income", period)
            additions = tax_unit("sc_additions", period)
            return max_(0, taxable_income + additions - subtractions)
