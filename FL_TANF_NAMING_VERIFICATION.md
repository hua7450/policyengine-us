# Florida TANF Naming Convention - Verification Report

**Date**: 2025-10-22
**Status**: VERIFIED - All existing variables follow the established convention

## Existing Implementation Review

### Variables Implemented (15 total)

All variables follow the `fl_tanf_{component}` pattern:

1. `fl_tanf.py` - Main benefit variable ✅
2. `fl_tanf_categorically_eligible.py` - Categorical eligibility ✅
3. `fl_tanf_countable_earned_income.py` - Countable earned income ✅
4. `fl_tanf_countable_income.py` - Total countable income ✅
5. `fl_tanf_countable_unearned_income.py` - Countable unearned income ✅
6. `fl_tanf_earned_income_disregard.py` - Earned income disregard ✅
7. `fl_tanf_eligible.py` - Overall eligibility ✅
8. `fl_tanf_family_cap_reduction.py` - Family cap reduction ✅
9. `fl_tanf_gross_earned_income.py` - Gross earned income ✅
10. `fl_tanf_gross_income.py` - Total gross income ✅
11. `fl_tanf_gross_unearned_income.py` - Gross unearned income ✅
12. `fl_tanf_income_eligible.py` - Income eligibility ✅
13. `fl_tanf_payment_standard.py` - Payment standard ✅
14. `fl_tanf_resource_eligible.py` - Resource eligibility ✅
15. `fl_tanf_shelter_tier.py` - Shelter tier ✅

### Test Files

1. `integration.yaml` - Integration test ✅ (Correctly named)

### Directory Structure

```
policyengine_us/variables/gov/states/fl/dcf/tanf/
├── fl_tanf.py
├── benefit/
│   ├── fl_tanf_family_cap_reduction.py
│   ├── fl_tanf_payment_standard.py
│   └── fl_tanf_shelter_tier.py
├── eligibility/
│   ├── fl_tanf_categorically_eligible.py
│   ├── fl_tanf_eligible.py
│   ├── fl_tanf_income_eligible.py
│   └── fl_tanf_resource_eligible.py
└── income/
    ├── fl_tanf_countable_earned_income.py
    ├── fl_tanf_countable_income.py
    ├── fl_tanf_countable_unearned_income.py
    ├── fl_tanf_earned_income_disregard.py
    ├── fl_tanf_gross_earned_income.py
    ├── fl_tanf_gross_income.py
    └── fl_tanf_gross_unearned_income.py
```

## Naming Convention Compliance

### ✅ Compliant Patterns

- All variables use `fl_tanf_` prefix
- All variables use snake_case
- Variable names are descriptive but concise
- Subdirectory organization (benefit/, eligibility/, income/) is logical and consistent
- Test file correctly named `integration.yaml` (not `fl_tanf_integration.yaml`)

### Pattern Analysis by Category

#### Eligibility Variables (4)
- `fl_tanf_eligible` - Overall eligibility
- `fl_tanf_income_eligible` - Income eligibility test
- `fl_tanf_resource_eligible` - Resource eligibility test
- `fl_tanf_categorically_eligible` - Categorical eligibility test

**Pattern**: `fl_tanf_{criteria}_eligible`

#### Income Variables (7)

Gross Income:
- `fl_tanf_gross_earned_income`
- `fl_tanf_gross_unearned_income`
- `fl_tanf_gross_income`

Countable Income:
- `fl_tanf_countable_earned_income`
- `fl_tanf_countable_unearned_income`
- `fl_tanf_countable_income`

Disregards:
- `fl_tanf_earned_income_disregard`

**Pattern**: `fl_tanf_{gross|countable}_{earned|unearned}_income` or `fl_tanf_{type}_disregard`

#### Benefit Calculation Variables (3)
- `fl_tanf_payment_standard` - Maximum benefit amount
- `fl_tanf_shelter_tier` - Shelter cost tier
- `fl_tanf_family_cap_reduction` - Family cap reduction amount

**Pattern**: `fl_tanf_{component}`

## Consistency with Other States

### Comparison with Similar State Patterns

| State | Main Variable | Eligibility | Gross Income | Countable Income | Payment/Standard |
|-------|---------------|-------------|--------------|------------------|------------------|
| FL | `fl_tanf` | `fl_tanf_eligible` | `fl_tanf_gross_earned_income` | `fl_tanf_countable_income` | `fl_tanf_payment_standard` |
| CO | `co_tanf` | `co_tanf_eligible` | N/A | `co_tanf_countable_gross_earned_income` | `co_tanf_grant_standard` |
| IL | `il_tanf` | `il_tanf_eligible` | `il_tanf_gross_earned_income` | `il_tanf_countable_income_for_grant_calculation` | `il_tanf_payment_level_for_grant_calculation` |
| TX | `tx_tanf` | `tx_tanf_eligible` | `tx_tanf_gross_earned_income` | `tx_tanf_countable_income` | `tx_tanf_payment_standard` |
| DC | `dc_tanf` | `dc_tanf_eligible` | `dc_tanf_gross_earned_income` | `dc_tanf_countable_income` | `dc_tanf_standard_payment` |

**Observation**: Florida's naming is HIGHLY CONSISTENT with Texas and DC patterns, which is ideal.

## Recommendations

### For Future Development

1. **Additional Variables Likely Needed**:
   - None currently identified - implementation appears complete for basic TANF calculation

2. **If Additional Variables Are Added**:
   - Continue using `fl_tanf_` prefix
   - Reference similar variables in TX and DC implementations (they have very similar structures)
   - Keep variable names under 50 characters when possible

3. **Parameter Development**:
   - Continue using `gov.states.fl.dcf.tanf` as base path
   - Use subdirectories for logical grouping (already established)

4. **Test Development**:
   - Add unit tests named after each variable (e.g., `fl_tanf_eligible.yaml`)
   - Keep integration test as `integration.yaml`

## Summary

The Florida TANF implementation follows the established naming conventions PERFECTLY:

- ✅ All 15 variables use consistent `fl_tanf_` prefix
- ✅ All variables use snake_case
- ✅ Variable names are descriptive and appropriate length
- ✅ Directory structure is logical and organized
- ✅ Test file naming follows conventions
- ✅ Patterns match similar state implementations (TX, DC)
- ✅ No inconsistencies or deviations detected

**Conclusion**: The naming convention document accurately reflects the existing implementation, and the existing implementation serves as an excellent reference for future development.

