from policyengine_us.model_api import *


class ct_tanf_gross_unearned_income(Variable):
    value_type = float
    entity = Person
    label = "Connecticut TFA gross unearned income"
    unit = USD
    definition_period = MONTH
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = StateCode.CT

    adds = "gov.states.ct.dss.tanf.income.sources.unearned"
