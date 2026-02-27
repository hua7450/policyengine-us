# California CalWORKs - Implementation Spec (Consolidated)

## Summary of Current Implementation

The CalWORKs implementation is **well-structured and largely correct** for current-period values. It covers:

### Variables (19 files):
- `ca_tanf.py` - Main benefit calculation (MAP - countable income, prorated by immigration-eligible fraction)
- `ca_tanf_eligible.py` - Overall eligibility (demographic + financial + resources + vehicle)
- `ca_tanf_financial_eligible.py` - Financial eligibility using `is_tanf_enrolled` to distinguish applicants vs recipients
- `ca_tanf_applicant_financial_test.py` - Applicant gross income vs MBSAC
- `ca_tanf_recipient_financial_test.py` - Recipient net income vs MAP
- `ca_tanf_maximum_payment.py` - MAP lookup by region/exempt status/AU size
- `ca_tanf_income_limit.py` - MBSAC lookup by region/AU size
- `ca_tanf_countable_income_applicant.py` - Applicant income: earned - $450/person disregard + unearned
- `ca_tanf_countable_income_recipient.py` - Recipient income: $600 flat disregard + 50% remaining earned
- `ca_tanf_region1.py` - Region determination by county
- `ca_tanf_exempt.py` - Exempt/non-exempt status
- `ca_tanf_earned_income.py`, `ca_tanf_db_unearned_income.py`, `ca_tanf_other_unearned_income.py` - Income sources
- `ca_tanf_resources.py`, `ca_tanf_resources_limit.py`, `ca_tanf_resources_eligible.py` - Resource eligibility
- `ca_tanf_vehicle_value_eligible.py` - Vehicle value test
- `ca_tanf_immigration_status_eligible_person.py` - Immigration status eligibility

### Parameters (20+ files):
- MAP: 4 files (region1/region2 x exempt/non_exempt), each with breakdown by AU size 1-10
- MBSAC: 2 files (region1/region2), each with breakdown by AU size 1-10
- Income disregards: 3 files (applicant flat, recipient flat, recipient percentage)
- Resources: 4 files (vehicle, with/without elderly, age threshold)
- Income sources: 3 files (earned, db_unearned, other_unearned)
- Other: region1_counties, exempt conditions, immigration statuses, max_au_size

---

## Validation Against Regulatory Sources

### Tier A: Current Values Verified Correct

| Parameter | Implemented | Verified Source | Status |
|---|---|---|---|
| Region 1 Non-Exempt MAP (10/01/2024) | $734-$2,876 | Santa Clara DEBS, LA DPSS | CORRECT |
| Region 1 Exempt MAP (10/01/2024) | $809-$3,215 | LA DPSS, EHSD | CORRECT |
| Region 2 Non-Exempt MAP (10/01/2024) | $695-$2,731 | Santa Clara DEBS Region 2 | CORRECT |
| Region 2 Exempt MAP (10/01/2024) | $770-$3,054 | Santa Clara DEBS Region 2 | CORRECT |
| Recipient EID flat ($600) | $600 (2022-06-01) | LA DPSS ePolicies, LSNC | CORRECT |
| Recipient EID percentage (50%) | 0.5 (2022-06-01) | LA DPSS ePolicies | CORRECT |
| Applicant EID flat ($450) | $450 (2022-07-01) | LA DPSS ePolicies, LSNC | CORRECT |
| Vehicle limit ($32,968) | $32,968 (2024-07-01) | ACL 24-36 | CORRECT |

### Tier A: Issues Found

#### Issue 1: MBSAC (Income Limit) Values Need Update
- **Region 1 MBSAC**: Currently has values only for `2023-01-01`. Missing `2024-07-01` (4.32% COLA) and `2025-07-01` values.
  - Region 1 MBSAC 2024-07-01: $899, $1,476, $1,829, $2,080(?), ... (from LSNC/ACL 24-37)
  - Region 1 MBSAC 2025-07-01: $930, $1,526, $1,892, $2,244, $2,561, $2,880, $3,166, $3,445, $3,738, $4,056 (from Santa Clara DEBS)
- **Region 2 MBSAC**: Currently has values only for `2023-07-01`. Missing `2024-07-01` and `2025-07-01`.
  - Region 2 MBSAC 2024-07-01: $853, $1,401, $1,736, ... (from LSNC/ACL 24-37)
  - Region 2 MBSAC 2025-07-01: $882, $1,449, $1,795, $2,134, $2,441, $2,741, $3,002, $3,279, $3,544, $3,858 (from Santa Clara DEBS)

#### Issue 2: Resource Limit Values May Be Incorrect for 2025
- Implementation: $12,137 (2025-01-01 without elderly), $18,206 (2025-01-01 with elderly)
- Research found: $12,552 (2025 from ACL 25-65 / DB101), $18,829 (2025 from ACL 25-65 / DB101)
- **Need to verify**: The discrepancy may be due to different effective dates (Jan 2025 vs later in 2025). ACL 25-65 was issued September 2025 with effective date January 1, 2026.

#### Issue 3: Region 1 MAP Date Discrepancy
- Region 1 non_exempt.yaml and exempt.yaml have `2023-01-01` as the first date entry, with a comment `# Actual date: 2023-10-01`
- Region 2 files correctly use `2023-10-01`
- The 3.6% MAP increase was effective October 1, 2023 (per ACL 23-74), so the Region 1 files should use `2023-10-01`, not `2023-01-01`

### Tier B: Missing Historical Parameters (Backdating Needed)

All parameter files currently have only 1-2 date entries. Historical values are needed for:

#### MAP Payment Standards (4 files):
| Period | Change | Need Values For |
|---|---|---|
| 1998-01-01 | CalWORKs creation | 4 files x 10 sizes |
| Multiple dates through 2023 | Various COLAs/cuts/restorations | See timeline in working_references.md |

Key historical MAP milestones:
- 1997-98: Original CalWORKs levels (~$565 for 3-person R1 non-exempt)
- 2009-07-01: 4% grant reduction
- 2011-06-01: 8% MAP reduction
- 2014-03-01: 5% restoration
- 2016-17: 1.43% increase
- 2021-10-01: 5.3% increase
- 2022-10-01: 11% increase
- 2023-10-01: 3.6% increase
- 2024-10-01: 0.3% increase

#### MBSAC (2 files):
- Need annual values from CalWORKs creation (adjusted July 1 each year by CNI)
- CDSS MAP-MBSAC.pdf (being rendered by prep-1) has comprehensive historical data

#### Earned Income Disregards (3 files):
| Parameter | Historical Values Needed |
|---|---|
| Applicant flat | 1998-01-01: $90, 2022-07-01: $450 |
| Recipient flat | 1998-01-01: $225, 2011-06-01: $112, 2012-07-01: $225, 2020-06-01: $500, 2021-06-01: $550, 2022-06-01: $600 |
| Recipient percentage | 1998-01-01: 0.5 (unchanged) |

#### Resource Limits:
- Need historical values from CalFresh alignment dates
- Vehicle limit history: $4,650 (1997) -> ... -> $32,045 (2023) -> $32,968 (2024)

### Tier C: Formula/Logic Issues

#### Issue C1: Applicant Income Calculation
The applicant countable income formula subtracts the flat $450 disregard as a total, not per-employed-person:
```python
yearly_disregard = p.flat * MONTHS_IN_YEAR
countable_earned = max_(spm_unit("ca_tanf_earned_income", period) - yearly_disregard, 0)
```
Per regulation (WIC 11450.12), the $450 is per **each employed person** in the AU, not a flat amount for the whole AU. This may be a simplification for the PolicyEngine model (since income is aggregated at SPMUnit level), but should be verified/documented.

#### Issue C2: Recipient Income Formula - DBI Priority
The current recipient formula correctly implements the DBI-first priority for the $600 disregard:
```python
countable_db_unearned = max_(db_unearned - p.flat, 0)
remaining_flat_exclusion = max_(p.flat - db_unearned, 0)
countable_earned = max_(earned - remaining_flat_exclusion, 0) * (1 - p.percentage)
```
This is CORRECT per regulation: the $600 applies first to disability-based income, then any remainder to earned income.

---

## Implementation Priority

### Priority 1 (Tier A - YAML Updates Only):
1. **Fix Region 1 MAP dates**: Change `2023-01-01` to `2023-10-01` in region1/exempt.yaml and region1/non_exempt.yaml
2. **Add MBSAC 2024 and 2025 values**: Add entries for both regions
3. **Verify 2025 resource limits**: Cross-check ACL 25-65 effective dates

### Priority 2 (Tier B - Historical Backdating):
4. **Backdate EID parameters**: Add historical entries (most critical: $225 -> $112 -> $225 -> $500 -> $550 -> $600)
5. **Backdate MAP parameters**: Add historical entries from CDSS MAP-MBSAC.pdf (awaiting prep-1 rendering)
6. **Backdate MBSAC parameters**: Add historical entries from CDSS MAP-MBSAC.pdf

### Priority 3 (Tier C - Formula Review):
7. **Review applicant per-person disregard**: Determine if current implementation is acceptable simplification or needs fix
8. **Add reference quality**: Update reference URLs to use more permanent CDSS sources rather than county ePolicies

---

## Cross-Reference Data Sources

| Data Point | Primary Source | Cross-Check Sources |
|---|---|---|
| MAP values | CDSS ACLs | Santa Clara DEBS, LA DPSS, CCWRO tables |
| MBSAC values | CDSS ACLs | Santa Clara DEBS, LSNC Reg Summaries |
| EID amounts | WIC 11451.5, ACLs | LA DPSS ePolicies, LSNC |
| Resource limits | CDSS ACLs | DB101, county fact sheets |
| Historical MAP | CDSS MAP-MBSAC.pdf | CCWRO tables, LAO analyses |
| Historical MBSAC | CDSS MAP-MBSAC.pdf | CCWRO tables |
