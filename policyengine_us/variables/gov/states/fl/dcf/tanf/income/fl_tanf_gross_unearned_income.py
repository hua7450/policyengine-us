from policyengine_us.model_api import *


class fl_tanf_gross_unearned_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Florida TANF gross unearned income"
    unit = USD
    definition_period = MONTH
    reference = "Florida Administrative Code Rule 65A-4.209"
    documentation = "Gross unearned income for Florida TANF before disregards."
    defined_for = StateCode.FL

    def formula(spm_unit, period, parameters):
        # Major unearned income sources
        unearned_sources = [
            "social_security",
            "unemployment_compensation",
            "alimony_income",
            "child_support_received",
            "gi_cash_assistance",
        ]

        return add(spm_unit, period, unearned_sources)
