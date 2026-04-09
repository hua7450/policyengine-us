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
