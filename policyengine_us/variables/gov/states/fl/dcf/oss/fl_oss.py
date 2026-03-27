from policyengine_us.model_api import *


class fl_oss(Variable):
    value_type = float
    entity = Person
    label = "Florida Optional State Supplementation"
    unit = USD
    definition_period = MONTH
    defined_for = "fl_oss_eligible"
    reference = (
        "https://www.flrules.org/gateway/RuleNo.asp?title=PUBLIC%20ASSISTANCE&ID=65A-2.036",
        "https://www.myflfamilies.com/sites/default/files/2024-10/Appendix%20A-12%20OSS%20Payment%20Standards.pdf",
    )

    def formula(person, period, parameters):
        pna = parameters(period).gov.states.fl.dcf.oss.pna
        provider_rate = person("fl_oss_provider_rate", period)
        total_needs = provider_rate + pna
        countable_income = person("ssi_countable_income", period)
        max_oss = person("fl_oss_max_oss", period)
        return min_(max_(total_needs - countable_income, 0), max_oss)
