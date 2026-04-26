from policyengine_us.model_api import *


class wa_pte_age_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Age-eligible for the Washington Senior Citizens and Disabled Persons Property Tax Exemption"
    definition_period = MONTH
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=84.36.381",
        "https://app.leg.wa.gov/WAC/default.aspx?cite=458-16A-130",
        "https://dor.wa.gov/sites/default/files/2022-02/PTExemption_Senior.pdf#page=1",
    )

    def formula(person, period, parameters):
        age = person("age", period.this_year)
        p = parameters(
            period
        ).gov.states.wa.dor.property_tax_exemption.senior_disabled.eligibility
        return age >= p.age_threshold
