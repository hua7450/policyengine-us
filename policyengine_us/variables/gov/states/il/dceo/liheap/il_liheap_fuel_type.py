from policyengine_us.model_api import *


class ILLIHEAPFuelType(Enum):
    ALL_ELECTRIC = "All Electric"
    NAT_GAS_OTHER = "Natural Gas / Other"
    PROPANE_FUEL_OIL = "Propane / Fuel Oil"
    CASH = "Cash (heat included in rent)"


class il_liheap_fuel_type(Variable):
    value_type = Enum
    entity = SPMUnit
    possible_values = ILLIHEAPFuelType
    default_value = ILLIHEAPFuelType.ALL_ELECTRIC
    definition_period = YEAR
    label = "Household fuel type for IL LIHEAP"
    defined_for = StateCode.IL

    def formula(spm_unit, period, parameters):
        heat_in_rent = spm_unit("heat_expense_included_in_rent", period)
        return where(
            heat_in_rent,
            ILLIHEAPFuelType.CASH,
            ILLIHEAPFuelType.ALL_ELECTRIC,
        )
