import numpy as np

from policyengine_us.model_api import *


# High-confidence tipped occupation groupings from the CPS POCCU2 detailed
# recode. Additional industries let us recover some legal tipped categories
# that are mixed together inside broader CPS occupation buckets.
ALWAYS_ELIGIBLE_OCCUPATION_RECODES = np.array([32, 33])


class tip_income_deduction_occupation_requirement_met(Variable):
    value_type = bool
    entity = Person
    label = "Occupation requirement met for the tip income deduction"
    definition_period = YEAR
    reference = [
        "https://www.irs.gov/forms-pubs/occupations-that-customarily-and-regularly-received-tips-on-or-before-december-31-2024",
        "https://www.irs.gov/irb/2025-42_IRB",
    ]
    documentation = (
        "Approximates the Treasury tipped-occupation list using the CPS "
        "POCCU2 occupation recode and, when available, the CPS A_DTIND "
        "industry recode. If occupation data is unavailable, this returns "
        "true so standalone calculations remain backward compatible."
    )

    def formula(person, period, parameters):
        occupation = person("detailed_occupation_recode", period)
        industry = person("detailed_industry_recode", period)
        is_sstb = person("business_is_sstb", period)
        eligible_industries_by_occupation_recode = parameters(
            period
        ).gov.irs.deductions.tip_income.eligible_industries_by_occupation_recode

        has_no_occupation_data = occupation == 0
        occupation_is_eligible = np.isin(occupation, ALWAYS_ELIGIBLE_OCCUPATION_RECODES)

        for (
            occupation_recode_name
        ) in eligible_industries_by_occupation_recode._children:
            occupation_recode = int(
                occupation_recode_name.removeprefix("occupation_recode_")
            )
            qualifying_industries = getattr(
                eligible_industries_by_occupation_recode,
                occupation_recode_name,
            )
            occupation_is_eligible |= (occupation == occupation_recode) & (
                np.isin(industry, qualifying_industries)
            )

        return (has_no_occupation_data | occupation_is_eligible) & ~is_sstb
