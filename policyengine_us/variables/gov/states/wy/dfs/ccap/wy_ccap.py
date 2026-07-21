from policyengine_us.model_api import *


class wy_ccap(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Wyoming Child Care, Purchase of Service benefit amount"
    definition_period = MONTH
    defined_for = "wy_ccap_eligible"
    reference = (
        "https://drive.google.com/file/d/1yatL28Yylj62R2cTipV2sGa10TxZplxr/view",  # Wyo. Admin. Rules, DFS, Child Care - Purchase of Service, Ch. 1 §9(c), eff. 05/07/2025 (PDF p. 23)
        "https://drive.google.com/file/d/1XlBkvgwQuX-rIL3eYjkPog1zZ-hi-gD7/view",  # Wyoming DFS Child Care Subsidy Policy Manual §1101.M (PDF p. 2)
    )

    def formula(spm_unit, period, parameters):
        # Rules Ch. 1 §9(c) / Manual §1101.M: DFS pays the lowest of the
        # provider's actual charge, the statewide maximum limit, and the
        # provider's DFS rate for each authorized day of care, summed across
        # eligible children, minus the family copayment, floored at zero.
        # The 16-hour-per-day care cap (§9(k)) and the multi-child family rate
        # cap (§9(m)) are not modeled.
        person = spm_unit.members
        daily_benefit = person("wy_ccap_daily_benefit", period)
        care_days = person("childcare_attending_days_per_month", period.this_year)
        total_reimbursement = spm_unit.sum(daily_benefit * care_days)
        copay = spm_unit("wy_ccap_copay", period)
        return max_(total_reimbursement - copay, 0)
