from policyengine_us.model_api import *


class de_ssp(Variable):
    value_type = float
    entity = Person
    label = "Delaware State Supplementary Payment"
    unit = USD
    definition_period = MONTH
    defined_for = "de_ssp_eligible"
    reference = "https://secure.ssa.gov/poms.nsf/lnx/0501415008PHI"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.de.dhss.ssp.amount
        joint_claim = person("ssi_claim_is_joint", period.this_year)
        per_person_amount = where(joint_claim, p.couple / 2, p.individual)
        uncapped_ssi = person("uncapped_ssi", period)
        reduction = max_(0, -uncapped_ssi)
        supplement = max_(0, per_person_amount - reduction)
        return where(
            joint_claim,
            person.marital_unit.sum(supplement) / 2,
            supplement,
        )
