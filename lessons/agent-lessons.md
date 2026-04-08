# Agent Lessons Learned

Accumulated from /encode-policy-v2 and /backdate-program runs across all contributors.
Loaded by implementation agents on future runs.

## New Lessons from West Virginia CCAP (2026-04-08)

### PARAMETER
- When transcribing a multi-dimension lookup table (e.g., age group x quality tier x provider type), verify that row labels (age groups) are correctly aligned with their data columns; if one dimension's boundaries shift (e.g., age groups redefined), ALL rate values in that dimension must be re-read from the source — a wrong row-label mapping cascades to every value in the affected rows, not just one.
- Never invent a parameter value when no source supports it; if the regulatory document does not specify a threshold (e.g., an initial FPL limit distinct from the ongoing limit), do not fabricate one — either use the documented value for both paths or flag the gap as unverifiable. A fabricated value that looks plausible (e.g., 150% vs 185%) passes casual review and is harder to catch than a missing value.
- When a parameter represents a soft administrative guideline rather than a hard regulatory cutoff (e.g., "adults are defined as 18+" used as a general definition, not a strict eligibility bar), document this distinction in the parameter description; do not model it as a strict eligibility gate unless the regulation explicitly mandates denial for failing the criterion.
