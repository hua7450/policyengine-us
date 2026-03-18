from policyengine_us.model_api import *


class person_receives_aca(Variable):
    value_type = bool
    entity = Person
    label = "Person receives ACA"
    documentation = (
        "Whether a person is eligible for ACA premium tax credits and is in a "
        "tax unit with positive assigned ACA premium tax credit."
    )
    definition_period = YEAR

    def formula(person, period, parameters):
        return (person.tax_unit("assigned_aca_ptc", period) > 0) & person(
            "is_aca_ptc_eligible", period
        )
