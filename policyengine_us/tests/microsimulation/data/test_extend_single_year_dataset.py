"""
Tests for extend_single_year_dataset and its internal helpers.

Uses mock system objects to avoid loading the full policyengine-us
tax-benefit system, keeping tests fast and deterministic.
"""

import sys as _sys
from types import ModuleType
from unittest.mock import patch

import numpy as np
import pandas as pd
import pytest

from policyengine_us.data.dataset_schema import (
    USSingleYearDataset,
    USMultiYearDataset,
)
from policyengine_us.data.economic_assumptions import (
    _apply_single_year_uprating,
    _resolve_parameter,
)
from policyengine_us.tests.microsimulation.data.fixtures.economic_assumptions_fixtures import (
    BASE_YEAR,
    END_YEAR_SHORT,
    END_YEAR_DEFAULT,
    NUM_PERSONS,
    NUM_HOUSEHOLDS,
    EMPLOYMENT_INCOME_BASE,
    EMPLOYMENT_INCOME_GROWTH_FACTOR_2024_TO_2025,
    EMPLOYMENT_INCOME_GROWTH_FACTOR_2025_TO_2026,
    CPI_U_GROWTH_FACTOR_2024_TO_2025,
    AGE_BASE,
    RENT_BASE,
    EMPLOYMENT_INCOME_UPRATING,
    EMPLOYMENT_INCOME_PARAM_VALUES,
    CPI_U_UPRATING,
    CPI_U_PARAM_VALUES,
    INVALID_UPRATING_PATH,
    build_mock_system,
    build_mock_parameters,
    build_single_year_dataset,
    MockVariable,
    MockSystem,
)


def _call_extend_with_mock_system(mock_system, dataset, **kwargs):
    """Call extend_single_year_dataset with a mock system module.

    The real ``_apply_uprating`` does ``from policyengine_us.system import
    system`` at call time.  We intercept that import by temporarily
    injecting a fake ``policyengine_us.system`` module into ``sys.modules``
    so the real (expensive) tax-benefit system is never loaded.
    """
    fake_module = ModuleType("policyengine_us.system")
    fake_module.system = mock_system

    saved = _sys.modules.get("policyengine_us.system")
    _sys.modules["policyengine_us.system"] = fake_module
    try:
        # Import here so the patched module is used
        from policyengine_us.data.economic_assumptions import (
            extend_single_year_dataset,
        )

        return extend_single_year_dataset(dataset, **kwargs)
    finally:
        if saved is not None:
            _sys.modules["policyengine_us.system"] = saved
        else:
            _sys.modules.pop("policyengine_us.system", None)


@pytest.fixture
def mock_system():
    return build_mock_system()


@pytest.fixture
def base_dataset():
    return build_single_year_dataset()


# ---------------------------------------------------------------------------
# _resolve_parameter
# ---------------------------------------------------------------------------


class TestResolveParameter:
    def test_given_valid_dotted_path_then_returns_parameter(self):
        # Given
        params = build_mock_parameters(
            {EMPLOYMENT_INCOME_UPRATING: EMPLOYMENT_INCOME_PARAM_VALUES}
        )

        # When
        result = _resolve_parameter(params, EMPLOYMENT_INCOME_UPRATING)

        # Then
        assert result is not None
        assert result("2024-01-01") == 100.0

    def test_given_invalid_path_then_returns_none(self):
        # Given
        params = build_mock_parameters(
            {EMPLOYMENT_INCOME_UPRATING: EMPLOYMENT_INCOME_PARAM_VALUES}
        )

        # When
        result = _resolve_parameter(params, INVALID_UPRATING_PATH)

        # Then
        assert result is None

    def test_given_partial_valid_path_then_returns_none(self):
        # Given
        params = build_mock_parameters(
            {EMPLOYMENT_INCOME_UPRATING: EMPLOYMENT_INCOME_PARAM_VALUES}
        )

        # When — path exists partially but not fully
        result = _resolve_parameter(params, "calibration.gov.nonexistent")

        # Then
        assert result is None


# ---------------------------------------------------------------------------
# _apply_single_year_uprating
# ---------------------------------------------------------------------------


class TestApplySingleYearUprating:
    def test_given_uprated_variable_then_values_scaled_by_growth_factor(
        self, base_dataset, mock_system
    ):
        # Given
        current = base_dataset.copy()
        current.time_period = str(BASE_YEAR + 1)
        previous = base_dataset

        # When
        _apply_single_year_uprating(current, previous, mock_system)

        # Then
        expected = EMPLOYMENT_INCOME_BASE * EMPLOYMENT_INCOME_GROWTH_FACTOR_2024_TO_2025
        np.testing.assert_allclose(current.person["employment_income"].values, expected)

    def test_given_variable_without_uprating_then_values_unchanged(
        self, base_dataset, mock_system
    ):
        # Given
        current = base_dataset.copy()
        current.time_period = str(BASE_YEAR + 1)
        previous = base_dataset

        # When
        _apply_single_year_uprating(current, previous, mock_system)

        # Then — age has no uprating, should be unchanged
        np.testing.assert_array_equal(current.person["age"].values, AGE_BASE)

    def test_given_household_variable_with_uprating_then_values_scaled(
        self, base_dataset, mock_system
    ):
        # Given
        current = base_dataset.copy()
        current.time_period = str(BASE_YEAR + 1)
        previous = base_dataset

        # When
        _apply_single_year_uprating(current, previous, mock_system)

        # Then — rent is uprated by CPI-U
        expected = RENT_BASE * CPI_U_GROWTH_FACTOR_2024_TO_2025
        np.testing.assert_allclose(current.household["rent"].values, expected)

    def test_given_variable_not_in_system_then_values_unchanged(self, mock_system):
        # Given — add a column the system doesn't know about
        person_df = pd.DataFrame(
            {
                "person_id": [1, 2],
                "employment_income": [50_000.0, 60_000.0],
                "mystery_column": [999.0, 888.0],
            }
        )
        current = USSingleYearDataset(
            person=person_df.copy(),
            household=pd.DataFrame({"household_id": [1]}),
            tax_unit=pd.DataFrame({"tax_unit_id": [1]}),
            time_period=BASE_YEAR + 1,
        )
        previous = USSingleYearDataset(
            person=person_df.copy(),
            household=pd.DataFrame({"household_id": [1]}),
            tax_unit=pd.DataFrame({"tax_unit_id": [1]}),
            time_period=BASE_YEAR,
        )

        # When
        _apply_single_year_uprating(current, previous, mock_system)

        # Then — mystery_column should be untouched
        np.testing.assert_array_equal(
            current.person["mystery_column"].values,
            [999.0, 888.0],
        )

    def test_given_uprating_path_unresolvable_then_values_unchanged(self):
        # Given — variable has an uprating path that doesn't exist in params
        variables = {
            "bad_variable": MockVariable("bad_variable", uprating=INVALID_UPRATING_PATH)
        }
        system = MockSystem(
            variables=variables,
            parameters=build_mock_parameters({}),
        )

        person_df = pd.DataFrame(
            {
                "person_id": [1],
                "bad_variable": [42.0],
            }
        )
        current = USSingleYearDataset(
            person=person_df.copy(),
            household=pd.DataFrame({"household_id": [1]}),
            tax_unit=pd.DataFrame({"tax_unit_id": [1]}),
            time_period=BASE_YEAR + 1,
        )
        previous = USSingleYearDataset(
            person=person_df.copy(),
            household=pd.DataFrame({"household_id": [1]}),
            tax_unit=pd.DataFrame({"tax_unit_id": [1]}),
            time_period=BASE_YEAR,
        )

        # When
        _apply_single_year_uprating(current, previous, system)

        # Then
        assert current.person["bad_variable"].values[0] == 42.0

    def test_given_previous_param_value_zero_then_values_unchanged(self):
        # Given — parameter value is 0 for the previous year (avoid div-by-zero)
        variables = {"some_income": MockVariable("some_income", uprating="test.param")}
        system = MockSystem(
            variables=variables,
            parameters=build_mock_parameters(
                {"test.param": {"2024-01-01": 0.0, "2025-01-01": 100.0}}
            ),
        )

        person_df = pd.DataFrame(
            {
                "person_id": [1],
                "some_income": [5_000.0],
            }
        )
        current = USSingleYearDataset(
            person=person_df.copy(),
            household=pd.DataFrame({"household_id": [1]}),
            tax_unit=pd.DataFrame({"tax_unit_id": [1]}),
            time_period=BASE_YEAR + 1,
        )
        previous = USSingleYearDataset(
            person=person_df.copy(),
            household=pd.DataFrame({"household_id": [1]}),
            tax_unit=pd.DataFrame({"tax_unit_id": [1]}),
            time_period=BASE_YEAR,
        )

        # When
        _apply_single_year_uprating(current, previous, system)

        # Then — no division by zero, value unchanged
        assert current.person["some_income"].values[0] == 5_000.0

    def test_given_zero_base_values_then_uprating_preserves_zeros(
        self, base_dataset, mock_system
    ):
        # Given — person index 7 has employment_income = 0
        current = base_dataset.copy()
        current.time_period = str(BASE_YEAR + 1)
        previous = base_dataset

        # When
        _apply_single_year_uprating(current, previous, mock_system)

        # Then — 0 * any_factor = 0
        assert current.person["employment_income"].values[7] == 0.0


# ---------------------------------------------------------------------------
# extend_single_year_dataset (end-to-end with mocked system)
# ---------------------------------------------------------------------------


class TestExtendSingleYearDataset:
    def test_given_base_year_and_end_year_then_correct_number_of_years(
        self, base_dataset, mock_system
    ):
        # When
        result = _call_extend_with_mock_system(
            mock_system, base_dataset, end_year=END_YEAR_SHORT
        )

        # Then
        expected_years = list(range(BASE_YEAR, END_YEAR_SHORT + 1))
        assert result.years == expected_years

    def test_given_base_year_equals_end_year_then_single_year_returned(
        self, base_dataset, mock_system
    ):
        # When
        result = _call_extend_with_mock_system(
            mock_system, base_dataset, end_year=BASE_YEAR
        )

        # Then
        assert result.years == [BASE_YEAR]

    def test_given_default_end_year_then_extends_to_2035(self):
        # Given — need param values through 2035
        extended_values = {
            f"{y}-01-01": 100.0 * (1.1 ** (y - BASE_YEAR))
            for y in range(BASE_YEAR, END_YEAR_DEFAULT + 1)
        }
        cpi_values = {
            f"{y}-01-01": 300.0 * (1.03 ** (y - BASE_YEAR))
            for y in range(BASE_YEAR, END_YEAR_DEFAULT + 1)
        }
        system = MockSystem(
            parameters=build_mock_parameters(
                {
                    EMPLOYMENT_INCOME_UPRATING: extended_values,
                    CPI_U_UPRATING: cpi_values,
                }
            )
        )
        dataset = build_single_year_dataset()

        # When
        result = _call_extend_with_mock_system(system, dataset)

        # Then
        assert result.years == list(range(BASE_YEAR, END_YEAR_DEFAULT + 1))

    def test_given_extended_dataset_then_base_year_values_unchanged(
        self, base_dataset, mock_system
    ):
        # When
        result = _call_extend_with_mock_system(
            mock_system, base_dataset, end_year=END_YEAR_SHORT
        )

        # Then — base year data should match original
        base = result[BASE_YEAR]
        np.testing.assert_array_equal(
            base.person["employment_income"].values,
            EMPLOYMENT_INCOME_BASE,
        )
        np.testing.assert_array_equal(base.person["age"].values, AGE_BASE)
        np.testing.assert_array_equal(base.household["rent"].values, RENT_BASE)

    def test_given_extended_dataset_then_year_one_correctly_uprated(
        self, base_dataset, mock_system
    ):
        # When
        result = _call_extend_with_mock_system(
            mock_system, base_dataset, end_year=END_YEAR_SHORT
        )

        # Then
        year_one = result[BASE_YEAR + 1]
        expected = EMPLOYMENT_INCOME_BASE * EMPLOYMENT_INCOME_GROWTH_FACTOR_2024_TO_2025
        np.testing.assert_allclose(
            year_one.person["employment_income"].values, expected
        )

    def test_given_extended_dataset_then_year_two_chains_uprating(
        self, base_dataset, mock_system
    ):
        # When
        result = _call_extend_with_mock_system(
            mock_system, base_dataset, end_year=END_YEAR_SHORT
        )

        # Then — year 2 should be uprated from year 1, not from base
        expected = (
            EMPLOYMENT_INCOME_BASE
            * EMPLOYMENT_INCOME_GROWTH_FACTOR_2024_TO_2025
            * EMPLOYMENT_INCOME_GROWTH_FACTOR_2025_TO_2026
        )
        year_two = result[BASE_YEAR + 2]
        np.testing.assert_allclose(
            year_two.person["employment_income"].values, expected
        )

    def test_given_extended_dataset_then_non_uprated_variable_same_all_years(
        self, base_dataset, mock_system
    ):
        # When
        result = _call_extend_with_mock_system(
            mock_system, base_dataset, end_year=END_YEAR_SHORT
        )

        # Then — age has no uprating, identical across all years
        for year in result.years:
            np.testing.assert_array_equal(result[year].person["age"].values, AGE_BASE)

    def test_given_extended_dataset_then_row_counts_preserved(
        self, base_dataset, mock_system
    ):
        # When
        result = _call_extend_with_mock_system(
            mock_system, base_dataset, end_year=END_YEAR_SHORT
        )

        # Then — every year has the same number of rows per entity
        for year in result.years:
            ds = result[year]
            assert len(ds.person) == NUM_PERSONS
            assert len(ds.household) == NUM_HOUSEHOLDS

    def test_given_extended_dataset_then_each_year_has_correct_time_period(
        self, base_dataset, mock_system
    ):
        # When
        result = _call_extend_with_mock_system(
            mock_system, base_dataset, end_year=END_YEAR_SHORT
        )

        # Then
        for year in result.years:
            assert int(result[year].time_period) == year

    def test_given_extended_dataset_then_result_is_multi_year_dataset(
        self, base_dataset, mock_system
    ):
        # When
        result = _call_extend_with_mock_system(
            mock_system, base_dataset, end_year=END_YEAR_SHORT
        )

        # Then
        assert isinstance(result, USMultiYearDataset)
        assert result.data_format == "time_period_arrays"

    def test_given_extended_dataset_then_input_dataset_not_mutated(self, mock_system):
        # Given
        dataset = build_single_year_dataset()
        original_values = dataset.person["employment_income"].values.copy()

        # When
        _call_extend_with_mock_system(mock_system, dataset, end_year=END_YEAR_SHORT)

        # Then — original dataset should be untouched
        np.testing.assert_array_equal(
            dataset.person["employment_income"].values,
            original_values,
        )

    def test_given_multiple_entities_uprated_then_all_apply_correctly(
        self, base_dataset, mock_system
    ):
        # When
        result = _call_extend_with_mock_system(
            mock_system, base_dataset, end_year=END_YEAR_SHORT
        )

        # Then — both person (employment_income) and household (rent) uprated
        year_one = result[BASE_YEAR + 1]
        np.testing.assert_allclose(
            year_one.person["employment_income"].values,
            EMPLOYMENT_INCOME_BASE * EMPLOYMENT_INCOME_GROWTH_FACTOR_2024_TO_2025,
        )
        np.testing.assert_allclose(
            year_one.household["rent"].values,
            RENT_BASE * CPI_U_GROWTH_FACTOR_2024_TO_2025,
        )
