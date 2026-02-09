from policyengine_us.model_api import *


class ia_fip_gross_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Iowa FIP gross income eligible"
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/regulations/iowa/Iowa-Admin-Code-r-441-41-27"
    defined_for = StateCode.IA

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ia.hhs.fip
        unit_size = spm_unit("spm_unit_size", period.this_year)
        capped_size = min_(unit_size, p.benefit.max_unit_size)
        standard_of_need = p.standard_of_need.amount.calc(capped_size)
        additional = where(
            unit_size > p.benefit.max_unit_size,
            (unit_size - p.benefit.max_unit_size)
            * p.standard_of_need.additional_person,
            0,
        )
        gross_limit = (
            standard_of_need + additional
        ) * p.income.gross_income_test.rate
        gross_income = spm_unit("ia_fip_gross_income", period)
        return gross_income <= gross_limit
