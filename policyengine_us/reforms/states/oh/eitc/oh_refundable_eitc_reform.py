from policyengine_us.model_api import *
from policyengine_core.periods import period as period_


def create_oh_refundable_eitc() -> Reform:
    """
    Ohio Refundable EITC Reform

    Converts the Ohio Earned Income Credit from a nonrefundable credit
    to a refundable credit. By default, OH EITC is nonrefundable.
    """

    class oh_refundable_eitc(Variable):
        value_type = float
        entity = TaxUnit
        label = "Ohio refundable Earned Income Credit"
        unit = USD
        definition_period = YEAR
        defined_for = StateCode.OH

        def formula(tax_unit, period, parameters):
            p = parameters(period).gov.contrib.states.oh.eitc
            oh_eitc = tax_unit("oh_eitc", period)
            return where(p.in_effect, oh_eitc, 0)

    class oh_non_refundable_eitc(Variable):
        value_type = float
        entity = TaxUnit
        label = "Ohio nonrefundable Earned Income Credit"
        unit = USD
        definition_period = YEAR
        defined_for = StateCode.OH

        def formula(tax_unit, period, parameters):
            p = parameters(period).gov.contrib.states.oh.eitc
            oh_eitc = tax_unit("oh_eitc", period)
            # If refundable reform is in effect, nonrefundable portion is 0
            return where(p.in_effect, 0, oh_eitc)

    class oh_non_refundable_credits(Variable):
        value_type = float
        entity = TaxUnit
        label = "Ohio non-refundable credits"
        unit = USD
        definition_period = YEAR
        reference = (
            "https://tax.ohio.gov/static/forms/ohio_individual/individual/2021/sch-cre.pdf",
            "https://tax.ohio.gov/static/forms/ohio_individual/individual/2022/itschedule-credits.pdf",
        )
        defined_for = StateCode.OH

        def formula(tax_unit, period, parameters):
            p = parameters(period).gov.states.oh.tax.income.credits
            # Get all nonrefundable credits except oh_eitc
            credits_list = p.non_refundable
            other_credits = 0
            for credit in [
                "oh_adoption_credit",
                "oh_cdcc",
                "oh_senior_citizen_credit",
                "oh_retirement_credit",
                "oh_non_public_school_credits",
                "oh_exemption_credit",
                "oh_joint_filing_credit",
            ]:
                try:
                    other_credits = other_credits + tax_unit(credit, period)
                except Exception:
                    pass
            # Add the nonrefundable EITC (0 when reform is in effect)
            nonrefundable_eitc = tax_unit("oh_non_refundable_eitc", period)
            return other_credits + nonrefundable_eitc

    class oh_refundable_credits(Variable):
        value_type = float
        entity = TaxUnit
        label = "Ohio refundable credits"
        unit = USD
        definition_period = YEAR
        reference = (
            "https://tax.ohio.gov/static/forms/ohio_individual/individual/2021/sch-cre.pdf",
            "https://tax.ohio.gov/static/forms/ohio_individual/individual/2022/itschedule-credits.pdf",
        )
        defined_for = StateCode.OH

        def formula(tax_unit, period, parameters):
            # Add refundable EITC (positive when reform is in effect)
            return tax_unit("oh_refundable_eitc", period)

    class reform(Reform):
        def apply(self):
            self.update_variable(oh_refundable_eitc)
            self.update_variable(oh_non_refundable_eitc)
            self.update_variable(oh_non_refundable_credits)
            self.update_variable(oh_refundable_credits)

    return reform


def create_oh_refundable_eitc_reform(parameters, period, bypass: bool = False):
    if bypass:
        return create_oh_refundable_eitc()

    p = parameters.gov.contrib.states.oh.eitc

    reform_active = False
    current_period = period_(period)

    for i in range(5):
        if p(current_period).in_effect:
            reform_active = True
            break
        current_period = current_period.offset(1, "year")

    if reform_active:
        return create_oh_refundable_eitc()
    else:
        return None


oh_refundable_eitc = create_oh_refundable_eitc_reform(None, None, bypass=True)
