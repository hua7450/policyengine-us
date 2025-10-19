from policyengine_us.model_api import *


class ct_tanf_immigration_status_eligible_person(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Connecticut TFA immigration status eligibility"
    documentation = "Whether this person meets Connecticut's immigration status requirements for TFA. Connecticut follows federal immigration eligibility rules."
    reference = "CGS § 17b-112"
    defined_for = StateCode.CT

    def formula(person, period, parameters):
        # Connecticut follows federal immigration eligibility
        return person("is_citizen_or_legal_immigrant", period)
