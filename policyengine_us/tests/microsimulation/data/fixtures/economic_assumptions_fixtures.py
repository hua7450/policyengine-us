"""
Fixtures for extend_single_year_dataset and uprating tests.

Provides mock system objects, parameter trees, and sample datasets
so tests can run without loading the full policyengine-us tax-benefit
system.
"""

import numpy as np
import pandas as pd

from policyengine_us.data.dataset_schema import USSingleYearDataset

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BASE_YEAR = 2024
END_YEAR_DEFAULT = 2035
END_YEAR_SHORT = 2026

NUM_PERSONS = 10
NUM_HOUSEHOLDS = 4
NUM_TAX_UNITS = 5

# Uprating parameter paths (mirrors real policyengine-us paths)
EMPLOYMENT_INCOME_UPRATING = "calibration.gov.irs.soi.employment_income"
CPI_U_UPRATING = "gov.bls.cpi.cpi_u"
INVALID_UPRATING_PATH = "does.not.exist"

# Uprating parameter values — simple round numbers for easy verification.
# The growth factor from 2024 to 2025 is 110/100 = 1.10 (10% growth).
# The growth factor from 2025 to 2026 is 121/110 = 1.10 (10% growth).
EMPLOYMENT_INCOME_PARAM_VALUES = {
    "2024-01-01": 100.0,
    "2025-01-01": 110.0,
    "2026-01-01": 121.0,
    "2027-01-01": 133.1,
}
EMPLOYMENT_INCOME_GROWTH_FACTOR_2024_TO_2025 = 110.0 / 100.0  # 1.10
EMPLOYMENT_INCOME_GROWTH_FACTOR_2025_TO_2026 = 121.0 / 110.0  # 1.10

CPI_U_PARAM_VALUES = {
    "2024-01-01": 300.0,
    "2025-01-01": 309.0,
    "2026-01-01": 318.27,
}
CPI_U_GROWTH_FACTOR_2024_TO_2025 = 309.0 / 300.0  # 1.03

# Base-year column values
PERSON_IDS = np.arange(1, NUM_PERSONS + 1)
EMPLOYMENT_INCOME_BASE = np.array(
    [
        50_000,
        60_000,
        70_000,
        80_000,
        90_000,
        40_000,
        30_000,
        0,
        100_000,
        55_000,
    ],
    dtype=float,
)
AGE_BASE = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70], dtype=float)

HOUSEHOLD_IDS = np.arange(1, NUM_HOUSEHOLDS + 1)
RENT_BASE = np.array([1_200, 1_500, 900, 2_000], dtype=float)

TAX_UNIT_IDS = np.arange(1, NUM_TAX_UNITS + 1)


# ---------------------------------------------------------------------------
# Mock parameter tree
# ---------------------------------------------------------------------------


class MockParameter:
    """A callable that returns a value for a given period string."""

    def __init__(self, values: dict[str, float]):
        self._values = values

    def __call__(self, period: str) -> float:
        return self._values[period]


class _ParameterNode:
    """A nested attribute-access node for building mock parameter trees."""

    def __init__(self):
        self._children = {}

    def _add_path(self, path: str, param: MockParameter):
        parts = path.split(".", 1)
        if len(parts) == 1:
            self._children[parts[0]] = param
        else:
            child = self._children.setdefault(parts[0], _ParameterNode())
            child._add_path(parts[1], param)

    def __getattr__(self, name):
        if name.startswith("_"):
            return super().__getattribute__(name)
        try:
            return self._children[name]
        except KeyError:
            raise AttributeError(name)


def build_mock_parameters(param_specs: dict[str, dict[str, float]]):
    """Build a mock parameter tree from {dotted_path: {period: value}}."""
    root = _ParameterNode()
    for path, values in param_specs.items():
        root._add_path(path, MockParameter(values))
    return root


# ---------------------------------------------------------------------------
# Mock variable metadata
# ---------------------------------------------------------------------------


class MockVariable:
    """Minimal stand-in for a policyengine Variable metadata object."""

    def __init__(self, name: str, uprating: str | None = None):
        self.name = name
        self.uprating = uprating


# Variables with uprating
MOCK_EMPLOYMENT_INCOME_VAR = MockVariable(
    "employment_income", uprating=EMPLOYMENT_INCOME_UPRATING
)
MOCK_RENT_VAR = MockVariable("rent", uprating=CPI_U_UPRATING)

# Variables without uprating (carried forward unchanged)
MOCK_AGE_VAR = MockVariable("age", uprating=None)
MOCK_PERSON_ID_VAR = MockVariable("person_id", uprating=None)

# Variable with an invalid uprating path
MOCK_BAD_UPRATING_VAR = MockVariable("bad_variable", uprating=INVALID_UPRATING_PATH)


def build_mock_variables() -> dict:
    """Return a dict mapping variable name -> MockVariable."""
    return {
        v.name: v
        for v in [
            MOCK_EMPLOYMENT_INCOME_VAR,
            MOCK_RENT_VAR,
            MOCK_AGE_VAR,
            MOCK_PERSON_ID_VAR,
        ]
    }


# ---------------------------------------------------------------------------
# Mock system
# ---------------------------------------------------------------------------


class MockSystem:
    """Minimal stand-in for policyengine_us.system.system."""

    def __init__(self, variables=None, parameters=None):
        self.variables = variables or build_mock_variables()
        self.parameters = parameters or build_mock_parameters(
            {
                EMPLOYMENT_INCOME_UPRATING: EMPLOYMENT_INCOME_PARAM_VALUES,
                CPI_U_UPRATING: CPI_U_PARAM_VALUES,
            }
        )


def build_mock_system() -> MockSystem:
    return MockSystem()


# ---------------------------------------------------------------------------
# Sample datasets
# ---------------------------------------------------------------------------


def build_base_person_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "person_id": PERSON_IDS,
            "employment_income": EMPLOYMENT_INCOME_BASE.copy(),
            "age": AGE_BASE.copy(),
        }
    )


def build_base_household_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "household_id": HOUSEHOLD_IDS,
            "rent": RENT_BASE.copy(),
        }
    )


def build_base_tax_unit_df() -> pd.DataFrame:
    return pd.DataFrame({"tax_unit_id": TAX_UNIT_IDS})


def build_single_year_dataset(
    time_period: int = BASE_YEAR,
) -> USSingleYearDataset:
    """Create a minimal USSingleYearDataset for testing."""
    return USSingleYearDataset(
        person=build_base_person_df(),
        household=build_base_household_df(),
        tax_unit=build_base_tax_unit_df(),
        spm_unit=pd.DataFrame({"spm_unit_id": [1, 2, 3]}),
        family=pd.DataFrame({"family_id": [1, 2]}),
        marital_unit=pd.DataFrame({"marital_unit_id": [1, 2, 3, 4]}),
        time_period=time_period,
    )
