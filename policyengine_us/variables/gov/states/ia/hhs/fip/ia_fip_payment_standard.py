from policyengine_us.model_api import *


class ia_fip_payment_standard(Variable):
    value_type = float
    entity = SPMUnit
    label = "Iowa FIP payment standard"
    unit = USD
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/regulations/iowa/Iowa-Admin-Code-r-441-41-28"
    defined_for = StateCode.IA

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ia.hhs.fip
        unit_size = spm_unit("spm_unit_size", period.this_year)
        capped_size = min_(unit_size, p.benefit.max_unit_size)
        base_amount = p.payment_standard.amount.calc(capped_size)
        additional = where(
            unit_size > p.benefit.max_unit_size,
            (unit_size - p.benefit.max_unit_size)
            * p.payment_standard.additional_person,
            0,
        )
        return base_amount + additional
