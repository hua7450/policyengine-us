# Agent Lessons Learned

Accumulated from /encode-policy-v2 and /backdate-program runs across all contributors.
Loaded by implementation agents on future runs.

## New Lessons from Rhode Island CCAP (2026-03-09)

### PARAMETER
- When a regulation references a composite benefit acronym (e.g., "RSDI" = Retirement + Survivors + Disability Insurance), enumerate and include ALL component income types in the sources list; do not map the acronym to only its most common component.
- **Rules as code**: Parameter values MUST match the legal text exactly. If the law says "up through eighteen (18)", the parameter value is 18 — never adjust it to 19 to compensate for a wrong comparison operator. Fix the formula operator (`<=` vs `<`) instead. Parameters store what the law says; formulas encode the logic.

### TEST
- When tests were written to match a buggy parameter or formula, fixing the root cause requires a sweep of ALL test files that reference the affected variable; stale expected outputs silently mask regressions.

### FORMULA
- When a review finding identifies a boundary operator mismatch (strict `<` vs inclusive `<=`) against regulation text, resolve it before approving; boundary bugs affect exactly one threshold-value row and are invisible in typical test cases that avoid exact boundaries.
