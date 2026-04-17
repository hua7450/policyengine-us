from policyengine_us.model_api import *


class ky_ssp(Variable):
    value_type = float
    entity = Person
    label = "Kentucky State Supplementary Payment"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KY
    exhaustive_parameter_dependencies = "gov.states.ky.dcbs.ssp"
    reference = (
        "https://apps.legislature.ky.gov/law/kar/titles/921/002/015/",
        "https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=7671",
        "https://www.chfs.ky.gov/agencies/dcbs/dfs/Documents/OMVOLV.pdf#page=5",
    )

    def formula(person, period):
        # 921 KAR 2:015 §8(2): subtract total countable income from the
        # standard of need in §9.
        payment_standard = person("ky_ssp_payment_standard", period)
        countable_income = person("ssi_countable_income", period)
        state_supplement = max_(0, payment_standard - countable_income) * person(
            "ky_ssp_eligible", period
        )
        # §9(2): "in a couple case, if both are eligible" the couple's income
        # is combined and one-half of the deficit is payable to each. Require
        # both spouses to be actually SSI-eligible (not merely both ABD), per
        # §9(1)(c) which reserves the couple rates for "eligible couple, both
        # aged, blind, or having a disability".
        both_eligible = person.marital_unit.sum(person("is_ssi_eligible", period)) == 2
        return where(
            both_eligible,
            person.marital_unit.sum(state_supplement) / 2,
            state_supplement,
        )
