from policyengine_us.model_api import *


class snap_gross_test_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "SNAP gross income for the gross income test"
    reference = (
        "https://www.law.cornell.edu/uscode/text/7/2014#c",
        "https://www.law.cornell.edu/cfr/text/7/273.11#c_3_i",
    )
    unit = USD

    def formula(spm_unit, period, parameters):
        # Certain states count the full income of certain ineligible aliens
        # under the gross income test while prorating it under the net
        # income test.
        gross_income = spm_unit("snap_gross_income", period)
        person = spm_unit.members
        full_count_gross = person("is_snap_gross_test_full_income_count_alien", period)
        income = person("snap_earned_income_person", period) + person(
            "snap_unearned_income_person", period
        )
        fraction = spm_unit("snap_prorated_income_fraction", period)
        excluded_share = spm_unit.sum(full_count_gross * income) * (1 - fraction)
        return gross_income + excluded_share
