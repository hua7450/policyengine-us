from policyengine_us.model_api import *


class is_snap_gross_test_full_income_count_alien(Variable):
    value_type = bool
    entity = Person
    label = (
        "SNAP ineligible alien with fully counted income under the gross income test"
    )
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/cfr/text/7/273.11#c_3_i"

    def formula(person, period, parameters):
        p = parameters(period).gov.usda.snap.income.ineligible_members
        immigration_ineligible = ~person("is_snap_immigration_status_eligible", period)
        status = person("immigration_status", period.this_year).decode_to_str()
        state = person.household("state_code_str", period)
        state_discretion_status = np.isin(status, p.pre_prwora_statuses)
        hybrid_state = np.isin(state, p.gross_test_full_count_states)
        student = person("is_snap_ineligible_student", period)
        return (
            ~student & immigration_ineligible & state_discretion_status & hybrid_state
        )
