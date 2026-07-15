# Agent Lessons Learned

Accumulated from /encode-policy-v2 and /backdate-program runs across all contributors.
Loaded by implementation agents on future runs.

## New Lessons from Tennessee CCAP (2026-07-15)

### PARAMETER
- To decide whether a rate differential/enhancement is ADDITIVE (stacks on the base) or BAKED-IN (already inside the base row), compare the SAME table cell across two eras where the differential was added or removed: if the base cell is unchanged across the differential's elimination, it was never baked in (additive); if it dropped by the differential amount, it was baked in. Corroborate by checking the enhanced (e.g., QRIS-bonus) columns equal base × (1 + bonus) — that proves the table cells are the plain base and the enhancements stack multiplicatively on top.

### VARIABLE
- Every category on a State Plan copay-WAIVER checklist should be swept against existing PolicyEngine inputs before declaring it unmodelable — e.g. a Head Start / Early Head Start waiver maps to the standing `is_enrolled_in_head_start` input (AL/FL/SC precedent). Grep sibling states' waiver OR-sets for an available hook rather than assuming the category has none. (Broadens the KY protective-services grep rule from that one pathway to copay-waiver categories generally.)

### REFERENCE
- When a rate/eligibility CHART carries its own enumeration footnote (e.g., a Top-Tier county list printed on the chart), that footnote is the authoritative membership list — it beats the upstream analytic/ranking document the chart is derived FROM (e.g., a Market Rate Survey ranking), which can omit entries added by other mechanisms (employer-petition additions). Encode from the chart's enumeration, not the ranking source it was built on.
- A footnote reference marker (e.g., "(a)") placed on SPECIFIC ROWS of a rate table scopes that footnote's rule to only the marked rows; a footnoted adjustment (e.g., part-time halving) must be gated to the rows bearing the marker, not applied table-wide. Read which rows carry the marker before encoding any footnoted rule — row-marker placement is load-bearing.
- When a document's PROSE states a count (e.g., "these 26 counties") but its own enumerated list contains a different number of items (25), trust the enumeration over the prose count — the prose figure is frequently a stale carryover from a prior edition. Count the list; do not accept the stated total.
- When one variable's formula encodes several distinct sourced rules (e.g., a copay rate, a part-time share, and a set of waivers), its `reference =` tuple must carry a page anchor for EACH rule's location — a single stale anchor pointing at only one of them is an incomplete citation even when the value it lands on is correct.

### FORMULA
- When a rate/copay chart gives BOTH a prose formula and a worked numeric example, reproduce the worked example's arithmetic exactly — it can reveal operations the prose omits (e.g., a SECOND whole-dollar floor applied after the percentage step), and the worked example governs over the prose reading. (Distinct from verifying cap semantics: this is about the COUNT of rounding/flooring operations, which prose routinely understates.)
- When a footnote says a differential is applied "above the current reimbursement rates," the base it multiplies is the provider's APPLICABLE (e.g., QRIS-tier-boosted) rate column, not the plain unenhanced base row — stack the differential on the already-enhanced rate.
- The same program can legitimately use DIFFERENT week-to-month conversion factors for different components — e.g. 4.3 for a copay the chart explicitly specifies vs `WEEKS_IN_YEAR / MONTHS_IN_YEAR` (4.333) for a benefit annualization the chart is silent on. Match each component to its own source; do not "unify" the factor, and do not flag the divergence as an inconsistency. (Extends the "use the chart's exact conversion factor" rule to within-program divergence.)
