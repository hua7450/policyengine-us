from policyengine_us.model_api import *


class or_erdc_monthly_care_hours(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    unit = "hour"
    label = "Oregon ERDC monthly child care hours"
    defined_for = "or_erdc_eligible_child"
    reference = "https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=7871"

    def formula(person, period, parameters):
        p = parameters(period).gov.states["or"].delc.erdc.hours
        weekly_hours = person("childcare_hours_per_week", period.this_year)
        return min_(
            max_(weekly_hours, 0) * (WEEKS_IN_YEAR / MONTHS_IN_YEAR),
            p.max_monthly,
        )
