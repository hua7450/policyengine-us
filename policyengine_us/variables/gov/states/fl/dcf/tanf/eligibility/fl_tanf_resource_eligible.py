from policyengine_us.model_api import *


class fl_tanf_resource_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Resource eligible for Florida Temporary Cash Assistance"
    definition_period = MONTH
    reference = "Florida Statute § 414.075"
    documentation = "https://www.flsenate.gov/Laws/Statutes/2024/414.075"
    defined_for = StateCode.FL

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.fl.dcf.tanf

        # For now, assume resource eligibility based on available data
        # In a complete implementation, this would check countable assets
        # and vehicle equity values against limits

        # Placeholder: assume eligible unless we have asset data
        # A full implementation would check:
        # - Total countable assets <= $2,000 (p.resource_limit)
        # - Vehicle equity <= $8,500 (p.vehicle_limit)

        return True
