from policyengine_us.model_api import *


class or_erdc_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    unit = USD
    label = "Oregon ERDC countable income"
    defined_for = StateCode.OR
    reference = "https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=7871"
    adds = "gov.states.or.delc.erdc.income.countable_income.sources"
