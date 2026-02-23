from policyengine_us.model_api import *
from policyengine_core.periods import period as period_
from policyengine_core.periods import instant


def create_ct_tax_rebate_2026() -> Reform:
    class ct_tax_rebate_2026(Variable):
        value_type = float
        entity = TaxUnit
        label = "Connecticut 2026 tax rebate"
        unit = USD
        definition_period = YEAR
        defined_for = StateCode.CT

        def formula(tax_unit, period, parameters):
            p = parameters(period).gov.contrib.states.ct.tax_rebate_2026

            filing_status = tax_unit("filing_status", period)
            agi = tax_unit("adjusted_gross_income", period)

            threshold = p.income_threshold[filing_status]
            amount = p.amount[filing_status]

            eligible = agi <= threshold
            return eligible * amount

    def modify_parameters(parameters):
        parameters.gov.states.ct.tax.income.credits.refundable.update(
            start=instant("2026-01-01"),
            stop=instant("2026-12-31"),
            value=["ct_eitc", "ct_tax_rebate_2026"],
        )
        return parameters

    class reform(Reform):
        def apply(self):
            self.update_variable(ct_tax_rebate_2026)
            self.modify_parameters(modify_parameters)

    return reform


def create_ct_tax_rebate_2026_reform(parameters, period, bypass: bool = False):
    if bypass:
        return create_ct_tax_rebate_2026()

    p = parameters.gov.contrib.states.ct.tax_rebate_2026

    reform_active = False
    current_period = period_(period)

    for i in range(5):
        if p(current_period).in_effect:
            reform_active = True
            break
        current_period = current_period.offset(1, "year")

    if reform_active:
        return create_ct_tax_rebate_2026()
    else:
        return None


ct_tax_rebate_2026 = create_ct_tax_rebate_2026_reform(None, None, bypass=True)
