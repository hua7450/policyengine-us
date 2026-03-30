from policyengine_us.model_api import *


class is_head_start_categorically_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Early Head Start or Head Start program eligible"
    definition_period = YEAR
    reference = (
        "https://eclkc.ohs.acf.hhs.gov/policy/45-cfr-chap-xiii/1302-12-determining-verifying-documenting-eligibility",
        "https://www.hhs.gov/answers/programs-for-families-and-children/how-can-i-get-my-child-into-head-start/index.html",
    )

    def formula(person, period):
        use_reported = person("head_start_use_reported_programs", period)

        # Person-level: child's own status (not aggregated across family)
        person_eligible = person.household("is_homeless", period) | person(
            "was_in_foster_care", period
        )

        # Family-level: family receives benefits (aggregated at spm_unit)
        family_computed = add(person.spm_unit, period, ["tanf", "ssi", "snap"]) > 0
        family_reported = (
            add(
                person.spm_unit,
                period,
                ["receives_snap", "receives_tanf", "receives_ssi"],
            )
            > 0
        )

        family_eligible = where(use_reported, family_reported, family_computed)
        return family_eligible | person_eligible
