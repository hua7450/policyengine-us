from policyengine_us.model_api import *


class ia_ssa_resides_in_residential_care_facility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA resides in licensed residential care facility"
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.52.pdf#page=2",
        "https://www.legis.iowa.gov/docs/code/135C.1.pdf",
    )
