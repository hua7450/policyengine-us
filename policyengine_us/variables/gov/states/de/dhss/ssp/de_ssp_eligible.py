from policyengine_us.model_api import *


class de_ssp_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Delaware State Supplementary Payment"
    definition_period = MONTH
    defined_for = StateCode.DE
    reference = (
        "https://secure.ssa.gov/apps10/poms.nsf/lnx/0501415058",
        "https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/de.html",
        "https://delcode.delaware.gov/title16/c011/sc01/",
    )

    def formula(person, period, parameters):
        # No uncapped_ssi > 0 check: WorkWorld states that Delaware
        # covers "aged, blind, or disabled adults who are SSI
        # recipients or would qualify except for income." Income
        # overspill is handled in de_ssp via the uncapped_ssi
        # reduction formula.
        # https://help.workworldapp.com/wwwebhelp/ssi_state_supplement_delaware.htm
        is_ssi_eligible = person("is_ssi_eligible", period.this_year)
        age = person("age", period.this_year)
        p = parameters(period).gov.states.de.dhss.ssp
        age_eligible = age >= p.age_threshold
        living_arrangement = person.household("de_ssp_living_arrangement", period)
        in_certified_adult_care_setting = (
            living_arrangement
            == living_arrangement.possible_values.CERTIFIED_ADULT_CARE_SETTING
        )
        return is_ssi_eligible & age_eligible & in_certified_adult_care_setting
