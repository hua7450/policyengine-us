from policyengine_us.model_api import *
from policyengine_us.variables.gov.ssa.ssi.eligibility.income._apply_ssi_exclusions import (
    _apply_ssi_exclusions,
)


class msp_countable_income(Variable):
    value_type = float
    entity = Person
    unit = USD
    label = "Medicare Savings Program countable monthly income"
    definition_period = MONTH
    reference = (
        "https://www.law.cornell.edu/uscode/text/42/1396d#p",
        "https://www.law.cornell.edu/cfr/text/20/416.1163",
        "https://secure.ssa.gov/apps10/poms.nsf/lnx/0501715010",
        "https://www.medicare.gov/basics/costs/help/medicare-savings-programs",
    )
    documentation = """
    MSP countable income uses SSI methodology per 42 U.S.C. 1396d(p)(1)(B),
    which specifies income "determined under section 1382a" (SSI rules).
    This applies the standard SSI exclusions:
    1. $20 general income exclusion (from unearned first)
    2. $65 earned income exclusion
    3. 50% of remaining earned income excluded
    """

    def formula(person, period, parameters):
        year = period.this_year
        both_eligible = person("ssi_marital_both_eligible", year)

        blind_or_disabled_working_student_exclusion = person(
            "ssi_blind_or_disabled_working_student_exclusion", year
        )
        personal_earned_income = max_(
            person("ssi_earned_income", year)
            - blind_or_disabled_working_student_exclusion,
            0,
        )
        personal_unearned_income = person("ssi_unearned_income", year)

        spouse_earned_income = person(
            "ssi_earned_income_deemed_from_ineligible_spouse", year
        )
        spouse_unearned_income = person(
            "ssi_unearned_income_deemed_from_ineligible_spouse", year
        )
        spouse_deemed_income = spouse_earned_income + spouse_unearned_income

        ssi = parameters(year).gov.ssa.ssi
        deeming_applies = spouse_deemed_income > (
            (ssi.amount.couple - ssi.amount.individual) * MONTHS_IN_YEAR
        )

        annual_countable = where(
            both_eligible,
            # MSP compares the full couple income to the couple FPG, not SSI's
            # per-spouse half used for benefit amounts.
            _apply_ssi_exclusions(
                max_(
                    person("ssi_marital_earned_income", year)
                    - person.marital_unit.sum(
                        blind_or_disabled_working_student_exclusion
                    ),
                    0,
                ),
                person("ssi_marital_unearned_income", year),
                parameters,
                year,
            ),
            where(
                deeming_applies,
                _apply_ssi_exclusions(
                    personal_earned_income + spouse_earned_income,
                    personal_unearned_income + spouse_unearned_income,
                    parameters,
                    year,
                ),
                _apply_ssi_exclusions(
                    personal_earned_income,
                    personal_unearned_income,
                    parameters,
                    year,
                ),
            ),
        )
        return annual_countable / MONTHS_IN_YEAR
