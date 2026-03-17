"""Test that LSR and CG behavioral responses work together.

When both labor supply responses (LSR) and capital gains (CG) behavioral
responses are enabled, the combined revenue impact should be bounded
between the individual impacts — not orders of magnitude larger.

Fixes #7785.
"""

import os

import pytest
from policyengine_core.reforms import Reform
from policyengine_us import Microsimulation

YEAR = 2026
DATE_RANGE = "2020-01-01.2100-12-31"


def _federal_tax_impact(reform_tuple):
    """Calculate federal tax revenue impact for a reform."""
    sim_baseline = Microsimulation()
    sim_reform = Microsimulation(reform=reform_tuple)
    tax_baseline = sim_baseline.calculate("income_tax", period=YEAR, map_to="household")
    tax_reform = sim_reform.calculate("income_tax", period=YEAR, map_to="household")
    return float((tax_reform - tax_baseline).sum())


def _make_tax_reform():
    """Create a simple tax reform that changes rates enough to trigger
    behavioral responses — raise the top bracket rate by 10pp."""
    return Reform.from_dict(
        {
            "gov.irs.income.bracket.rates.7": {
                DATE_RANGE: 0.47,
            },
        },
        country_id="us",
    )


def _make_lsr_reform():
    """Create CBO labor supply response reform."""
    return Reform.from_dict(
        {
            "gov.simulation.labor_supply_responses.elasticities.income": {
                DATE_RANGE: -0.05,
            },
            "gov.simulation.labor_supply_responses.elasticities.substitution.all": {
                DATE_RANGE: 0.25,
            },
        },
        country_id="us",
    )


def _make_cg_reform():
    """Create capital gains behavioral response reform."""
    return Reform.from_dict(
        {
            "gov.simulation.capital_gains_responses.elasticity": {
                DATE_RANGE: -0.62,
            },
        },
        country_id="us",
    )


@pytest.mark.skipif(
    os.environ.get("RUN_HEAVY_TESTS") != "1",
    reason="Requires ~60min for 3 microsimulations; set RUN_HEAVY_TESTS=1",
)
def test_combined_lsr_cg_impact_is_bounded():
    """Combined LSR+CG impact should not exceed sum of individual impacts.

    The combined behavioral response should produce a revenue impact
    that is bounded — roughly between the minimum and the sum of the
    individual impacts. It should definitely NOT be orders of magnitude
    larger, which would indicate a compounding/feedback bug.
    """
    tax_reform = (_make_tax_reform(),)
    lsr = _make_lsr_reform()
    cg = _make_cg_reform()

    # Individual impacts
    impact_lsr = _federal_tax_impact(tax_reform + (lsr,))
    impact_cg = _federal_tax_impact(tax_reform + (cg,))

    # Combined impact
    impact_both = _federal_tax_impact(tax_reform + (lsr, cg))

    # The combined impact should be in the same ballpark as individual
    # impacts — within 3x of their sum at most. Before the fix,
    # this was orders of magnitude larger.
    individual_sum = abs(impact_lsr) + abs(impact_cg)
    assert abs(impact_both) < 3 * individual_sum, (
        f"Combined LSR+CG impact (${impact_both / 1e9:.1f}B) is more "
        f"than 3x the sum of individual impacts "
        f"(LSR=${impact_lsr / 1e9:.1f}B + CG=${impact_cg / 1e9:.1f}B"
        f" = ${individual_sum / 1e9:.1f}B). "
        f"This suggests a compounding feedback bug between behavioral "
        f"responses. See #7785."
    )
