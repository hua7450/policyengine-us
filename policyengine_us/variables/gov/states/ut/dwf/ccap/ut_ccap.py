from policyengine_us.model_api import *


class ut_ccap(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Utah CCAP benefit amount"
    definition_period = MONTH
    defined_for = "ut_ccap_eligible"
    reference = (
        "https://utrules.elaws.us/uac/r986-700-713",
        "https://utrules.elaws.us/uac/r986-700-707",
    )

    def formula(spm_unit, period, parameters):
        # The subsidy is the lower of the provider's actual established rate
        # (proxied by billed child care expenses) and the summed per-child
        # local market rate caps, less the family co-payment, floored at zero
        # (R986-700-713). The hourly-unit-cost payment path and the CCQS
        # Enhanced Subsidy Grant (R986-700-742) are not modeled.
        maximum_monthly_rate = add(spm_unit, period, ["ut_ccap_market_rate"])
        pre_subsidy_childcare_expenses = spm_unit(
            "spm_unit_pre_subsidy_childcare_expenses", period
        )
        capped_expenses = min_(pre_subsidy_childcare_expenses, maximum_monthly_rate)
        copay = spm_unit("ut_ccap_copay", period)
        return max_(capped_expenses - copay, 0)
