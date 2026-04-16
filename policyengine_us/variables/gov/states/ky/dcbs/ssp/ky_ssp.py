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
        "https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=46358",
        "https://www.chfs.ky.gov/agencies/dcbs/dfs/Documents/OMVOLV.pdf#page=5",
    )

    def formula(person, period):
        # uncapped_ssi can be negative when countable income exceeds the
        # federal SSI benefit. The negative portion reduces the state supplement.
        uncapped_ssi = person("uncapped_ssi", period)
        payment_standard = person("ky_ssp_payment_standard", period)
        income_excess = max_(0, -uncapped_ssi)
        state_supplement = max_(0, payment_standard - income_excess) * person(
            "ky_ssp_eligible", period
        )
        return where(
            person("ssi_claim_is_joint", period),
            person.marital_unit.sum(state_supplement) / 2,
            state_supplement,
        )
