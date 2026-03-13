from policyengine_us.model_api import *
from policyengine_core.periods import period as period_


def create_individual_eitc() -> Reform:
    """Individual-income EITC reform (Winship proposal).

    Computes EITC separately for each spouse based on their individual
    earnings, then sums the results. This differs from baseline EITC
    which uses combined household earnings.

    Reference: https://ifstudies.org/blog/reforming-the-eitc-to-reduce-single-parenthood-and-ease-work-family-balance
    """

    class individual_eitc_base(Variable):
        """Helper variable for computing EITC in simulation branches.

        This variable calculates EITC based on the current simulation's
        filer_adjusted_earnings and adjusted_gross_income inputs.
        Used by get_branch() to compute individual EITC for head/spouse.
        """

        value_type = float
        entity = TaxUnit
        definition_period = YEAR
        label = "Individual EITC base calculation"
        unit = USD
        defined_for = "eitc_eligible"

        def formula(tax_unit, period, parameters):
            maximum = tax_unit("eitc_maximum", period)
            phased_in = tax_unit("eitc_phased_in", period)
            reduction = tax_unit("eitc_reduction", period)
            limitation = max_(0, maximum - reduction)
            return min_(phased_in, limitation)

    class eitc(Variable):
        value_type = float
        entity = TaxUnit
        definition_period = YEAR
        label = "Federal earned income credit"
        reference = "https://www.law.cornell.edu/uscode/text/26/32#a"
        unit = USD
        defined_for = "eitc_eligible"

        def formula(tax_unit, period, parameters):
            p = parameters(period).gov.contrib.individual_eitc
            takes_up_eitc = tax_unit("takes_up_eitc", period)

            # Check if reform is active
            reform_active = p.in_effect

            # Baseline EITC calculation
            maximum = tax_unit("eitc_maximum", period)
            phased_in = tax_unit("eitc_phased_in", period)
            reduction = tax_unit("eitc_reduction", period)
            limitation = max_(0, maximum - reduction)
            baseline_eitc = min_(phased_in, limitation)

            # Reform: compute EITC separately for head and spouse
            person = tax_unit.members
            simulation = tax_unit.simulation
            adj_earnings = person("adjusted_earnings", period)
            is_head = person("is_tax_unit_head", period)
            is_spouse = person("is_tax_unit_spouse", period)

            filer_earned_head_only = tax_unit.sum(adj_earnings * is_head)
            filer_earned_spouse_only = tax_unit.sum(adj_earnings * is_spouse)

            # Calculate head's individual EITC using branch
            head_branch = simulation.get_branch("head_only")
            head_branch.set_input(
                "filer_adjusted_earnings", period, filer_earned_head_only
            )
            head_branch.set_input(
                "adjusted_gross_income", period, filer_earned_head_only
            )
            head_eitc = head_branch.calculate("individual_eitc_base", period)

            # Calculate spouse's individual EITC using branch
            spouse_branch = simulation.get_branch("spouse_only")
            spouse_branch.set_input(
                "filer_adjusted_earnings", period, filer_earned_spouse_only
            )
            spouse_branch.set_input(
                "adjusted_gross_income", period, filer_earned_spouse_only
            )
            spouse_eitc = spouse_branch.calculate("individual_eitc_base", period)

            individual_eitc = head_eitc + spouse_eitc

            # Apply AGI limit if set (0 = no limit)
            agi_limit = p.agi_eitc_limit
            agi = tax_unit("adjusted_gross_income", period)
            agi_eligible = where(agi_limit > 0, agi < agi_limit, True)

            reform_eitc = individual_eitc * agi_eligible

            return where(reform_active, reform_eitc, baseline_eitc) * takes_up_eitc

    class reform(Reform):
        def apply(self):
            self.update_variable(individual_eitc_base)
            self.update_variable(eitc)

    return reform


def create_individual_eitc_reform(parameters, period, bypass: bool = False):
    if bypass:
        return create_individual_eitc()

    p = parameters.gov.contrib.individual_eitc

    reform_active = False
    current_period = period_(period)

    for _ in range(5):
        if p(current_period).in_effect:
            reform_active = True
            break
        current_period = current_period.offset(1, "year")

    if reform_active:
        return create_individual_eitc()
    else:
        return None


individual_eitc_reform = create_individual_eitc_reform(None, None, bypass=True)

# Backward compatibility aliases
winship_reform = individual_eitc_reform
create_eitc_winship_reform = create_individual_eitc_reform
