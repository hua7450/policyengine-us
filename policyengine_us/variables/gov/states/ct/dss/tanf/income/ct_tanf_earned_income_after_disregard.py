from policyengine_us.model_api import *


class ct_tanf_earned_income_after_disregard(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Connecticut TFA earned income after initial disregard"
    documentation = "Person's earned income after applying the $90 initial application disregard. This is a simplified implementation using the initial disregard; full implementation would distinguish between applicants (use $90 disregard) and recipients (use 100% FPL exclusion)."
    unit = USD
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf
        gross_earned = person("ct_tanf_gross_earned_income", period)
        # Apply $90 disregard per person (initial application)
        disregard = p.income.disregards.initial_disregard
        return max_(gross_earned - disregard, 0)
