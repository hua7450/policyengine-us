from policyengine_us.model_api import *


class sc_ccap_copay(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "South Carolina CCAP monthly family copay"
    definition_period = MONTH
    defined_for = StateCode.SC
    reference = (
        "https://www.scchildcare.org/media/ubhdm1at/1-13-2025_policy-manual.pdf#page=86",
        "https://www.scchildcare.org/media/ih2mrjw5/fee-scale-2025-2026.pdf#page=1",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.sc.dss.ccap.copay
        # Exempt populations: TANF, foster care, homeless,
        # families at/below 150% FPL, families with disabled children.
        is_tanf = spm_unit("is_tanf_enrolled", period)
        has_foster_child = add(spm_unit, period, ["is_in_foster_care"]) > 0
        is_homeless = spm_unit.household("is_homeless", period.this_year)
        monthly_fpg = spm_unit("spm_unit_fpg", period)
        below_fpl_threshold = (
            spm_unit("sc_ccap_countable_income", period)
            <= monthly_fpg * p.fpg_exempt_rate
        )
        has_disabled_child = add(spm_unit, period, ["is_disabled"]) > 0
        exempt = (
            is_tanf
            | has_foster_child
            | is_homeless
            | below_fpl_threshold
            | has_disabled_child
        )

        # Look up weekly copay per child from fee scale by family size
        # and monthly income.
        monthly_income = spm_unit("sc_ccap_countable_income", period)
        size = spm_unit("spm_unit_size", period.this_year)
        capped_size = min_(size, p.max_family_size).astype(int)
        fee_scale = p.fee_scale
        weekly_copay_per_child = select(
            [capped_size == i for i in range(1, 17)],
            [fee_scale[f"family_size_{i}"].calc(monthly_income) for i in range(1, 17)],
        )
        # Cap weekly copay at 2% of annual income / 52 weeks.
        weekly_income_cap = (
            monthly_income * p.income_cap_rate * MONTHS_IN_YEAR / WEEKS_IN_YEAR
        )
        capped_weekly = min_(weekly_copay_per_child, weekly_income_cap)
        # Multiply by eligible children and convert to monthly.
        num_eligible = add(spm_unit, period, ["sc_ccap_eligible_child"])
        monthly_copay = capped_weekly * num_eligible * (WEEKS_IN_YEAR / MONTHS_IN_YEAR)
        return where(exempt, 0, monthly_copay)
