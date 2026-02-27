# California CalWORKs - Formula Review vs Regulations

## Overall Assessment

The CalWORKs implementation is **structurally sound** and follows correct CalWORKs regulations for the current period. The variable dependency graph is well-designed and matches the actual program flow. No zero-sentinel anti-patterns, no hardcoded year-checks, no unused parameters.

---

## Variable-by-Variable Review

### 1. `ca_tanf.py` (Main Benefit Calculation)
**Formula:** `prorated_fraction * min(max(MAP - countable_income, 0), MAP)`
**Regulation:** WIC 11450 - Grant = MAP - net countable income
**Verdict:** CORRECT
- Correctly caps benefit at MAP (prevents negative income inflation)
- Correctly prorates by immigration-eligible fraction
- No issues

### 2. `ca_tanf_eligible.py`
**Formula:** `demographic & financial & resources & vehicle`
**Regulation:** CalWORKs requires demographic, financial, resource, and vehicle eligibility
**Verdict:** CORRECT
- All four eligibility checks are present

### 3. `ca_tanf_financial_eligible.py`
**Formula:** `where(tanf_enrolled, recipient_test, applicant_test & recipient_test)`
**Regulation:** Applicants must pass both applicant (MBSAC gross income) and recipient (MAP net income) tests; recipients only need recipient test
**Verdict:** CORRECT
- Correctly uses `is_tanf_enrolled` per CLAUDE.md TANF instructions
- Logic matches regulation: applicants face both tests, recipients face only the net income test

### 4. `ca_tanf_applicant_financial_test.py`
**Formula:** `countable_income_applicant <= income_limit`
**Regulation:** Applicant gross income (after $450/person disregard) must be <= MBSAC
**Verdict:** CORRECT (but see applicant income issue below)

### 5. `ca_tanf_recipient_financial_test.py`
**Formula:** `countable_income_recipient < maximum_payment`
**Regulation:** Recipient net income (after $600 + 50% disregard) must be < MAP
**Verdict:** CORRECT
- Note: uses strict `<` not `<=`, which is correct per CalWORKs rules (if net income equals MAP, grant would be $0)

### 6. `ca_tanf_maximum_payment.py`
**Formula:** Looks up MAP by region, exempt status, and AU size (capped at max_au_size)
**Regulation:** MAP varies by Region 1/2, exempt/non-exempt, and family size 1-10+
**Verdict:** CORRECT
- Correctly uses `where` for region selection
- Correctly uses `min_(unit_size, p.max_au_size)` for AU sizes > 10

### 7. `ca_tanf_income_limit.py` (MBSAC lookup)
**Formula:** Looks up MBSAC by region and AU size, adds per-person increment for AU > 10
**Regulation:** MBSAC is per family size, with additional per-person amount for sizes > 10
**Verdict:** CORRECT
- Correctly handles additional persons beyond max AU size

### 8. `ca_tanf_countable_income_applicant.py`
**Formula:** `max(earned - $450*12, 0) + db_unearned + other_unearned`
**Regulation:** WIC 11450.12 - Subtract $450 from **each employed person's** earned income
**Verdict:** POTENTIAL ISSUE (Tier C)
- The code applies $450 as a flat total disregard for the entire SPMUnit
- Regulation says $450 **per employed person**
- Example: Family with 2 working adults should get $900 disregard, not $450
- **Impact:** Families with multiple workers would have higher countable income than they should, potentially failing the applicant test incorrectly
- **Note:** This may be a known simplification given SPMUnit-level income aggregation

### 9. `ca_tanf_countable_income_recipient.py`
**Formula:**
```
db_countable = max(db_monthly - $600, 0)
remaining_flat = max($600 - db_monthly, 0)
earned_countable = max(earned_monthly - remaining_flat, 0) * 0.5
total = (db_countable + earned_countable + other_unearned) * 12
```
**Regulation:** WIC 11451.5 - $600 disregard applies first to DBI, remainder to earned; then 50% of remaining earned income
**Verdict:** CORRECT
- DBI-first priority is correctly implemented
- Remaining flat exclusion correctly cascades to earned income
- 50% disregard correctly applied after flat deduction
- Monthly-to-yearly conversion is correct

### 10. `ca_tanf_exempt.py`
**Formula:** Uses `adds` pattern checking for SSI, IHSS, SDI, workers_comp
**Regulation:** Exempt if all adult caretakers receive SSI/SSP, IHSS, SDI, workers' comp, or temporary disability
**Verdict:** POTENTIAL CONCERN
- The `adds` pattern sums boolean values - this checks if **any** member receives these benefits
- Regulation requires **all** adult caretakers to receive qualifying benefits
- This may lead to incorrect exempt classification if one adult has SSI but the other does not
- **Note:** Need to verify how `adds` is used in the context of SPMUnit boolean aggregation

### 11. `ca_tanf_region1.py`
**Formula:** Checks if household county is in Region 1 list
**Regulation:** 17 counties in Region 1 per WIC 11452.018
**Verdict:** CORRECT
- All 17 Region 1 counties match the statutory list

### 12. `ca_tanf_resources_eligible.py` and `ca_tanf_resources_limit.py`
**Formula:** Resources <= limit (higher limit for elderly/disabled)
**Regulation:** Resource limit tied to CalFresh limits, higher for families with 60+ or disabled members
**Verdict:** CORRECT

### 13. `ca_tanf_vehicle_value_eligible.py`
**Formula:** Vehicle value <= vehicle limit parameter
**Regulation:** One vehicle exempt up to limit
**Verdict:** CORRECT but simplified
- Regulation exempts one vehicle up to the limit; the code checks total household vehicle value
- This may overcount if family has multiple vehicles

### 14. Income Source Variables (`ca_tanf_earned_income`, `ca_tanf_db_unearned_income`, `ca_tanf_other_unearned_income`)
**Formula:** Each uses `adds` pattern to sum income sources from parameter lists
**Verdict:** CORRECT
- Income source definitions match regulation categories

### 15. `ca_tanf_immigration_status_eligible_person.py`
**Formula:** Checks person's immigration status against eligible list
**Verdict:** CORRECT
- Note: Reference URL points to child care section, not cash assistance section (minor reference error)

---

## Issues Summary

### Critical (affects benefit accuracy):
**NONE identified** - All formulas produce correct results for the most common scenarios.

### Moderate (edge case accuracy):
1. **Applicant per-person disregard** (Issue C1): $450 applied as flat total, not per employed person. Affects multi-worker families.
2. **Exempt status determination** (Issue C2): May incorrectly classify partially-exempt AUs. Needs verification of `adds` pattern behavior.

### Minor (reference/documentation):
3. **Immigration status reference**: Points to child care section URL instead of cash assistance eligibility.
4. **Date comments**: Multiple files have `# Actual date:` comments indicating the implemented dates differ from actual effective dates.

### No Issues Found:
- No zero-sentinel anti-patterns
- No hardcoded year-checks or period-conditional logic
- No unused parameters
- No redundant logic
- Monthly/yearly conversions are consistent throughout
- DBI-first priority correctly implemented
- Region determination correctly matches statutory county list
- Resource and vehicle tests correctly structured
