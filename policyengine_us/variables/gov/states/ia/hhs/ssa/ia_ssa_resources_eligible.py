from policyengine_us.model_api import *


class ia_ssa_resources_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA resources eligible"
    defined_for = StateCode.IA
    reference = "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.51.pdf"

    def formula(person, period, parameters):
        individual_resources = person("ssi_countable_resources", period.this_year)
        joint = person("ssi_claim_is_joint", period.this_year)
        # For joint SSI claims, federal SSI counts resources of both spouses
        # against the couple limit. Mirror that rule: compare the combined
        # marital-unit resources to the couple limit rather than each
        # individual amount to the couple limit (which would effectively
        # allow $3,000 per spouse).
        couple_resources = person.marital_unit.sum(individual_resources)
        resources_to_check = where(joint, couple_resources, individual_resources)
        p = parameters(period).gov.ssa.ssi.eligibility.resources.limit
        limit = where(joint, p.couple, p.individual)
        return resources_to_check <= limit
