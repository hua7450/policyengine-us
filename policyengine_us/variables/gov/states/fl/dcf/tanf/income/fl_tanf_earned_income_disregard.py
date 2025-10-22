from policyengine_us.model_api import *


class fl_tanf_earned_income_disregard(Variable):
    value_type = float
    entity = SPMUnit
    label = "Florida TANF earned income disregard"
    unit = USD
    definition_period = MONTH
    reference = "Florida Statute § 414.095 - Earned income disregards"
    documentation = """
    Florida uses a two-step earned income disregard process:
    Step 1: Standard disregard per earner (person with earned income)
    Step 2: Flat amount plus percentage of remainder (work incentive disregard)

    Example with $90 per earner, $200 flat, 50% percentage:
    $1,000 gross earned income, 1 earner
    Step 1: $1,000 - $90 = $910
    Step 2: $910 - $200 = $710
            $710 × 0.5 = $355 (half disregarded)
    Countable: $355
    """
    defined_for = StateCode.FL

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.fl.dcf.tanf.income_disregards

        gross_earned = spm_unit("fl_tanf_gross_earned_income", period)

        # Count number of earners (people with earned income)
        person = spm_unit.members
        has_earned_income = person("employment_income", period) > 0
        num_earners = spm_unit.sum(has_earned_income)

        # Step 1: Standard disregard ($90 per earner, not per person)
        standard_disregard = p.earned_per_person * num_earners
        after_standard = max_(gross_earned - standard_disregard, 0)

        # Step 2: Work incentive disregard ($200 + 50% of remainder)
        after_flat = max_(after_standard - p.earned_flat, 0)
        percentage_disregard = after_flat * p.earned_percentage

        # Total disregard is everything except what's counted
        total_disregard = (
            standard_disregard + p.earned_flat + percentage_disregard
        )

        return min_(total_disregard, gross_earned)
