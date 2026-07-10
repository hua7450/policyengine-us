from policyengine_us.model_api import *


class ok_ccs(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Oklahoma Child Care Subsidy benefit amount"
    definition_period = MONTH
    defined_for = "ok_ccs_eligible"
    reference = (
        "https://oklahoma.gov/content/dam/ok/en/okdhs/documents/searchcenter/okdhsformresults/c-4.pdf#page=1",
        "https://oklahoma.gov/content/dam/ok/en/okdhs/documents/searchcenter/okdhsformresults/c-4-b.pdf#page=1",
    )

    def formula(spm_unit, period, parameters):
        # OKDHS pays the provider a daily rate for each day of care, capped at
        # the family's child care charges, and the family pays the family
        # share copayment directly to the provider (Appendix C-4). Blended and
        # weekly unit types, special needs add-on rates, non-traditional hours
        # payments, the Child Welfare $5 per day add-on, Community Hope Center
        # rates, and absent day payments are not modeled.
        person = spm_unit.members
        daily_rate = person("ok_ccs_daily_rate", period)
        days = person("childcare_attending_days_per_month", period.this_year)
        pre_subsidy_per_child = person("pre_subsidy_childcare_expenses", period)
        per_child_payment = min_(daily_rate * days, pre_subsidy_per_child)
        total_payment = spm_unit.sum(per_child_payment)
        copay = spm_unit("ok_ccs_copay", period)
        return max_(total_payment - copay, 0)
