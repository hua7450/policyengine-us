from policyengine_us.model_api import *


class al_ssp_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Alabama SSP eligible"
    definition_period = MONTH
    defined_for = StateCode.AL
    reference = (
        "https://admincode.legislature.state.al.us/api/chapter/660-2-4#page=9",
        "https://help.workworldapp.com/wwwebhelp/ssi_state_supplement_alabama.htm",
    )

    def formula(person, period, parameters):
        is_ssi_eligible = person("is_ssi_eligible", period.this_year)
        receives_ssi = person("uncapped_ssi", period) > 0
        living_arrangement = person("al_ssp_living_arrangement", period)
        in_qualifying_arrangement = (
            living_arrangement != living_arrangement.possible_values.NONE
        )
        return is_ssi_eligible & receives_ssi & in_qualifying_arrangement
