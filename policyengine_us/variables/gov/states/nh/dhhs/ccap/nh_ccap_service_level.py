from policyengine_us.model_api import *


class NHCCAPServiceLevel(Enum):
    FULL_TIME = "Full-time"
    HALF_TIME = "Half-time"
    PART_TIME = "Part-time"


class nh_ccap_service_level(Variable):
    value_type = Enum
    entity = Person
    possible_values = NHCCAPServiceLevel
    default_value = NHCCAPServiceLevel.FULL_TIME
    definition_period = MONTH
    defined_for = StateCode.NH
    label = "New Hampshire Child Care Scholarship Program service level"
    reference = "https://www.law.cornell.edu/regulations/new-hampshire/N-H-Admin-Code-SS-He-C-6910.07"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.nh.dhhs.ccap.service_level
        hours = person("childcare_hours_per_week", period.this_year)

        return select(
            [
                hours > p.full_time_hours,
                hours > p.half_time_hours,
            ],
            [
                NHCCAPServiceLevel.FULL_TIME,
                NHCCAPServiceLevel.HALF_TIME,
            ],
            default=NHCCAPServiceLevel.PART_TIME,
        )
