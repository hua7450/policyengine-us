from policyengine_us.model_api import *


class wa_pte_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Income-eligible for the Washington Senior Citizens and Disabled Persons Property Tax Exemption"
    definition_period = MONTH
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=84.36.381",
        "https://app.leg.wa.gov/RCW/default.aspx?cite=84.36.383",
        "https://dor.wa.gov/sites/default/files/2022-02/PTExemption_Senior.pdf#page=2",
    )

    def formula(spm_unit, period, parameters):
        income = spm_unit("wa_pte_combined_disposable_income", period.this_year)
        in_wa = spm_unit.household("state_code_str", period.this_year) == "WA"
        county = spm_unit.household("county_str", period.this_year)
        p = parameters(period).gov.states.wa.dor.property_tax_exemption.senior_disabled
        threshold = np.zeros_like(county, dtype=float)
        threshold[in_wa] = p.thresholds.tier_3[county[in_wa]]
        # Tier 3 is the highest qualifying income threshold; income above it
        # disqualifies the household from any tier of the exemption.
        return income <= threshold
