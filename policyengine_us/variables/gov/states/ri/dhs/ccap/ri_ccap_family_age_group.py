from policyengine_us.model_api import *


class RICCAPFamilyAgeGroup(Enum):
    INFANT_TODDLER = "Infant/Toddler (6 weeks to 3 years)"
    PRESCHOOL = "Preschool (3 years to first grade)"
    SCHOOL_AGE = "School age (first grade to 13 years)"


class ri_ccap_family_age_group(Variable):
    value_type = Enum
    possible_values = RICCAPFamilyAgeGroup
    default_value = RICCAPFamilyAgeGroup.PRESCHOOL
    entity = Person
    label = "Rhode Island CCAP child age group for family and exempt provider rates"
    definition_period = MONTH
    defined_for = StateCode.RI
    reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.12"

    def formula(person, period, parameters):
        age = person("monthly_age", period)
        return select(
            [age < 3, age < 6, age >= 6],
            [
                RICCAPFamilyAgeGroup.INFANT_TODDLER,
                RICCAPFamilyAgeGroup.PRESCHOOL,
                RICCAPFamilyAgeGroup.SCHOOL_AGE,
            ],
        )
