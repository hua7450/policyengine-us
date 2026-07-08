from policyengine_us.model_api import *


class tanf_enrolled(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "TANF enrolled"
    documentation = (
        "Whether the SPM unit participates in TANF, for programs whose "
        "eligibility depends on TANF receipt. Usually this is whether "
        "the calculated tanf amount is positive. If use_reported_tanf "
        "is True, this instead follows the is_tanf_enrolled flag alone "
        "— even when the calculated tanf amount is zero, and no matter "
        "what reported_tanf_amount says. The tanf variable itself is "
        "never affected; programs that count TANF dollars use "
        "applicable_tanf."
    )
    reference = "https://www.law.cornell.edu/uscode/text/42/601"

    def formula(spm_unit, period, parameters):
        use_reported = spm_unit("use_reported_tanf", period.this_year)
        enrolled = spm_unit("is_tanf_enrolled", period)
        computed = spm_unit("tanf", period) > 0
        return where(use_reported, enrolled, computed)
