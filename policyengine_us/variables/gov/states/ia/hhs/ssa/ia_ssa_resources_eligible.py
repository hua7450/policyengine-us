from policyengine_us.model_api import *


class ia_ssa_resources_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA resources eligible"
    defined_for = StateCode.IA
    reference = "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.51.pdf"

    def formula(person, period, parameters):
        resources = person("ssi_countable_resources", period.this_year)
        p = parameters(period).gov.ssa.ssi.eligibility.resources.limit
        joint = person("ssi_claim_is_joint", period.this_year)
        limit = where(joint, p.couple, p.individual)
        return resources <= limit
