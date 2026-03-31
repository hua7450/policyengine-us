from policyengine_us.model_api import *
from policyengine_core.periods import period as period_


def create_wv_eitc() -> Reform:
    class wv_eitc(Variable):
        value_type = float
        entity = TaxUnit
        label = "West Virginia Earned Income Tax Credit"
        unit = USD
        definition_period = YEAR
        defined_for = StateCode.WV

        def formula(tax_unit, period, parameters):
            p = parameters(
                period
            ).gov.contrib.states.wv.child_poverty_impact_dashboard.eitc
            federal_eitc = tax_unit("eitc", period)
            return federal_eitc * p.match

    class wv_refundable_credits(Variable):
        value_type = float
        entity = TaxUnit
        label = "West Virginia refundable tax credits"
        unit = USD
        definition_period = YEAR
        defined_for = StateCode.WV

        def formula(tax_unit, period, parameters):
            wv_eitc_amount = tax_unit("wv_eitc", period)
            other_refundable = add(
                tax_unit,
                period,
                "gov.states.wv.tax.income.credits.refundable",
            )
            return wv_eitc_amount + other_refundable

    class reform(Reform):
        def apply(self):
            self.update_variable(wv_eitc)
            self.update_variable(wv_refundable_credits)

    return reform


def create_wv_eitc_reform(parameters, period, bypass: bool = False):
    if bypass:
        return create_wv_eitc()

    p = parameters.gov.contrib.states.wv.child_poverty_impact_dashboard.eitc

    reform_active = False
    current_period = period_(period)

    for i in range(5):
        p_at_period = p(current_period)
        if p_at_period.in_effect:
            reform_active = True
            break
        current_period = current_period.offset(1, "year")

    if reform_active:
        return create_wv_eitc()
    else:
        return None


wv_eitc = create_wv_eitc_reform(None, None, bypass=True)
