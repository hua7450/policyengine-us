# Agent Lessons Learned

Accumulated from /encode-policy-v2 and /backdate-program runs across all contributors.
Loaded by implementation agents on future runs.

## New Lessons from Georgia CAPS (2026-04-09)

### FORMULA
- When a program defines countable income at the family/unit level using an `adds` list, verify which household members' income the regulation includes; do not assume all members contribute -- regulations often exclude income from minors (e.g., children 17 or younger), requiring a formula that filters by age before summing.
- When a quality bonus or supplement is defined as a percentage of "base payment," verify whether the regulation means the gross rate or the net amount after subtracting copays/fees; applying a percentage to the wrong base (gross vs net-of-fee) systematically over- or understates the subsidy for every recipient.

### WORKFLOW
- When a requirements document includes priority/triage categorization flags (e.g., "very low income priority") that do not gate eligibility or change benefit amounts, explicitly mark them as deferrable in the coverage report rather than treating them as missing implementation; priority flags affect waitlist ordering, not the benefit calculation pipeline.
