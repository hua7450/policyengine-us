from policyengine_us.model_api import *


class ct_tanf_demographic_eligible_person(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Connecticut TFA demographic eligibility"
    documentation = "Whether this person meets the demographic requirements for Connecticut Temporary Family Assistance (TFA/TANF) eligibility. Connecticut's age threshold (18) matches the federal TANF definition."
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    def formula(person, period, parameters):
        # Connecticut's age 18 threshold matches federal TANF non-student limit
        # Use federal demographic eligibility variable
        return person("is_person_demographic_tanf_eligible", period)
