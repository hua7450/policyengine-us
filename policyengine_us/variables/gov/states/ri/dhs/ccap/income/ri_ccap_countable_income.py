from policyengine_us.model_api import *


class ri_ccap_countable_income(Variable):
    value_type = float
    unit = USD
    entity = SPMUnit
    label = (
        "Rhode Island Child Care Assistance Program (CCAP) countable income"
    )
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.2"
    defined_for = StateCode.RI

    adds = "gov.states.ri.dhs.ccap.income.countable_income.sources"
