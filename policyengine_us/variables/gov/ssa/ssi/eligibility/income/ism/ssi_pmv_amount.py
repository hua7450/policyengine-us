from policyengine_us.model_api import *


class ssi_pmv_amount(Variable):
    value_type = float
    entity = Person
    label = "SSI presumed maximum value amount"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.law.cornell.edu/cfr/text/20/416.1140",
        "https://secure.ssa.gov/poms.nsf/lnx/0500835300",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.ssa.ssi
        # Per POMS SI 00835.300: use the couple FBR when the person is
        # part of an eligible couple or when spousal deeming applies.
        is_joint = person("ssi_claim_is_joint", period)
        deeming_applies = person("is_ssi_spousal_deeming_applies", period)
        applicable_fbr = where(
            is_joint | deeming_applies,
            p.amount.couple,
            p.amount.individual,
        )
        # PMV = (1/3 × applicable FBR) + $20 general income exclusion
        pmv_monthly = (
            applicable_fbr * p.income.ism.pmv_fbr_fraction + p.income.exclusions.general
        )
        # For eligible couples, the PMV is per-couple; divide by 2
        # so each person's ISM reflects their individual share.
        per_person_monthly = where(is_joint, pmv_monthly / 2, pmv_monthly)
        return per_person_monthly * MONTHS_IN_YEAR
