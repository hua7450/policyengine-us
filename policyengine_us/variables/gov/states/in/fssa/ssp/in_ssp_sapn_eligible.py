from policyengine_us.model_api import *


class in_ssp_sapn_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Indiana Supplemental Assistance for Personal Needs"
    definition_period = MONTH
    defined_for = StateCode.IN
    reference = (
        "https://www.in.gov/fssa/ompp/files/Medicaid_PM_5000.pdf",
        "https://secure.ssa.gov/poms.nsf/lnx/0501401001CHI",
    )

    def formula(person, period, parameters):
        is_ssi_eligible = person("is_ssi_eligible", period.this_year)
        # IC 12-15-32-6.5: must be "a recipient of assistance under the federal SSI program"
        is_ssi_recipient = person("ssi", period.this_year) > 0
        is_medicaid_eligible = person("is_medicaid_eligible", period.this_year)
        age = person("age", period.this_year)
        p = parameters(period).gov.states["in"].fssa.ssp
        age_eligible = age >= p.age_threshold
        living_arrangement = person.household("in_ssp_living_arrangement", period)
        in_medicaid_facility = (
            living_arrangement == living_arrangement.possible_values.MEDICAID_FACILITY
        )
        return (
            is_ssi_eligible
            & is_ssi_recipient
            & is_medicaid_eligible
            & age_eligible
            & in_medicaid_facility
        )
