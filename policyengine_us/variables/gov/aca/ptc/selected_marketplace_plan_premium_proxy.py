from policyengine_us.model_api import *


class selected_marketplace_plan_premium_proxy(Variable):
    value_type = float
    entity = TaxUnit
    label = "Selected marketplace plan premium proxy"
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        aca_ptc = tax_unit("aca_ptc", period)
        return where(
            aca_ptc > 0,
            tax_unit("slcsp", period)
            * tax_unit("selected_marketplace_plan_benchmark_ratio", period),
            0,
        )
