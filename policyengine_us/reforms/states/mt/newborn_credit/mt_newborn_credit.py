from policyengine_us.model_api import *
from policyengine_core.periods import period as period_
from policyengine_core.periods import instant


def create_mt_newborn_credit() -> Reform:
    class mt_newborn_credit_eligible_child(Variable):
        value_type = bool
        entity = Person
        label = "Montana newborn credit eligible child"
        definition_period = YEAR
        defined_for = StateCode.MT

        def formula(person, period, parameters):
            p = parameters(period).gov.contrib.states.mt.newborn_credit
            # Child must be under age limit (under 1 year old)
            age = person("age", period)
            age_eligible = age < p.age_limit
            # Must be claimed as dependent
            is_dependent = person("is_tax_unit_dependent", period)
            # Child must have SSN (not ITIN)
            ssn_card_type = person("ssn_card_type", period)
            ssn_types = ssn_card_type.possible_values
            has_ssn = (ssn_card_type == ssn_types.CITIZEN) | (
                ssn_card_type == ssn_types.NON_CITIZEN_VALID_EAD
            )
            return age_eligible & is_dependent & has_ssn

    class mt_newborn_credit_eligible(Variable):
        value_type = bool
        entity = TaxUnit
        label = "Eligible for the Montana newborn credit"
        definition_period = YEAR
        defined_for = StateCode.MT

        def formula(tax_unit, period, parameters):
            # Must have at least $1 of earned income (like EITC requirement)
            earned_income = tax_unit("tax_unit_earned_income", period)
            has_earned_income = earned_income > 0
            # Must have qualifying children
            qualifying_children = add(
                tax_unit, period, ["mt_newborn_credit_eligible_child"]
            )
            has_qualifying_children = qualifying_children > 0
            # Filer (head or spouse) must have SSN
            person = tax_unit.members
            head_or_spouse = person("is_tax_unit_head_or_spouse", period)
            ssn_card_type = person("ssn_card_type", period)
            ssn_types = ssn_card_type.possible_values
            has_ssn = (ssn_card_type == ssn_types.CITIZEN) | (
                ssn_card_type == ssn_types.NON_CITIZEN_VALID_EAD
            )
            filer_has_ssn = tax_unit.any(head_or_spouse & has_ssn)
            return has_earned_income & has_qualifying_children & filer_has_ssn

    class mt_newborn_credit(Variable):
        value_type = float
        entity = TaxUnit
        label = "Montana newborn credit"
        definition_period = YEAR
        unit = USD
        defined_for = "mt_newborn_credit_eligible"

        def formula(tax_unit, period, parameters):
            p = parameters(period).gov.contrib.states.mt.newborn_credit
            # Check if reform is in effect
            in_effect = p.in_effect
            # Count qualifying children
            qualifying_children = add(
                tax_unit, period, ["mt_newborn_credit_eligible_child"]
            )
            # Calculate base credit
            base_credit = p.amount * qualifying_children
            # Calculate phase-out
            filing_status = tax_unit("filing_status", period)
            agi = tax_unit("adjusted_gross_income", period)
            threshold = p.reduction.threshold[filing_status]
            increment = p.reduction.increment
            reduction_amount = p.reduction.amount
            # Number of increments (ceiling - any fraction triggers reduction)
            excess = max_(agi - threshold, 0)
            increments = np.ceil(excess / increment)
            # Calculate reduction
            reduction = reduction_amount * increments
            return in_effect * max_(base_credit - reduction, 0)

    def modify_parameters(parameters):
        # Add mt_newborn_credit to Montana refundable credits list
        refundable = parameters.gov.states.mt.tax.income.credits.refundable
        current_refundable = refundable(instant("2027-01-01"))
        if "mt_newborn_credit" not in current_refundable:
            new_refundable = list(current_refundable) + ["mt_newborn_credit"]
            refundable.update(
                start=instant("2027-01-01"),
                stop=instant("2100-12-31"),
                value=new_refundable,
            )
        return parameters

    class reform(Reform):
        def apply(self):
            self.update_variable(mt_newborn_credit_eligible_child)
            self.update_variable(mt_newborn_credit_eligible)
            self.update_variable(mt_newborn_credit)
            self.modify_parameters(modify_parameters)

    return reform


def create_mt_newborn_credit_reform(parameters, period, bypass: bool = False):
    if bypass:
        return create_mt_newborn_credit()

    p = parameters.gov.contrib.states.mt.newborn_credit

    reform_active = False
    current_period = period_(period)

    for _ in range(5):
        if p(current_period).in_effect:
            reform_active = True
            break
        current_period = current_period.offset(1, "year")

    if reform_active:
        return create_mt_newborn_credit()
    else:
        return None


mt_newborn_credit = create_mt_newborn_credit_reform(None, None, bypass=True)
