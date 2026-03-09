from policyengine_us.model_api import *


class ri_ccap_copay(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "Rhode Island CCAP family co-payment"
    definition_period = YEAR
    defined_for = StateCode.RI
    reference = (
        "https://rules.sos.ri.gov/regulations/part/218-20-00-4#4.6.1",
        "https://dhs.ri.gov/media/10606/download?language=en",
    )

    def formula(spm_unit, period, parameters):
        # RI Works recipients and housing insecure families pay $0.
        is_tanf_enrolled = spm_unit("is_tanf_enrolled", period)
        is_homeless = spm_unit.household("is_homeless", period)
        exempt_from_copay = is_tanf_enrolled | is_homeless

        copay_rate = spm_unit("ri_ccap_fpl_copay_rate", period)
        countable_income = spm_unit("ri_ccap_countable_income", period)
        copay = countable_income * copay_rate

        return where(exempt_from_copay, 0, copay)
