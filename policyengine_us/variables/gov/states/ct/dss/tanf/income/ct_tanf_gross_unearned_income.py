from policyengine_us.model_api import *


class ct_tanf_gross_unearned_income(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Connecticut TFA gross unearned income"
    documentation = "Total gross unearned income for Connecticut TFA. SSI and EITC are excluded per Connecticut policy."
    unit = USD
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    adds = "gov.states.ct.dss.tanf.income.sources.unearned"
