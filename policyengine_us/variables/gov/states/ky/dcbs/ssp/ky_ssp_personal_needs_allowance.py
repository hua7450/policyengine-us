from policyengine_us.model_api import *


class ky_ssp_personal_needs_allowance(Variable):
    value_type = float
    entity = Person
    label = "Kentucky SSP personal needs allowance"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KY
    reference = (
        "https://apps.legislature.ky.gov/law/kar/titles/921/002/015/",
        "https://www.chfs.ky.gov/agencies/dcbs/dfs/Documents/OMVOLV.pdf#page=6",
    )

    def formula(person, period, parameters):
        # Informational only: the PNA is retained by the resident out of
        # the SSP standard paid to the facility, not deducted from ky_ssp.
        category = person.household("ky_ssp_category", period)
        categories = category.possible_values
        p = parameters(period).gov.states.ky.dcbs.ssp.personal_needs_allowance
        monthly_amount = select(
            [category == categories.PCH, category == categories.FCH],
            [p.pch, p.fch],
            default=0,
        )
        return monthly_amount * MONTHS_IN_YEAR
