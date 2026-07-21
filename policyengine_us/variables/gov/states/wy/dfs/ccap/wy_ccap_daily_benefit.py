from policyengine_us.model_api import *


class wy_ccap_daily_benefit(Variable):
    value_type = float
    entity = Person
    unit = USD
    label = "Wyoming CCAP daily benefit per child"
    definition_period = MONTH
    defined_for = "wy_ccap_eligible_child"
    reference = (
        "https://drive.google.com/file/d/1yatL28Yylj62R2cTipV2sGa10TxZplxr/view",  # Wyo. Admin. Rules, DFS, Child Care - Purchase of Service, Ch. 1 §9(c), eff. 05/07/2025 (PDF p. 23)
        "https://drive.google.com/file/d/1XlBkvgwQuX-rIL3eYjkPog1zZ-hi-gD7/view",  # Wyoming DFS Child Care Subsidy Policy Manual §1101.M (PDF p. 2)
    )

    def formula(person, period, parameters):
        # Manual §1101.M: DFS pays the lowest of the provider's actual charge,
        # the statewide limit, and the DFS provider rate. The Table I maximum
        # rates are the statewide limits; the provider-specific registered DFS
        # rate is not tracked, so the modeled legs are the Table I maximum and
        # the actual charge (the pre-subsidy expense spread over attended
        # days).
        max_rate = person("wy_ccap_max_rate", period)
        pre_subsidy_expense = person("pre_subsidy_childcare_expenses", period)
        care_days = person("childcare_attending_days_per_month", period.this_year)
        mask = care_days > 0
        daily_charge = np.divide(
            pre_subsidy_expense,
            care_days,
            out=np.zeros_like(pre_subsidy_expense, dtype=float),
            where=mask,
        )
        return max_(min_(max_rate, daily_charge), 0)
