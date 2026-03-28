import numpy as np

from policyengine_us.model_api import *


# High-confidence tipped occupation groupings from the CPS POCCU2 detailed
# recode. Additional industries let us recover some legal tipped categories
# that are mixed together inside broader CPS occupation buckets.
ALWAYS_ELIGIBLE_OCCUPATION_RECODES = np.array([32, 33])
ELIGIBLE_INDUSTRIES_BY_OCCUPATION_RECODE = {
    23: np.array([44, 45, 50]),  # Entertainment, events, private events
    35: np.array([45, 48, 50]),  # Hotel/home cleaning and housekeeping
    36: np.array([44]),  # Gaming supervisors
    37: np.array([44, 45, 48, 50]),  # Gaming, hospitality, personal services
    39: np.array([44]),  # Gambling cashiers/change persons
    40: np.array([45]),  # Hotel front desk clerks
    49: np.array([46, 48]),  # Bakers, tailors, tattoo/piercing workers
    50: np.array([44, 45]),  # Tour and recreational pilots
    51: np.array([23, 44, 45, 50]),  # Valet, taxi, shuttle, delivery, movers
}


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

        has_no_occupation_data = occupation == 0
        occupation_is_eligible = np.isin(occupation, ALWAYS_ELIGIBLE_OCCUPATION_RECODES)

        for (
            occupation_recode,
            qualifying_industries,
        ) in ELIGIBLE_INDUSTRIES_BY_OCCUPATION_RECODE.items():
            occupation_is_eligible |= (occupation == occupation_recode) & (
                np.isin(industry, qualifying_industries)
            )

        return (has_no_occupation_data | occupation_is_eligible) & ~is_sstb
