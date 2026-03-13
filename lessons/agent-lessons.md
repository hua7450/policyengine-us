# Agent Lessons Learned

Accumulated from /encode-policy-v2 and /backdate-program runs across all contributors.
Loaded by implementation agents on future runs.

## New Lessons from Connecticut C4K (2026-03-13)

### REFERENCE
- Prefer direct document URLs (e.g., PDFs with `#page=` anchors) over landing-page or index-page URLs; agency websites frequently reorganize navigation pages while direct document links remain stable — 23 parameter files had to be fixed in a single session because all referenced the same reorganized landing page.
- When a regulation cites a specific conversion factor or constant (e.g., "multiply by 4.3"), use that exact value in the formula even if a standard library constant (e.g., WEEKS_IN_YEAR / 12 = 4.333) is close; regulatory precision takes precedence over mathematical convenience, and the discrepancy may affect benefit amounts at boundary conditions.
- When citing the legal authority for a parameter, distinguish between the statute (e.g., CGS section) that establishes the rule and the regulation (e.g., RCSA section) that implements it; citing the wrong legal instrument (regulation instead of statute or vice versa) is a correctness error even if both documents mention the same topic.

### PARAMETER
- When a transmittal or policy document has a numbered identifier (e.g., POL-24-01 vs POL-24-02), verify the identifier matches the specific document that contains the cited data; adjacent transmittals from the same agency often cover different provisions and have similar-looking identifiers.
