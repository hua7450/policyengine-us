from policyengine_us.model_api import *
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

            in_effect = p.in_effect
            filing_status = tax_unit("filing_status", period)
            agi = tax_unit("adjusted_gross_income", period)

            threshold = p.income_threshold[filing_status]
            amount = p.amount[filing_status]

            eligible = agi <= threshold
            rebate = where(eligible, amount, 0)
            return where(in_effect, rebate, 0)

    def modify_parameters(parameters):
        refundable = parameters.gov.states.ct.tax.income.credits.refundable
        current_refundable = refundable(instant("2026-01-01"))
        if "ct_tax_rebate_2026" not in current_refundable:
            new_refundable = list(current_refundable) + ["ct_tax_rebate_2026"]
            refundable.update(
                start=instant("2026-01-01"),
                stop=instant("2026-12-31"),
                value=new_refundable,
            )
        return parameters

    class reform(Reform):
        def apply(self):
            self.update_variable(ct_tax_rebate_2026)
            self.modify_parameters(modify_parameters)

    return reform


def create_ct_tax_rebate_2026_reform(parameters, period, bypass: bool = False):
    # Always return the reform - the in_effect check happens via parameter toggle
    return create_ct_tax_rebate_2026()


ct_tax_rebate_2026 = create_ct_tax_rebate_2026_reform(None, None, bypass=True)
