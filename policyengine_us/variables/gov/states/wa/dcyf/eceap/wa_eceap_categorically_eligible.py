from policyengine_us.model_api import *


class wa_eceap_categorically_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Categorically eligible for Washington ECEAP"
    definition_period = YEAR
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=43.216.505",
        "https://app.leg.wa.gov/WAC/default.aspx?cite=110-425-0080",
    )

    def formula(person, period, parameters):
        # Homeless, IEP, and prior Head Start enrollment are the three
        # modelable categorical paths. Indian-child, ESIT, ECLIPSE, and IDEA
        # Part C paths from RCW 43.216.505 are not modeled because we don't
        # track tribal enrollment or these prior-program indicators at the
        # moment. is_enrolled_in_head_start captures current federal Head Start
        # enrollment as a loose proxy for the four statutory prior-participation
        # pathways (Early Head Start, ESIT, birth-to-three ECEAP, IDEA Part C);
        # the proxy understates eligibility for children no longer enrolled.
        is_homeless = person.household("is_homeless", period)
        has_iep = person("has_individualized_education_program", period)
        prior_head_start = person("is_enrolled_in_head_start", period)
        return is_homeless | has_iep | prior_head_start
