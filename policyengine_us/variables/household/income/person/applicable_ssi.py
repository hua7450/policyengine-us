from policyengine_us.model_api import *


class applicable_ssi(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    unit = USD
    label = "Applicable SSI for program income tests"
    documentation = (
        "SSI amount counted in program income tests. Uses calculated ssi "
        "by default. When use_reported_ssi is True, the receives_ssi "
        "flag decides participation: zero without it; with it, a "
        "positive reported_ssi_amount if provided, the calculated ssi "
        "otherwise."
    )

    def formula(person, period, parameters):
        use_reported = person("use_reported_ssi", period.this_year)
        receives = person("receives_ssi", period)
        reported = person("reported_ssi_amount", period)
        computed = person("ssi", period)
        reported_value = receives * where(reported > 0, reported, computed)
        return where(use_reported, reported_value, computed)
