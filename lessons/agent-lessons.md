# Agent Lessons Learned

Accumulated from /encode-policy-v2 and /backdate-program runs across all contributors.
Loaded by implementation agents on future runs.


## New Lessons from New Hampshire CCAP (2026-03-12)

### REFERENCE
- State legislature filing-history or rule-history URLs are fragile (redirect chains that end in 404); always verify that reference URLs resolve before citing them, and prefer permanent/canonical URLs (e.g., section-specific regulation portals) over dynamic filing-history pages.

### TEST
- Integration tests must include at least one case with a positive (non-zero) final benefit amount to verify the full calculation pipeline produces a correct payable result; zero-benefit-only integration tests hide formula errors that cancel out.
- When a benefit has add-on components (supplements, adjustments, bonuses), test that each add-on flows through to the top-level benefit variable — not just that the add-on variable calculates correctly in isolation.
