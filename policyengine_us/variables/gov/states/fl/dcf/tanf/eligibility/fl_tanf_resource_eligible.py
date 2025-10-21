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

        # Check countable assets against resource limit
        # Note: spm_unit_assets includes all household assets
        total_assets = spm_unit("spm_unit_assets", period)

        # For vehicle assets, we use the standard vehicle_value variable
        # Florida allows one vehicle exclusion up to $8,500 equity
        vehicle_value = spm_unit("vehicle_owned_value", period)

        # Calculate countable assets (total assets minus exempt vehicle value)
        # Exempt the first vehicle up to the vehicle limit
        exempt_vehicle = min_(vehicle_value, p.vehicle_limit)
        countable_assets = max_(total_assets - exempt_vehicle, 0)

        # Family is resource eligible if countable assets <= resource limit
        return countable_assets <= p.resource_limit
