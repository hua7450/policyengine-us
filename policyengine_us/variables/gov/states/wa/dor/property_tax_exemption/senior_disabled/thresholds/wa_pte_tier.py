from policyengine_us.model_api import *


class wa_pte_tier(Variable):
    value_type = int
    entity = SPMUnit
    label = "Washington Senior/Disabled Property Tax Exemption tier"
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
        tier_1_threshold = np.zeros_like(county, dtype=float)
        tier_2_threshold = np.zeros_like(county, dtype=float)
        tier_3_threshold = np.zeros_like(county, dtype=float)
        tier_1_threshold[in_wa] = p.thresholds.tier_1[county[in_wa]]
        tier_2_threshold[in_wa] = p.thresholds.tier_2[county[in_wa]]
        tier_3_threshold[in_wa] = p.thresholds.tier_3[county[in_wa]]
        # Tier 1 has the strictest income limit and the largest exemption.
        return select(
            [
                income <= tier_1_threshold,
                income <= tier_2_threshold,
                income <= tier_3_threshold,
            ],
            [1, 2, 3],
            default=0,
        )
