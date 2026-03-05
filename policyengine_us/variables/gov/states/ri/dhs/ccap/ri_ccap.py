from policyengine_us.model_api import *


class ri_ccap(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Rhode Island Child Care Assistance Program"
    reference = (
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.2",
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3",
    )
    unit = USD
    defined_for = "ri_ccap_eligible"

    def formula(spm_unit, period, parameters):
        # Per 218-RICR-20-00-4.2(A)(1): allowable child care expense =
        # total authorized care cost - family share (co-payment)
        expenses = add(spm_unit, period, ["pre_subsidy_childcare_expenses"])
        co_payment = spm_unit("ri_ccap_co_payment", period)
        return max_(expenses - co_payment, 0)
