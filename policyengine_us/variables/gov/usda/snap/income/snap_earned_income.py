from policyengine_us.model_api import *


class snap_earned_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "SNAP earned income"
    documentation = "Earned income for calculating the SNAP earned income deduction"
    reference = (
        "https://www.law.cornell.edu/cfr/text/7/273.9#b_1",
        "https://www.law.cornell.edu/cfr/text/7/273.11#c",
    )
    unit = USD

    def formula(spm_unit, period, parameters):
        person = spm_unit.members
        earned = person("snap_earned_income_person", period)
        share = person("snap_income_counted_share", period)
        return spm_unit.sum(earned * share)
