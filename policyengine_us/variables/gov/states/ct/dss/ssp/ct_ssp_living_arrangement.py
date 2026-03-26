from policyengine_us.model_api import *


class CTSSPLivingArrangement(Enum):
    COMMUNITY_ALONE = "Community - Living Alone"
    COMMUNITY_SHARED = "Community - Shared Living"
    BOARDING_HOME = "Boarding Home / Residential Care Home"
    SNF = "Skilled Nursing Facility"


class ct_ssp_living_arrangement(Variable):
    value_type = Enum
    entity = Person
    label = "Connecticut SSP living arrangement"
    definition_period = YEAR
    defined_for = StateCode.CT
    possible_values = CTSSPLivingArrangement
    default_value = CTSSPLivingArrangement.COMMUNITY_ALONE
    reference = (
        "https://www.ctdssmap.com/CTPortal/Information/Get/UPM#4520.10",
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ct.html",
    )
