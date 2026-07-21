from policyengine_us.model_api import *


class wy_child_care_subsidies(Variable):
    value_type = float
    entity = SPMUnit
    label = "Wyoming child care subsidies"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.WY
    reference = "https://drive.google.com/file/d/1yatL28Yylj62R2cTipV2sGa10TxZplxr/view"  # Wyo. Admin. Rules, DFS, Child Care - Purchase of Service, Ch. 1, eff. 05/07/2025
    adds = ["wy_ccap"]
