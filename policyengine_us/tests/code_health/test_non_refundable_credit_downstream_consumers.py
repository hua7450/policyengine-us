import re

from policyengine_us.model_api import REPO


STATE_VARIABLES_ROOT = REPO / "variables" / "gov" / "states"


REVIEWED_APPLIED_CREDIT_EXTERNAL_REFERENCES = {
    "de_non_refundable_eitc": {
        "variables/gov/states/de/tax/income/credits/eitc/de_eitc.py",
        "variables/gov/states/de/tax/income/credits/eitc/refundability_calculation/de_income_tax_if_claiming_non_refundable_eitc.py",
    },
    "ky_personal_tax_credits": {
        "variables/gov/states/ky/tax/income/credits/family_size_credit/ky_family_size_tax_credit_potential.py",
    },
    "la_non_refundable_cdcc": {
        "variables/gov/states/la/tax/income/credits/school_readiness/la_school_readiness_tax_credit.py",
    },
    "md_non_refundable_eitc": {
        "variables/gov/states/md/tax/income/credits/eitc/md_eitc.py",
    },
    "ny_household_credit": {
        "variables/gov/states/ny/tax/income/credits/ny_eitc.py",
    },
    "va_non_refundable_eitc": {
        "variables/gov/states/va/tax/income/credits/eitc/refundability_calculation/va_income_tax_if_claiming_non_refundable_eitc.py",
        "variables/gov/states/va/tax/income/credits/eitc/va_eitc.py",
        "variables/gov/states/va/tax/income/credits/eitc/va_eitc_person.py",
    },
}


def applied_credit_variable_definitions() -> dict[str, str]:
    definitions = {}

    assert STATE_VARIABLES_ROOT.exists(), (
        f"Expected state variables root to exist: {STATE_VARIABLES_ROOT}"
    )

    for file_name in STATE_VARIABLES_ROOT.glob("**/*.py"):
        source = file_name.read_text()
        if "applied_state_non_refundable_credit(" not in source:
            continue

        class_match = re.search(r"class\s+([a-z0-9_]+)\(Variable\):", source)
        if class_match is None:
            continue
        definitions[class_match.group(1)] = file_name.relative_to(REPO).as_posix()

    assert definitions, "Expected to discover at least one applied credit variable"
    return definitions


def string_literal_references(variable_name: str) -> set[str]:
    pattern = re.compile(rf"[\"']{re.escape(variable_name)}[\"']")
    references = set()

    for file_name in STATE_VARIABLES_ROOT.glob("**/*.py"):
        if pattern.search(file_name.read_text()):
            references.add(file_name.relative_to(REPO).as_posix())

    return references


def test_applied_credit_downstream_consumers_are_reviewed():
    mismatches = []

    for variable_name, defining_file in sorted(
        applied_credit_variable_definitions().items()
    ):
        actual_external_references = string_literal_references(variable_name) - {
            defining_file
        }
        expected_external_references = REVIEWED_APPLIED_CREDIT_EXTERNAL_REFERENCES.get(
            variable_name, set()
        )

        if actual_external_references != expected_external_references:
            mismatches.append(
                "\n".join(
                    [
                        f"{variable_name}:",
                        f"  expected: {sorted(expected_external_references)}",
                        f"  actual:   {sorted(actual_external_references)}",
                    ]
                )
            )

    assert not mismatches, (
        "Applied state nonrefundable credit variables gained new downstream "
        "consumers or no longer match the reviewed set. If a form or statute "
        "needs the pre-ordering amount, add a *_potential variable consumer "
        "instead of reading the applied credit. Details:\n\n" + "\n\n".join(mismatches)
    )
