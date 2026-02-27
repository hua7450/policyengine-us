from policyengine_us.model_api import *


class mt_tanf_payment_standard(Variable):
    value_type = float
    entity = SPMUnit
    label = "Montana Temporary Assistance for Needy Families (TANF) payment standard"
    unit = USD
    definition_period = MONTH
    reference = (
        "https://dphhs.mt.gov/assets/hcsd/TANF/TANFStatePlan.pdf#page=10"
    )
    defined_for = StateCode.MT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.mt.dhs.tanf
        p_standards = p.income_standards
        # Montana pins the payment standard to a specific historical FPL year.
        pinned_year = int(p_standards.payment_fpg_year)
        instant_str = f"{pinned_year}-01-01"
        p_fpg = parameters(instant_str).gov.hhs.fpg
        n = spm_unit("mt_tanf_assistance_unit_size", period)
        capped_size = min_(n, p.max_unit_size)
        state_group = spm_unit.household("state_group_str", period)
        monthly_fpg = (
            p_fpg.first_person[state_group]
            + p_fpg.additional_person[state_group] * (capped_size - 1)
        ) / MONTHS_IN_YEAR
        return monthly_fpg * p_standards.payment_fpg_rate
