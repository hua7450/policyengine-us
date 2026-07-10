from policyengine_us.model_api import *


class sd_cca(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "South Dakota Child Care Assistance benefit amount"
    definition_period = MONTH
    defined_for = "sd_cca_eligible"
    reference = (
        "https://dss.sd.gov/docs/childcare/assistance/Subsidy_Manual.pdf#page=21"
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.sd.dss.cca.rates
        # Only the weekly region-based rate schedule (effective 2026-08-03) is
        # modeled; the earlier hourly county-based schedule is deferred to a
        # follow-up implementation, so no benefit is paid before that date.
        if not p.uses_weekly_rates:
            return 0
        # The benefit is the lesser of the summed per-child weekly maximum rates
        # (converted to a monthly amount) and the family's billed child care
        # expenses, minus the monthly co-payment, floored at zero. The
        # special-needs multiplier is already folded into sd_cca_weekly_rate, so
        # it sits inside the expense cap. Billed expenses are a single SPM-unit
        # input, so the per-child maximum rates are pooled across the unit.
        person = spm_unit.members
        is_eligible_child = person("sd_cca_eligible_child", period)
        weekly_rate = person("sd_cca_weekly_rate", period)
        weekly_to_monthly = WEEKS_IN_YEAR / MONTHS_IN_YEAR
        max_reimbursement = (
            spm_unit.sum(weekly_rate * is_eligible_child) * weekly_to_monthly
        )
        actual_expenses = spm_unit("spm_unit_pre_subsidy_childcare_expenses", period)
        capped_expenses = min_(actual_expenses, max_reimbursement)
        copay = spm_unit("sd_cca_copay", period)
        return max_(capped_expenses - copay, 0)
