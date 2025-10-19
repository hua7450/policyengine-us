from policyengine_us.model_api import *


class ct_tanf_gross_earned_income(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Connecticut TFA gross earned income"
    documentation = "Total gross earned income for Connecticut TFA, using federal TANF baseline income sources."
    unit = USD
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    adds = "gov.states.ct.dss.tanf.income.sources.earned"
