from policyengine_us.model_api import *


class md_ccs_weekly_copay(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Maryland Child Care Scholarship (CCS) weekly copayment"
    definition_period = MONTH
    defined_for = StateCode.MD
    reference = (
        "https://dsd.maryland.gov/regulations/Pages/13A.14.06.12.aspx",
        "https://mgaleg.maryland.gov/2024RS/Chapters_noln/CH_717_sb0482e.pdf",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.md.msde.ccs.copay

        # TCA/SSI recipients pay $0 copayment per COMAR 13A.14.06.12(A)(1)
        is_tca = spm_unit("is_tanf_enrolled", period)
        receives_ssi = add(spm_unit, period, ["ssi"]) > 0

        # SNAP/WIC recipients have copayments waived per Chapters 525/526 of 2022
        # Use bare inputs to avoid circular dependency through SNAP/TANF/childcare chain
        is_snap = spm_unit("md_ccs_receives_snap", period)
        receives_wic = spm_unit("md_ccs_receives_wic", period)
        exempt = is_tca | receives_ssi | is_snap | receives_wic

        # Weekly copay per child based on service unit (enum-keyed lookup)
        person = spm_unit.members
        service_unit = person("md_ccs_service_unit", period)
        weekly_per_child = p.weekly_amount[service_unit]

        # Only charge copay for eligible children
        is_eligible_child = person("md_ccs_eligible_child", period)
        weekly_per_child = where(is_eligible_child, weekly_per_child, 0)

        # Copay assessed for up to max_children_with_copay children
        eligible_child_count = add(spm_unit, period, ["md_ccs_eligible_child"])
        capped_count = min_(eligible_child_count, p.max_children_with_copay)
        total_weekly = spm_unit.sum(weekly_per_child)
        scale = where(
            eligible_child_count > 0,
            capped_count / eligible_child_count,
            0,
        )
        scaled_weekly = total_weekly * scale

        # Federal cap: copay cannot exceed 7% of gross income per 45 CFR 98.45(k)
        countable_income = spm_unit("md_ccs_countable_income", period)
        weekly_income = countable_income * MONTHS_IN_YEAR / WEEKS_IN_YEAR
        federal_cap = weekly_income * p.federal_cap_rate

        return where(exempt, 0, min_(scaled_weekly, federal_cap))
