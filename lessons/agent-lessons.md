# Agent Lessons Learned

Accumulated from /encode-policy-v2 and /backdate-program runs across all contributors.
Loaded by implementation agents on future runs.


## New Lessons from Rhode Island CCAP (2026-03-05)

### TEST
- When a variable's output depends on a multi-valued dimension (e.g., provider type, care setting, filing status), ensure every dimension value has at least one test case; zero coverage of an entire dimension is a critical gap that hides bugs.

### PARAMETER
- After implementation, verify every parameter file is referenced by at least one formula; orphaned parameters indicate missing logic or over-specification and should be either wired into a formula or removed.

### REFERENCE
- When bulk-generating parameter files from a single regulatory document, page reference errors tend to be systematic (e.g., a consistent offset); verify every file's page anchor individually rather than spot-checking a few -- a single wrong base page propagates to all derived files.
