from policyengine_us.model_api import *


class RICCAPCenterAgeGroup(Enum):
    INFANT = "Infant (6 weeks to 18 months)"
    TODDLER = "Toddler (18 months to 3 years)"
    PRESCHOOL = "Preschool (3 years to first grade)"
    SCHOOL_AGE = "School age (first grade to 13 years)"


class ri_ccap_center_age_group(Variable):
    value_type = Enum
    possible_values = RICCAPCenterAgeGroup
    default_value = RICCAPCenterAgeGroup.PRESCHOOL
    entity = Person
    label = "Rhode Island CCAP child age group for licensed center rates"
    definition_period = MONTH
    defined_for = StateCode.RI
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.12"

    def formula(person, period, parameters):
        age = person("monthly_age", period)
        return select(
            [age < 1.5, age < 3, age < 6, age >= 6],
            [
                RICCAPCenterAgeGroup.INFANT,
                RICCAPCenterAgeGroup.TODDLER,
                RICCAPCenterAgeGroup.PRESCHOOL,
                RICCAPCenterAgeGroup.SCHOOL_AGE,
            ],
        )
