from policyengine_us.model_api import *


class nd_primary_residence_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "North Dakota primary residence credit"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.tax.nd.gov/prc",
        "https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1176.html?bill_year=2025-2026",
        "https://ndlegis.gov/cencode/t57c02.pdf",
    )
    defined_for = StateCode.ND

    def formula(tax_unit, period, parameters):
        # The primary residence credit reduces property tax on an
        # owner-occupied primary residence, capped at a flat amount, with no
        # age or income limitation. Renters have no real estate taxes, so the
        # credit is zero for them.
        p = parameters(period).gov.states.nd.tax.property.primary_residence_credit
        property_tax = add(tax_unit, period, ["real_estate_taxes"])
        return min_(p.amount, property_tax)
