from policyengine_us.model_api import *


class me_ccap_smi_percentage(Variable):
    value_type = float
    entity = SPMUnit
    label = "Maine CCAP income as percentage of SMI"
    unit = "/1"
    definition_period = MONTH
    defined_for = StateCode.ME
    reference = "https://www.maine.gov/dhhs/sites/maine.gov.dhhs/files/inline-files/CCAP%20Full%20Rule%208.18.2025_1.pdf#page=27"

    def formula(spm_unit, period, parameters):
        countable_income = spm_unit("me_ccap_countable_income", period)
        monthly_smi = spm_unit("me_ccap_smi", period)
        mask = monthly_smi > 0
        return np.divide(
            countable_income,
            monthly_smi,
            out=np.zeros_like(countable_income),
            where=mask,
        )
