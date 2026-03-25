from policyengine_us.model_api import *


class DEPOCAgeGroup(Enum):
    INFANT = "Infant"
    TODDLER = "Toddler"
    PRESCHOOL = "Preschool"
    SCHOOL_AGE_FULL_TIME = "School Age Full-time"
    SCHOOL_AGE_PART_TIME = "School Age Part-time"


class de_poc_age_group(Variable):
    value_type = Enum
    entity = Person
    possible_values = DEPOCAgeGroup
    default_value = DEPOCAgeGroup.PRESCHOOL
    definition_period = MONTH
    label = "Delaware Purchase of Care child care age group"
    defined_for = StateCode.DE
    reference = "https://dhss.delaware.gov/dss/childcr/"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.de.dss.poc
        age = person("age", period.this_year)
        base_group = p.age_group.calc(age)
        hours_per_day = person("childcare_hours_per_day", period.this_year)
        is_school_age_part_time = (base_group == 3) & (
            hours_per_day < p.full_time_hours_per_day
        )
        return where(
            is_school_age_part_time,
            DEPOCAgeGroup.SCHOOL_AGE_PART_TIME,
            base_group,
        )
