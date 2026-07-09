from policyengine_us.model_api import *


class oh_ccap_owf_basic_assistance(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    definition_period = MONTH
    label = "Ohio Works First basic assistance for Ohio CCAP income"
    defined_for = StateCode.OH
    reference = "https://codes.ohio.gov/ohio-administrative-code/rule-5180:2-16-03"
