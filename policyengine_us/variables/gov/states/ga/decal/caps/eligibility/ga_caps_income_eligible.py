from policyengine_us.model_api import *


class ga_caps_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Georgia CAPS based on income"
    definition_period = MONTH
    defined_for = StateCode.GA
    reference = (
        "https://caps.decal.ga.gov/assets/downloads/CAPS/04-CAPS_Policy-Chapter_8.pdf#page=2",
        "https://caps.decal.ga.gov/assets/downloads/CAPS/Appendix_A-CAPS_702_Income_Limits.pdf#page=2",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ga.decal.caps.income.smi_rate
        countable_income = spm_unit("ga_caps_countable_income", period)
        smi = spm_unit("hhs_smi", period)
        enrolled = spm_unit("ga_caps_enrolled", period)
        initial_limit = smi * p.initial_eligibility
        ongoing_limit = smi * p.ongoing_eligibility
        income_limit = where(enrolled, ongoing_limit, initial_limit)
        return countable_income <= income_limit
