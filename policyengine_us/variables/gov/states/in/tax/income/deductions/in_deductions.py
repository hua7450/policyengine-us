from policyengine_us.model_api import *


class in_deductions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Indiana deductions"
    unit = USD
    definition_period = YEAR
    reference = "http://iga.in.gov/legislative/laws/2021/ic/titles/006#6-3"
    defined_for = StateCode.IN

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states["in"].tax.income.deductions
        base = add(tax_unit, period, p.deductions)
        obbba_vars = p.obbba_conformity_deductions
        if len(obbba_vars) > 0:
            base = base + add(tax_unit, period, obbba_vars)
        return base
