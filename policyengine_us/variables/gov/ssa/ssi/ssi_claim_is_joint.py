from policyengine_us.model_api import *
from policyengine_us.variables.gov.ssa.ssi.eligibility.status.ssi_federal_living_arrangement import (
    SSIFederalLivingArrangement,
)


class ssi_claim_is_joint(Variable):
    value_type = bool
    entity = Person
    label = "SSI claim is joint"
    definition_period = YEAR
    reference = (
        "https://www.law.cornell.edu/cfr/text/20/416.414",
        "https://secure.ssa.gov/poms.nsf/lnx/0500501154",
    )

    def formula(person, period, parameters):
        abd_person = person("is_ssi_aged_blind_disabled", period)
        is_head_or_spouse = person("is_tax_unit_head_or_spouse", period)
        eligible_person = abd_person & is_head_or_spouse

        both_eligible = person.marital_unit.sum(eligible_person) > 1

        # 20 CFR 416.414(b)(3): When either spouse is in a medical
        # treatment facility (Medicaid paying >50% of care), benefits
        # are computed as if they were separately eligible individuals.
        # POMS SI 00501.154: Couple computation rules require living
        # in the same household; an institution is not the same household.
        arrangement = person("ssi_federal_living_arrangement", period)
        either_in_facility = (
            person.marital_unit.sum(
                arrangement == SSIFederalLivingArrangement.MEDICAL_TREATMENT_FACILITY
            )
            > 0
        )

        return both_eligible & ~either_in_facility
