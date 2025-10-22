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

        # Check countable resources against limit
        # Use cash assets as proxy for countable resources
        cash_assets = spm_unit("spm_unit_cash_assets", period.this_year)

        # Vehicle value with exclusion
        vehicle_value = spm_unit.household(
            "household_vehicles_value", period.this_year
        )

        # Exclude up to vehicle limit, count excess
        excess_vehicle_value = max_(vehicle_value - p.vehicle_limit, 0)

        # Total countable resources
        total_resources = cash_assets + excess_vehicle_value

        return total_resources <= p.resource_limit
