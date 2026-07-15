from policyengine_us.model_api import *


class ssi(Variable):
    value_type = float
    entity = Person
    label = "SSI"
    documentation = "Supplemental Security Income"
    unit = USD
    definition_period = MONTH
    reference = "https://www.law.cornell.edu/uscode/text/42/1382"

    def formula(person, period, parameters):
        takes_up = person("takes_up_ssi_if_eligible", period.this_year)
        return person("ssi_if_takes_up", period) * takes_up
