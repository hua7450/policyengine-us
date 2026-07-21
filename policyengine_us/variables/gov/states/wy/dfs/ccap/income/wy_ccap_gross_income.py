from policyengine_us.model_api import *


class wy_ccap_gross_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Wyoming CCAP gross income"
    definition_period = MONTH
    unit = USD
    defined_for = StateCode.WY
    reference = (
        "https://drive.google.com/file/d/1yatL28Yylj62R2cTipV2sGa10TxZplxr/view",  # Wyo. Admin. Rules, DFS, Child Care - Purchase of Service, Ch. 1, Appendix B, eff. 05/07/2025 (PDF pp. 38-40)
        "https://drive.google.com/file/d/1XWs2Q_duALLgJzG88OthnYJ87XApYZzS/view",  # Wyoming DFS Child Care Subsidy Policy Manual §901.G Table #1 (PDF pp. 2-4)
    )

    adds = "gov.states.wy.dfs.ccap.income.countable_income.sources"
