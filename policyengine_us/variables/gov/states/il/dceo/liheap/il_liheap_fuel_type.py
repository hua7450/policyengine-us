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
        has_fuel_oil = add(spm_unit, period, ["fuel_oil_expense", "coal_expense"]) > 0
        has_gas = (
            add(
                spm_unit,
                period,
                ["gas_expense", "bottled_gas_expense", "metered_gas_expense"],
            )
            > 0
        )
        return select(
            [heat_in_rent, has_fuel_oil, has_gas],
            [
                ILLIHEAPFuelType.CASH,
                ILLIHEAPFuelType.PROPANE_FUEL_OIL,
                ILLIHEAPFuelType.NAT_GAS_OTHER,
            ],
            default=ILLIHEAPFuelType.ALL_ELECTRIC,
        )
