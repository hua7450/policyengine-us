from policyengine_us.model_api import *


class fl_tanf_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Income eligible for Florida Temporary Cash Assistance"
    definition_period = MONTH
    reference = (
        "Florida Statute § 414.095; Florida Administrative Code Rule 65A-4.209"
    )
    documentation = "Gross income must be below 185% FPL and net countable income must not exceed the payment standard."
    defined_for = StateCode.FL

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.fl.dcf.tanf

        # Gross income test (185% FPL)
        gross_income = spm_unit("fl_tanf_gross_income", period.this_year)
        family_size = spm_unit("spm_unit_size", period)

        # Get annual gross income limit
        max_size = max(p.income_limits.gross_income_limit.keys())
        capped_size = min_(family_size, max_size)
        gross_income_limit = p.income_limits.gross_income_limit[capped_size]

        meets_gross_test = gross_income <= gross_income_limit

        # Net income test (countable income <= payment standard)
        countable_income = spm_unit("fl_tanf_countable_income", period)
        payment_standard = spm_unit("fl_tanf_payment_standard", period)

        meets_net_test = countable_income <= payment_standard

        return meets_gross_test & meets_net_test
