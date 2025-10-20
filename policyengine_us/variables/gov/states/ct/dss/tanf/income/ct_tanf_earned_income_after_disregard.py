from policyengine_us.model_api import *


class ct_tanf_earned_income_after_disregard(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Connecticut TFA earned income after disregard"
    unit = USD
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = StateCode.CT

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf
        # Use federal TANF gross earned income baseline
        gross_earned = person("tanf_gross_earned_income", period)

        # Apply $90 disregard per person for applicants
        # (Recipients have different eligibility test at income_eligible level)
        return max_(gross_earned - p.income.disregards.initial_disregard, 0)
