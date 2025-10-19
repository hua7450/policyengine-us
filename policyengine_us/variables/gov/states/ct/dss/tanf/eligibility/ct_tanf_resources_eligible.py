from policyengine_us.model_api import *


class ct_tanf_resources_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA resources eligibility"
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf
        countable_resources = spm_unit("ct_tanf_countable_resources", period)
        return countable_resources <= p.resources.limit
