from policyengine_us.model_api import *
from policyengine_us.variables.gov.hhs.medicare.savings_programs.category.msp_category import (
    MSPCategory,
)


class msp_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Medicare Savings Program eligible"
    definition_period = MONTH
    reference = (
        "https://www.medicare.gov/basics/costs/help/medicare-savings-programs",
        "https://www.law.cornell.edu/uscode/text/42/1396d#p",
    )

    def formula(person, period, parameters):
        return person("msp_category", period) != MSPCategory.NONE
