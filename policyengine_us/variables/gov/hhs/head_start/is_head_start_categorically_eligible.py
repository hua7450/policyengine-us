from policyengine_us.model_api import *


class is_head_start_categorically_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Early Head Start or Head Start program eligible"
    definition_period = YEAR
    reference = (
        "https://eclkc.ohs.acf.hhs.gov/policy/45-cfr-chap-xiii/1302-12-determining-verifying-documenting-eligibility"
        "https://www.hhs.gov/answers/programs-for-families-and-children/how-can-i-get-my-child-into-head-start/index.html"
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.hhs.head_start
        use_reported = person("head_start_use_reported_programs", period)

        computed = add(person.spm_unit, period, p.categorical_eligibility) > 0

        reported = add(person.spm_unit, period, p.reported_categorical_eligibility) > 0

        return where(use_reported, reported, computed)
