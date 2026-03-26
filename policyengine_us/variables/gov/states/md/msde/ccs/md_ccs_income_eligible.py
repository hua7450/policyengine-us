from policyengine_us.model_api import *


class md_ccs_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Maryland Child Care Scholarship (CCS) income eligible"
    definition_period = MONTH
    defined_for = StateCode.MD
    reference = (
        "https://dsd.maryland.gov/regulations/Pages/13A.14.06.03.aspx",
        "https://mgaleg.maryland.gov/2022RS/Chapters_noln/CH_525_hb0275e.pdf",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.md.msde.ccs.income.smi_rate
        countable_income = spm_unit("md_ccs_countable_income", period)
        # TODO: Maryland froze SMI base years for historical periods
        # (FY2019-2022 used 2018 SMI, FY2023-2024 used 2021 SMI).
        # This formula uses the current-year SMI, which is correct for
        # 2025+ but overstates historical thresholds. Follow-up PR
        # should parameterize the SMI base year.
        smi = spm_unit("hhs_smi", period)
        enrolled = spm_unit("md_ccs_enrolled", period)
        income_limit = where(
            enrolled,
            smi * p.continuation,
            smi * p.initial,
        )
        return countable_income <= income_limit
