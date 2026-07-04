from policyengine_us.model_api import *


class is_snap_prorated_income_member(Variable):
    value_type = bool
    entity = Person
    label = "SNAP ineligible member with prorated income"
    definition_period = MONTH
    reference = (
        "https://www.law.cornell.edu/cfr/text/7/273.11#c_2_ii",
        "https://www.law.cornell.edu/cfr/text/7/273.11#c_3",
        "https://www.law.cornell.edu/uscode/text/7/2015#f",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.usda.snap.income.ineligible_members
        immigration_ineligible = ~person("is_snap_immigration_status_eligible", period)
        status = person("immigration_status", period.this_year).decode_to_str()
        state = person.household("state_code_str", period)
        state_discretion_status = np.isin(status, p.pre_prwora_statuses)
        counts_all = np.isin(state, p.count_all_income_states)
        full_count_alien = immigration_ineligible & state_discretion_status & counts_all
        prorated_alien = immigration_ineligible & ~full_count_alien
        # NOTE: All members failing work requirements are prorated under
        # 273.11(c)(2); full counting for 273.7 sanctions under 273.11(c)(1)
        # is not yet modeled.
        fails_work_requirements = ~person("meets_snap_work_requirements_person", period)
        student = person("is_snap_ineligible_student", period)
        return ~student & (prorated_alien | fails_work_requirements)
