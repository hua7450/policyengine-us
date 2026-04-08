from policyengine_us.model_api import *


class VACCSPCareAgeGroup(Enum):
    INFANT = "Infant"
    TODDLER = "Toddler"
    TWO_YEAR_OLD = "2 year old"
    PRESCHOOL = "Pre-School"
    SCHOOL_AGE = "School Age"


class va_ccsp_care_age_group(Variable):
    value_type = Enum
    possible_values = VACCSPCareAgeGroup
    default_value = VACCSPCareAgeGroup.INFANT
    entity = Person
    definition_period = YEAR
    label = "Virginia CCSP care age group"
    defined_for = StateCode.VA
    reference = "https://ris.dls.virginia.gov/uploads/22VAC40/dibr/VDOE%20Child%20Care%20Program%20Guidance%20Manual%205.3.2023-20240822104447.pdf#page=203"

    def formula(person, period, parameters):
        age = person("age", period)
        return select(
            [age < 1, age < 2, age < 3, age < 6, age < 13],
            [
                VACCSPCareAgeGroup.INFANT,
                VACCSPCareAgeGroup.TODDLER,
                VACCSPCareAgeGroup.TWO_YEAR_OLD,
                VACCSPCareAgeGroup.PRESCHOOL,
                VACCSPCareAgeGroup.SCHOOL_AGE,
            ],
        )
