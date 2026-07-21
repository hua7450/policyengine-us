from policyengine_us.model_api import *


class wy_ccap_enrolled(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Enrolled in Wyoming Child Care, Purchase of Service"
    definition_period = MONTH
    defined_for = StateCode.WY
    reference = (
        "https://drive.google.com/file/d/1yatL28Yylj62R2cTipV2sGa10TxZplxr/view",  # Wyo. Admin. Rules, DFS, Child Care - Purchase of Service, Ch. 1 §8(e)(i)(N), eff. 05/07/2025 (PDF p. 18)
        "https://drive.google.com/file/d/1VpQ4WE2xQZ_byLcfJgmtyYyBiKr3_ytS/view",  # Wyoming DFS Child Care Subsidy Policy Manual §1201 (PDF p. 1)
    )
    # Distinguishes a unit already receiving assistance (eligible through
    # Sliding Fee Scale Step 6, 225% of the federal poverty guideline, under
    # Manual §1201's transitional/graduated phaseout) from a first-time
    # applicant (the default, held to the Step 4 initial limit of 175% under
    # Manual §1101.A).
