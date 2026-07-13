from policyengine_us.model_api import *


class or_erdc_countable_earned_income(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    unit = USD
    label = "Oregon ERDC countable earned income"
    defined_for = StateCode.OR
    reference = (
        "https://secure.sos.state.or.us/oard/view.action?ruleNumber=414-175-0035"
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states["or"].delc.erdc
        earned = add(person, period, p.income.countable_income.earned_sources)
        # OAR 414-175-0035(21)(a) excludes the earned income of a child; the
        # OAR 414-175-0015(2)(d) filing group counts earned income only from
        # caretakers, proxied program-wide by tax unit heads and spouses.
        caretaker = person("is_tax_unit_head_or_spouse", period.this_year)
        return earned * caretaker
