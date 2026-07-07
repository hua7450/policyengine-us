from policyengine_us.model_api import *


class meets_snap_gross_income_test(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Meets SNAP gross income test"
    documentation = "Whether this SPM unit meets the SNAP gross income test"
    definition_period = MONTH
    reference = (
        "https://www.law.cornell.edu/uscode/text/7/2017#a",
        "https://www.law.cornell.edu/uscode/text/7/2014#c",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.usda.snap.income.limit
        # The gross test uses state-specific income counting for certain
        # ineligible aliens, unlike the plain gross income used elsewhere
        # (e.g., the TANF non-cash gross income test).
        income = spm_unit("snap_gross_test_income", period)
        fpg = spm_unit("snap_fpg", period)
        # Households with elderly and disabled people are exempt from the
        # gross income test.
        has_elderly_disabled = spm_unit("has_usda_elderly_disabled", period)
        return has_elderly_disabled | (income <= p.gross * fpg)
