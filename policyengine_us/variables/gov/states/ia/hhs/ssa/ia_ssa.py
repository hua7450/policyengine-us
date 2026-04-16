from policyengine_us.model_api import *


class ia_ssa(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Iowa State Supplementary Assistance"
    unit = USD
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/code/249.3.pdf",
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.52.pdf",
        "https://hhs.iowa.gov/assistance-programs/state-supplementary-assistance",
    )

    adds = [
        "ia_ssa_blind_supplement",
        "ia_ssa_dp_supplement",
        "ia_ssa_flh_supplement",
        "ia_ssa_ihhrc_supplement",
        "ia_ssa_rcf_supplement",
        "ia_ssa_smme_supplement",
    ]
