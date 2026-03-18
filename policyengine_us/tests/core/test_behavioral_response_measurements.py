from types import SimpleNamespace

import numpy as np

from policyengine_us.variables.gov.simulation.behavioral_response_measurements import (
    BASELINE_BEHAVIORAL_RESPONSE_MEASUREMENT_BRANCH,
    BEHAVIORAL_RESPONSE_INPUT_VARIABLES,
    BEHAVIORAL_RESPONSE_MEASUREMENT_BRANCH,
    NEUTRALIZED_BEHAVIORAL_RESPONSE_VARIABLES,
    get_behavioral_response_measurements,
)


class FakePopulation:
    def __init__(self, net_income, mtr, capital_gains_mtr):
        self.net_income = net_income
        self.mtr = mtr
        self.capital_gains_mtr = capital_gains_mtr

    def __call__(self, variable, period):
        if variable == "marginal_tax_rate":
            return self.mtr
        if variable == "marginal_tax_rate_on_capital_gains":
            return self.capital_gains_mtr
        raise AssertionError(f"Unexpected variable lookup: {variable}")

    def household(self, variable, period):
        if variable != "household_net_income":
            raise AssertionError(f"Unexpected household lookup: {variable}")
        return self.net_income


class FakeTaxBenefitSystem:
    def __init__(self):
        self.parameters = SimpleNamespace(simulation=object())
        self.neutralized_variables = []

    def neutralize_variable(self, variable):
        self.neutralized_variables.append(variable)


class FakeBranch:
    def __init__(self, population=None, child_branches=None):
        self.tax_benefit_system = FakeTaxBenefitSystem()
        self.populations = {"person": population} if population is not None else {}
        self.branches = {}
        self.child_branches = child_branches or {}
        self.input_calls = []
        self.get_branch_calls = []

    def set_input(self, variable, period, value):
        self.input_calls.append((variable, period, value))

    def get_branch(self, name, clone_system=False):
        self.get_branch_calls.append((name, clone_system))
        if name not in self.branches:
            self.branches[name] = self.child_branches[name]
        return self.branches[name]


class FakeSimulation:
    def __init__(self, measurement_branch, baseline_branch):
        self.measurement_branch = measurement_branch
        self.baseline_branch = baseline_branch
        self.branches = {}
        self.get_branch_calls = []
        self.macro_cache_read = True
        self.macro_cache_write = True

    def get_branch(self, name, clone_system=False):
        self.get_branch_calls.append((name, clone_system))
        if name not in self.branches:
            if name == BEHAVIORAL_RESPONSE_MEASUREMENT_BRANCH:
                self.branches[name] = self.measurement_branch
            elif name == "baseline":
                self.branches[name] = self.baseline_branch
            else:
                raise AssertionError(f"Unexpected branch lookup: {name}")
        return self.branches[name]


class FakePerson:
    def __init__(self, simulation):
        self.simulation = simulation
        self.count = 2
        self.values = {
            "employment_income_before_lsr": np.array([50_000.0, 20_000.0]),
            "self_employment_income_before_lsr": np.array([0.0, 5_000.0]),
            "long_term_capital_gains_before_response": np.array(
                [10_000.0, 500.0]
            ),
        }

    def __call__(self, variable, period):
        return self.values[variable]


def test_behavioral_response_measurements_use_one_neutralized_pass():
    period = 2026
    reform_measurement = FakeBranch(
        FakePopulation(
            net_income=np.array([100.0, 200.0]),
            mtr=np.array([0.25, 0.35]),
            capital_gains_mtr=np.array([0.18, 0.22]),
        )
    )
    baseline_measurement = FakeBranch(
        FakePopulation(
            net_income=np.array([90.0, 190.0]),
            mtr=np.array([0.2, 0.3]),
            capital_gains_mtr=np.array([0.15, 0.2]),
        )
    )
    baseline_parent = FakeBranch(
        child_branches={
            BASELINE_BEHAVIORAL_RESPONSE_MEASUREMENT_BRANCH: baseline_measurement
        }
    )
    simulation = FakeSimulation(reform_measurement, baseline_parent)
    person = FakePerson(simulation)

    measurements = get_behavioral_response_measurements(person, period)

    assert np.array_equal(measurements["reform_net_income"], np.array([100.0, 200.0]))
    assert np.array_equal(
        measurements["baseline_capital_gains_mtr"], np.array([0.15, 0.2])
    )
    assert simulation.get_branch_calls == [
        (BEHAVIORAL_RESPONSE_MEASUREMENT_BRANCH, True),
        ("baseline", False),
    ]
    assert baseline_parent.get_branch_calls == [
        (BASELINE_BEHAVIORAL_RESPONSE_MEASUREMENT_BRANCH, True)
    ]
    for branch in (reform_measurement, baseline_measurement):
        assert branch.tax_benefit_system.neutralized_variables == list(
            NEUTRALIZED_BEHAVIORAL_RESPONSE_VARIABLES
        )
        assert [call[0] for call in branch.input_calls] == list(
            BEHAVIORAL_RESPONSE_INPUT_VARIABLES
        )

    assert simulation.macro_cache_read is False
    assert simulation.macro_cache_write is False
    assert BEHAVIORAL_RESPONSE_MEASUREMENT_BRANCH not in simulation.branches
    assert (
        BASELINE_BEHAVIORAL_RESPONSE_MEASUREMENT_BRANCH
        not in baseline_parent.branches
    )

    cached = get_behavioral_response_measurements(person, period)
    assert cached is measurements
    assert simulation.get_branch_calls == [
        (BEHAVIORAL_RESPONSE_MEASUREMENT_BRANCH, True),
        ("baseline", False),
    ]
