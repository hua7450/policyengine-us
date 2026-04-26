# Agent Lessons Learned

Accumulated from /encode-policy-v2 and /backdate-program runs across all contributors.
Loaded by implementation agents on future runs.

## New Lessons from Washington SSP (2026-04-25)

### REFERENCE
- When a rate or category change has both an emergency WSR (or equivalent emergency rule filing) and a later permanent codification, use the EMERGENCY rule's effective date as the operative date for the parameter — the permanent filing is just codification of what was already in force. Cite both, labeling each as "(emergency, eff. YYYY-MM-DD)" and "(permanent, eff. YYYY-MM-DD)".
- Verify subsection citations against the actual rule's numbering structure (top-level numbered (1), (2), ... and lettered sub-paragraphs (2)(a), (2)(b), ...) before quoting them; citing a subsection number that does not exist at all (e.g., (5) when the rule has only (1) and (2)) is a different error class than citing the wrong subsection content, and both must be checked.
- When researching a rule change, check whether the emergency rule amended MULTIPLE related WAC/CFR sections in one filing (e.g., both a rates rule and an eligibility-categories rule); do not assume an emergency rule touched only the section that introduced the rate change — pull the full filing text and inventory every section it amended.

### WORKFLOW
- When backdating a parameter's effective date based on a newly-discovered emergency rule, also check whether the SAME amending rule changed any related eligibility toggles, category-definition parameters, or in_effect flags — and apply the same backdate to every artifact that rule introduced. A single fix to one parameter while leaving sibling parameters keyed to the wrong (later) date creates internal inconsistency between rate and eligibility.
- When fixing a regulatory citation (subsection number, WSR ID, effective date) in a parameter file, also update any matching inline comments in variable .py files and any test case names that reference the old citation; correctness of outputs is not enough — readability and cross-reference alignment must also be preserved in the same fix round.
