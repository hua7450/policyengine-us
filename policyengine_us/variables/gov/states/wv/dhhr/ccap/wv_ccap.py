from policyengine_us.model_api import *


class wv_ccap(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "West Virginia CCAP benefit amount"
    definition_period = MONTH
    defined_for = "wv_ccap_eligible"
    reference = (
        "https://bfa.wv.gov/media/6766/download?inline#page=66",
        "https://bfa.wv.gov/media/39915/download?inline#page=42",
    )

    def formula(spm_unit, period, parameters):
        copay = spm_unit("wv_ccap_copay", period)
        person = spm_unit.members
        daily_benefit = person("wv_ccap_daily_benefit", period)
        days_per_week = person("childcare_days_per_week", period.this_year)
        days_per_month = days_per_week * (WEEKS_IN_YEAR / MONTHS_IN_YEAR)
        total_reimbursement = spm_unit.sum(daily_benefit * days_per_month)
        pre_subsidy_childcare_expenses = spm_unit(
            "spm_unit_pre_subsidy_childcare_expenses", period
        )
        uncapped = max_(pre_subsidy_childcare_expenses - copay, 0)
        return min_(uncapped, total_reimbursement)
