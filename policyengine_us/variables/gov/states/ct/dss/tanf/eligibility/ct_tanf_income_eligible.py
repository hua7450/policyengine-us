from policyengine_us.model_api import *


class ct_tanf_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA income eligibility"
    documentation = "Whether the household meets Connecticut TFA income requirements. For initial applicants, gross earnings must be under 55% of FPL. For continuing recipients, earned income is excluded up to 100% of FPL, with extended eligibility up to 230% of FPL."
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf

        # Get countable income (this will apply appropriate disregards)
        countable_income = spm_unit("ct_tanf_countable_income", period)

        # Calculate FPL for household size
        size = spm_unit.nb_persons()
        state_group = spm_unit.household("state_group_str", period.this_year)
        fpg = parameters(period).gov.hhs.fpg
        # Get annual FPL and convert to monthly
        annual_fpg = fpg.first_person[state_group] + fpg.additional_person[
            state_group
        ] * max_(size - 1, 0)
        monthly_fpg = annual_fpg / MONTHS_IN_YEAR

        # Initial eligibility: countable income < 55% FPL
        # (Extended eligibility with 100% and 230% FPL thresholds would be implemented
        # when modeling ongoing recipients vs new applicants)
        initial_limit = monthly_fpg * p.income.standards.initial_eligibility

        return countable_income <= initial_limit
