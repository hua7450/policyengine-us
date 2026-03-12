from policyengine_us.model_api import *


class VTCCFAPCareSchedule(Enum):
    PART_TIME = "Part Time"
    FULL_TIME = "Full Time"
    EXTENDED_CARE = "Extended Care"


class vt_ccfap_care_schedule(Variable):
    value_type = Enum
    entity = Person
    possible_values = VTCCFAPCareSchedule
    default_value = VTCCFAPCareSchedule.FULL_TIME
    definition_period = YEAR
    defined_for = StateCode.VT
    label = "Vermont CCFAP care schedule"
    reference = "https://outside.vermont.gov/dept/DCF/Shared%20Documents/CDD/CCFAP/State-Rates.pdf"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.vt.dcf.ccfap.care_schedule
        hours = person("childcare_hours_per_week", period)
        return select(
            [
                hours <= p.part_time_max,
                hours <= p.full_time_max,
            ],
            [
                VTCCFAPCareSchedule.PART_TIME,
                VTCCFAPCareSchedule.FULL_TIME,
            ],
            default=VTCCFAPCareSchedule.EXTENDED_CARE,
        )
