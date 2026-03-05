from policyengine_us.model_api import *


class ri_ccap(Variable):
    value_type = float
    entity = SPMUnit
    label = "Rhode Island Child Care Assistance Program (CCAP)"
    unit = USD
    definition_period = MONTH
    defined_for = "ri_ccap_eligible"
    reference = (
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.6",
        "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.12",
    )

    def formula(spm_unit, period, parameters):
        # Sum weekly payments across eligible children
        total_weekly_payment = add(
            spm_unit,
            period,
            ["ri_ccap_per_child_weekly_payment"],
        )
        weekly_copay = spm_unit("ri_ccap_co_payment", period)
        weekly_subsidy = max_(total_weekly_payment - weekly_copay, 0)
        return weekly_subsidy * WEEKS_IN_YEAR / MONTHS_IN_YEAR
