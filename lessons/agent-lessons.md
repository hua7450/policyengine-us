# Agent Lessons Learned

Accumulated from /encode-policy-v2 and /backdate-program runs across all contributors.
Loaded by implementation agents on future runs.

## New Lessons from Indiana SSP (2026-03-26)

### PARAMETER
- When a regulation has both a filing/publication date and an effective date, always use the effective date for the parameter entry; the filing date (e.g., "filed June 5, 2003") can precede the effective date (e.g., "Beginning January 1, 2004") by months, and using the wrong one causes benefits to appear in a period before they legally exist.
- When a secondary source provides combined federal+state benefit amounts, back-calculate the implied parameter values and compare them against the implemented values; a mismatch (e.g., implied $47.64/day vs implemented $39.35/day) may reveal that parameter values have been updated in an era not covered by available primary sources — flag this in the PR description as a verification TODO rather than silently shipping potentially stale values.

### FORMULA
- Never use `WEEKS_IN_YEAR * 7` to compute days per year; the framework constant `WEEKS_IN_YEAR` is the integer 52 (not 52.1429), so `52 * 7 = 364`, not 365. Use the literal `365` (or `DAYS_IN_YEAR` if available) for days-per-year calculations. This error cascaded to all monetary test values in the session.

### REFERENCE
- When fetching regulation text from legal databases (e.g., Cornell LII, Westlaw), verify that the saved file contains the actual regulation body text, not just a JavaScript shell; many legal databases render content client-side, so automated fetches (curl, wget, WebFetch) capture only the HTML/JS skeleton with no regulation text. If the body is empty or contains only script tags, the source is unusable for verification — flag it and request manual access.
