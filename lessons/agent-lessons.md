# Agent Lessons Learned

Accumulated from /encode-policy-v2 and /backdate-program runs across all contributors.
Loaded by implementation agents on future runs.

## New Lessons from Maryland CCS (2026-03-26)

### VARIABLE
- When a formula uses `select()` with a default/fallback for one category, replace it with explicit matching for ALL categories including the default; implicit defaults silently swallow new or misspelled values and make the "default" category untestable in isolation.

### REFERENCE
- When a state regulation portal migrates domains (e.g., `dsd.maryland.gov` to `regs.maryland.gov`), ALL parameter files referencing the old domain must be updated in one pass; broken redirects (301 to 404) are systematic, not isolated, so always search-and-replace across the entire state directory rather than fixing one file at a time.
- When a parameter encodes a state policy choice (e.g., state sets 85% SMI threshold), cite the state regulation as the primary reference, not the federal CFR that merely sets the ceiling; federal authority is context, not the source of the state's specific value.
- When correcting a wrong COMAR/regulation subsection citation, verify the replacement subsection's content in the same review round; three of four citation corrections in this session initially pointed to the wrong subsection because adjacent subsections cover different provisions with similar-sounding names (e.g., .03(B) = citizenship vs .03(H) = income eligibility).

### WORKFLOW
- When implementing a new state program, add it to `programs.yaml` as part of the initial implementation, not as an afterthought; missing registry entries block the program from appearing in the metadata API and coverage page.
- When a `select()` or similar lookup relies on a parameter file for each category, verify that ALL categories have corresponding parameter files before the first review round; a missing file for one category (e.g., Region W counties) forces the formula to use an implicit default, hiding a data gap.
