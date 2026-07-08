from policyengine_us.model_api import *


class is_head_start_categorically_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Early Head Start or Head Start program eligible"
    definition_period = YEAR
    reference = (
        "https://headstart.gov/policy/45-cfr-chap-xiii/1302-12-determining-verifying-documenting-eligibility",
        "https://www.hhs.gov/answers/programs-for-families-and-children/how-can-i-get-my-child-into-head-start/index.html",
    )

    def formula(person, period, parameters):
        # Person-level: child's own status (not aggregated across family)
        person_eligible = person.household("is_homeless", period) | person(
            "was_in_foster_care", period
        )

        # Family-level: eligible for, or potentially eligible for, public
        # assistance per 45 CFR 1302.12(c)(1)(ii) — receipt is not required,
        # so reported TANF enrollment and a positive calculated tanf amount
        # both qualify.
        tanf_enrolled = person.spm_unit("tanf_enrolled", period)
        family_eligible = tanf_enrolled | (
            add(person.spm_unit, period, ["tanf", "ssi", "snap"]) > 0
        )

        return family_eligible | person_eligible
