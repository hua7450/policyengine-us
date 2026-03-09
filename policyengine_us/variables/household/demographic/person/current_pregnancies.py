from policyengine_us.model_api import *


class current_pregnancies(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "The number of children a pregnant person is expecting"
    defined_for = "is_pregnant"

    def formula(person, period, parameters):
        return 1
