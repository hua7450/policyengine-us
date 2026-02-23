from policyengine_us.model_api import *


class k401_catch_up_limit(Variable):
    value_type = float
    entity = Person
    label = "401(k) catch-up contribution limit"
    unit = USD
    documentation = (
        "The maximum additional 401(k) catch-up contribution allowed "
        "for eligible individuals. SECURE 2.0 provides an enhanced "
        "limit for ages 60-63 starting in 2025."
    )
    definition_period = YEAR
    defined_for = "k401_catch_up_eligible"
    reference = (
        "https://www.law.cornell.edu/cfr/text/26/1.414(v)-1",
        "https://www.law.cornell.edu/uscode/text/26/414#v_2_E",
    )

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(
            period
        ).gov.irs.gross_income.retirement_contributions.catch_up
        return p.limit.k401.calc(age)
