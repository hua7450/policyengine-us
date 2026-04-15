from policyengine_us.model_api import *


class hi_oss_resides_in_medicaid_institution(Variable):
    value_type = bool
    entity = Person
    label = "Whether person resides in a Medicaid institution where Title XIX pays more than 50% of care cost"
    definition_period = YEAR
    defined_for = StateCode.HI
    reference = "https://secure.ssa.gov/poms.nsf/lnx/0501415210SF"
