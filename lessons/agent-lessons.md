# Agent Lessons Learned

Accumulated from /encode-policy-v2 and /backdate-program runs across all contributors.
Loaded by implementation agents on future runs.


## New Lessons from Vermont CCFAP (2026-03-12)

### REFERENCE
- When a parameter cites a source document, verify the document identity (not just page/section) is correct; referencing a related but wrong document (e.g., a rate sheet instead of the regulations PDF) passes casual review because the values may appear in both places.
- Section citations must use the most specific subsection available (e.g., "Section I B 6" not "Section I B"); generic parent-section citations make it impossible to verify which provision justifies the parameter value.

### TEST
- Test case names/descriptions must match their expected output values; a name that says "$275 weekly" when the test expects $250 misleads reviewers and masks whether the test is actually correct.
