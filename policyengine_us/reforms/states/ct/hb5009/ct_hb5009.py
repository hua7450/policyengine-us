from policyengine_us.model_api import *
from policyengine_core.periods import period as period_


def create_ct_hb5009() -> Reform:
    class ct_property_tax_credit(Variable):
        value_type = float
        entity = TaxUnit
        label = "Connecticut property tax credit"
        unit = USD
        definition_period = YEAR
        defined_for = "ct_property_tax_credit_eligible"

        def formula(tax_unit, period, parameters):
            # Check eligibility first
            eligible = tax_unit("ct_property_tax_credit_eligible", period)

            agi = tax_unit("ct_agi", period)
            filing_status = tax_unit("filing_status", period)

            # Use HB-5009 parameters
            p = parameters(period).gov.contrib.states.ct.hb5009
            baseline = parameters(
                period
            ).gov.states.ct.tax.income.credits.property_tax

            # Get property taxes paid
            real_estate_taxes = add(tax_unit, period, ["real_estate_taxes"])

            # Calculate credit with increased cap
            max_credit = min_(real_estate_taxes, p.cap)

            # Use expanded income thresholds
            income_threshold = p.income_threshold[filing_status]

            # Calculate phase-out using baseline increment and rate
            excess = max_(agi - income_threshold, 0)
            total_increments = np.ceil(
                excess / baseline.reduction.increment[filing_status]
            )
            reduction_percent = baseline.reduction.rate * total_increments
            reduction_amount = max_credit * reduction_percent

            # Apply minimum floor - key structural change
            credit_after_reduction = max_credit - reduction_amount
            minimum_floor = p.minimum

            credit = max_(credit_after_reduction, minimum_floor)

            return eligible * credit

    class reform(Reform):
        def apply(self):
            self.update_variable(ct_property_tax_credit)

    return reform


def create_ct_hb5009_reform(parameters, period, bypass: bool = False):
    if bypass:
        return create_ct_hb5009()

    p = parameters.gov.contrib.states.ct.hb5009

    reform_active = False
    current_period = period_(period)

    for i in range(5):
        if p(current_period).in_effect:
            reform_active = True
            break
        current_period = current_period.offset(1, "year")

    if reform_active:
        return create_ct_hb5009()
    else:
        return None


ct_hb5009 = create_ct_hb5009_reform(None, None, bypass=True)
