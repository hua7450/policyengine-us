from policyengine_us.model_api import *


class ri_ccap_assets(Variable):
    value_type = float
    entity = SPMUnit
    label = "Rhode Island CCAP countable assets"
    definition_period = YEAR
    unit = USD
    defined_for = StateCode.RI
    reference = "https://rules.sos.ri.gov/regulations/part/218-20-00-4#4.6.1"

    adds = "gov.states.ri.dhs.ccap.assets.sources"
