from policyengine_us.model_api import *


class snap_enrolled(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "SNAP enrolled"
    documentation = (
        "Whether the SPM unit participates in SNAP, for programs whose "
        "eligibility depends on SNAP receipt. Usually this is whether "
        "the calculated snap amount is positive. If use_reported_snap "
        "is True, the reported receives_snap input is used instead and "
        "the calculated snap amount is ignored. The snap variable "
        "itself is never affected."
    )
    reference = "https://www.law.cornell.edu/uscode/text/7/2017"

    def formula(spm_unit, period, parameters):
        use_reported = spm_unit("use_reported_snap", period.this_year)
        reported = spm_unit("receives_snap", period)
        computed = spm_unit("snap", period) > 0
        return where(use_reported, reported, computed)
