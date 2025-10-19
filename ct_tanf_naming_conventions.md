# Connecticut TANF Variable Naming Conventions

**Program**: Connecticut TANF (Temporary Family Assistance)  
**State Abbreviation**: `ct`  
**Analysis Date**: 2025-10-19

## Summary

This document establishes the variable naming conventions for Connecticut TANF based on analysis of existing state TANF implementations (IL, TX, DC, MD, CA, CO, NY, NJ, NC).

## Standard Naming Pattern

All Connecticut TANF variables follow this pattern:

```
{state}_{program}_{component}
```

Where:
- `state` = `ct` (lowercase, 2-letter state code)
- `program` = `tanf` (lowercase)
- `component` = descriptive component name (snake_case)

## Entity Level Patterns

- **Person-level variables**: Use `Person` entity for individual eligibility, demographics, and per-person income
- **SPMUnit-level variables**: Use `SPMUnit` entity for household-level calculations, benefits, and aggregated income

## Complete Variable Naming Specification

### 1. Main Benefit Variable

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf` | SPMUnit | float | Main TANF benefit amount |

### 2. Eligibility Variables

#### Household-Level Eligibility

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_eligible` | SPMUnit | bool | Overall TANF eligibility |
| `ct_tanf_income_eligible` | SPMUnit | bool | Meets income requirements |
| `ct_tanf_resources_eligible` | SPMUnit | bool | Meets resource/asset requirements |
| `ct_tanf_non_financial_eligible` | SPMUnit | bool | Meets non-financial requirements |

#### Person-Level Eligibility

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_eligible_child` | Person | bool | Child eligible for TANF assistance unit |
| `ct_tanf_eligible_parent` | Person | bool | Parent/caretaker eligible for assistance unit |
| `ct_tanf_demographic_eligible_person` | Person | bool | Meets demographic requirements (age, dependency) |
| `ct_tanf_immigration_status_eligible_person` | Person | bool | Meets immigration status requirements |
| `ct_tanf_categorically_eligible_person` | Person | bool | Meets categorical eligibility (not on SSI, etc.) |

### 3. Assistance Unit Variables

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_assistance_unit_size` | SPMUnit | int | Number of people in TANF assistance unit |
| `ct_tanf_payment_eligible_child` | Person | bool | Child included in payment calculation (IL pattern) |
| `ct_tanf_payment_eligible_parent` | Person | bool | Parent included in payment calculation (IL pattern) |

### 4. Income Variables

#### Gross Income (Person-Level)

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_gross_earned_income` | Person | float | Total earned income before deductions |
| `ct_tanf_gross_unearned_income` | Person | float | Total unearned income before exclusions |

#### Countable Income (SPMUnit-Level)

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_countable_earned_income` | SPMUnit | float | Earned income after deductions/disregards |
| `ct_tanf_countable_unearned_income` | SPMUnit | float | Unearned income after exclusions |
| `ct_tanf_countable_income` | SPMUnit | float | Total countable income (earned + unearned) |

#### Income for Different Purposes (if needed)

If Connecticut has different income tests for initial eligibility vs. ongoing benefit calculation (like Illinois):

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_countable_income_for_initial_eligibility` | SPMUnit | float | Income for initial eligibility determination |
| `ct_tanf_countable_income_for_grant_calculation` | SPMUnit | float | Income for benefit amount calculation |

#### Per-Person Income After Disregards (if needed)

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_earned_income_after_disregard_person` | Person | float | Person's earned income after applying disregards |

### 5. Deduction Variables

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_dependent_care_deduction` | SPMUnit | float | Child care/dependent care expense deduction |
| `ct_tanf_child_support_deduction` | SPMUnit | float | Child support paid deduction |
| `ct_tanf_work_related_deduction` | SPMUnit | float | Work-related expenses deduction |
| `ct_tanf_standard_deduction` | SPMUnit | float | Standard/flat deduction amount |

If there are person-level deductions (like Illinois):

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_childcare_deduction_person` | Person | float | Per-person childcare deduction |

### 6. Resource/Asset Variables

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_countable_resources` | SPMUnit | float | Total countable resources/assets |
| `ct_tanf_countable_vehicle_value` | SPMUnit | float | Vehicle value after exemption |
| `ct_tanf_liquid_resources` | SPMUnit | float | Cash, checking, savings accounts |

### 7. Benefit Calculation Variables

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_payment_standard` | SPMUnit | float | Maximum benefit amount by family size |
| `ct_tanf_standard_payment` | SPMUnit | float | Standard payment amount (DC pattern) |
| `ct_tanf_needs_standard` | SPMUnit | float | Needs standard for budgeting (TX pattern) |
| `ct_tanf_payment_level` | SPMUnit | float | Payment level for calculations (IL pattern) |

### 8. Age Threshold and Demographic Variables

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_age_eligible_child` | Person | bool | Child meets age requirements |
| `ct_tanf_student_age_limit` | Person | bool | Student meeting extended age limit |

### 9. Work Requirement Variables (if applicable)

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_work_requirement_exempt` | Person | bool | Exempt from work requirements |
| `ct_tanf_is_working` | Person | bool | Currently meeting work requirements |
| `ct_tanf_meets_work_requirements` | SPMUnit | bool | Household meets work requirements |
| `ct_tanf_work_participation_hours` | Person | float | Hours of work activities |

### 10. Special Program Components (if applicable)

If Connecticut has special components like Texas OTTANF (One-Time TANF):

| Variable Name | Entity | Type | Description |
|--------------|--------|------|-------------|
| `ct_tanf_emergency_assistance` | SPMUnit | float | Emergency/crisis assistance |
| `ct_tanf_diversion_payment` | SPMUnit | float | Diversion/one-time payment |

## Parameter Naming Pattern

Parameters should follow this path structure:

```
gov.states.ct.dss.tanf.{category}.{parameter_name}
```

### Common Parameter Paths

```yaml
gov.states.ct.dss.tanf.payment_standard          # Maximum benefit amounts
gov.states.ct.dss.tanf.income_limits             # Income eligibility limits
gov.states.ct.dss.tanf.resources                 # Resource/asset limits
gov.states.ct.dss.tanf.age_threshold             # Age limits for eligibility
gov.states.ct.dss.tanf.income.deductions         # Income deductions
gov.states.ct.dss.tanf.income.disregards         # Earned income disregards
gov.states.ct.dss.tanf.income.sources.earned     # Earned income sources
gov.states.ct.dss.tanf.income.sources.unearned   # Unearned income sources
```

## Directory Structure

Files should be organized in this structure:

```
policyengine_us/variables/gov/states/ct/dss/tanf/
├── ct_tanf.py                           # Main benefit
├── assistance_unit/
│   ├── ct_tanf_assistance_unit_size.py
│   ├── ct_tanf_eligible_child.py
│   └── ct_tanf_eligible_parent.py
├── eligibility/
│   ├── ct_tanf_eligible.py
│   ├── ct_tanf_income_eligible.py
│   ├── ct_tanf_resources_eligible.py
│   ├── ct_tanf_demographic_eligible_person.py
│   └── ct_tanf_immigration_status_eligible_person.py
├── income/
│   ├── ct_tanf_countable_income.py
│   ├── earned/
│   │   ├── ct_tanf_gross_earned_income.py
│   │   └── ct_tanf_countable_earned_income.py
│   ├── unearned/
│   │   ├── ct_tanf_gross_unearned_income.py
│   │   └── ct_tanf_countable_unearned_income.py
│   └── deductions/
│       ├── ct_tanf_dependent_care_deduction.py
│       └── ct_tanf_child_support_deduction.py
├── resources/
│   └── ct_tanf_countable_resources.py
└── ct_tanf_payment_standard.py
```

## Test File Naming

### Unit Tests
- Name unit test files after the variable: `{variable_name}.yaml`
- Examples:
  - `ct_tanf.yaml`
  - `ct_tanf_eligible.yaml`
  - `ct_tanf_gross_earned_income.yaml`
  - `ct_tanf_countable_income.yaml`

### Integration Tests
- Use `integration.yaml` for integration tests
- Place in the module directory (e.g., `/tanf/tests/integration.yaml`)
- **DO NOT** use `ct_tanf_integration.yaml` - always use just `integration.yaml`

## Key Patterns Observed

### Pattern 1: State Prefix Always First
✅ **Correct**: `ct_tanf_eligible`  
❌ **Incorrect**: `tanf_ct_eligible`

### Pattern 2: Income Type Organization
- Gross income → Deductions/Disregards → Countable income
- Example flow:
  1. `ct_tanf_gross_earned_income` (Person)
  2. Apply disregards/deductions
  3. `ct_tanf_countable_earned_income` (SPMUnit)

### Pattern 3: Eligibility Hierarchy
- Person-level: `ct_tanf_eligible_child`, `ct_tanf_demographic_eligible_person`
- Household-level: `ct_tanf_eligible`, `ct_tanf_income_eligible`

### Pattern 4: Use of "Countable" vs "Gross"
- **Gross**: Before any deductions/exclusions
- **Countable**: After deductions/exclusions applied

### Pattern 5: Agency Abbreviations
Connecticut uses **DSS** (Department of Social Services):
- Parameter path: `gov.states.ct.dss.tanf`
- Not `ct.tanf` or `ct.dhs.tanf`

## Consistency Rules

1. **Always use lowercase** for state code, program name, and components
2. **Use snake_case** for multi-word components (not camelCase or PascalCase)
3. **Use full words** when possible (avoid abbreviations except standard ones)
4. **Be specific**: Use `ct_tanf_gross_earned_income` not `ct_tanf_income`
5. **Entity alignment**: Person-level for individual attributes, SPMUnit for aggregations
6. **No redundancy**: Don't use `ct_tanf_tanf_eligible` - the program is implied

## Variables That Should NOT Use State Prefix

Some variables are used across programs and should NOT have the `ct_tanf_` prefix:

- `is_tax_unit_dependent`
- `is_in_secondary_school`
- `monthly_age` or `age`
- `is_pregnant`
- `childcare_expenses`
- `household_vehicles_value`
- `spm_unit_cash_assets`

These are general-purpose variables used by multiple programs.

## Examples from Analysis

### Illinois TANF Patterns
- `il_tanf`, `il_tanf_eligible`
- `il_tanf_gross_earned_income`, `il_tanf_countable_earned_income_for_grant_calculation`
- `il_tanf_payment_eligible_child`, `il_tanf_assistance_unit_size`

### Texas TANF Patterns
- `tx_tanf`, `tx_regular_tanf`, `tx_ottanf`
- `tx_tanf_gross_earned_income`, `tx_tanf_countable_earned_income`
- `tx_tanf_eligible_child`, `tx_tanf_assistance_unit_size`
- `tx_tanf_payment_standard`, `tx_tanf_budgetary_needs`

### DC TANF Patterns
- `dc_tanf`, `dc_tanf_eligible`
- `dc_tanf_standard_payment`, `dc_tanf_countable_income`
- `dc_tanf_demographic_eligible_person`, `dc_tanf_immigration_status_eligible_person`

## Reference Files Analyzed

1. `/policyengine_us/variables/gov/states/il/dhs/tanf/` - Illinois TANF (comprehensive)
2. `/policyengine_us/variables/gov/states/tx/tanf/` - Texas TANF (complex eligibility)
3. `/policyengine_us/variables/gov/states/dc/dhs/tanf/` - DC TANF (standard pattern)
4. `/policyengine_us/variables/gov/states/md/tanf/` - Maryland TANF (simple)
5. Additional states: CA, CO, NY, NJ, NC - for validation

## Decision Log

1. **State abbreviation**: Use `ct` (lowercase) following all existing patterns
2. **Program name**: Use `tanf` (not `tfa` or full name)
3. **Entity choice**: Follow IL/TX pattern - Person for eligibility checks, SPMUnit for income/benefits
4. **Income organization**: Follow three-tier structure: gross → deductions → countable
5. **Assistance unit**: Include both `eligible_child`/`eligible_parent` and optional `payment_eligible_*` variants
6. **Agency path**: Use `dss` for Connecticut's Department of Social Services

## Implementation Checklist

When implementing CT TANF, ensure:

- [ ] All variable names follow `ct_tanf_{component}` pattern
- [ ] Person-level variables use `Person` entity
- [ ] SPMUnit-level variables use `SPMUnit` entity
- [ ] Income flows from gross → countable correctly
- [ ] Test files named after variables (not `ct_tanf_integration.yaml`)
- [ ] Parameters use `gov.states.ct.dss.tanf.*` path
- [ ] Directory structure matches other state TANF implementations
- [ ] All variables have proper `defined_for = StateCode.CT` or specific eligibility
- [ ] Documentation includes regulatory references

---

**Generated**: 2025-10-19  
**For**: Connecticut TANF Implementation  
**Based on**: Analysis of IL, TX, DC, MD, CA, CO, NY, NJ, NC TANF implementations
