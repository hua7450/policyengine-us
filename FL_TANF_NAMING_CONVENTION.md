# Florida TANF Naming Convention

**Established**: 2025-10-22
**Purpose**: Ensure consistent variable and parameter naming across Florida TANF implementation

## Analysis Summary

After analyzing existing TANF implementations across multiple states (CO, IL, TX, DC, NY, CA), the following consistent patterns were identified:

### Pattern Structure
- **Format**: `{state_code}_{program}_{component}`
- **State Code**: Two-letter lowercase (e.g., `fl`, `co`, `il`, `tx`)
- **Program**: Lowercase acronym (e.g., `tanf`)
- **Component**: Descriptive snake_case (e.g., `countable_income`, `gross_earned_income`)

## Variable Naming Standards

### Primary Benefit Variable
- **Main benefit**: `fl_tanf`
  - Type: `float`
  - Entity: `SPMUnit`
  - Period: `MONTH`
  - Description: Final TANF benefit amount

### Eligibility Variables
- **Overall eligibility**: `fl_tanf_eligible`
  - Type: `bool`
  - Combines all eligibility criteria
  
- **Income eligibility**: `fl_tanf_income_eligible`
  - Type: `bool`
  - Tests both gross and net income limits
  
- **Resource eligibility**: `fl_tanf_resource_eligible`
  - Type: `bool`
  - Tests asset/resource limits
  
- **Categorical eligibility**: `fl_tanf_categorically_eligible`
  - Type: `bool`
  - Tests categorical requirements (age, family structure, etc.)

### Income Variables

#### Gross Income Variables
- **Gross earned income**: `fl_tanf_gross_earned_income`
  - Before any disregards or deductions
  
- **Gross unearned income**: `fl_tanf_gross_unearned_income`
  - Before any exclusions
  
- **Total gross income**: `fl_tanf_gross_income`
  - Sum of all gross income sources

#### Countable Income Variables
- **Countable earned income**: `fl_tanf_countable_earned_income`
  - After applying earned income disregards
  
- **Countable unearned income**: `fl_tanf_countable_unearned_income`
  - After applying unearned income exclusions
  
- **Total countable income**: `fl_tanf_countable_income`
  - Sum of all countable income (used in benefit calculation)

#### Income Deductions/Disregards
- **Earned income disregard**: `fl_tanf_earned_income_disregard`
  - Dollar amount or percentage excluded from earned income
  
- **Child support deduction**: `fl_tanf_child_support_deduction` (if applicable)
- **Childcare deduction**: `fl_tanf_childcare_deduction` (if applicable)
- **Dependent care deduction**: `fl_tanf_dependent_care_deduction` (if applicable)

### Benefit Calculation Variables
- **Payment standard**: `fl_tanf_payment_standard`
  - Maximum benefit before income offset
  
- **Need standard**: `fl_tanf_need_standard` (if different from payment standard)
  - Used for eligibility determination
  
- **Grant standard**: `fl_tanf_grant_standard` (if applicable)
  - Alternative term for payment/need standard
  
- **Base benefit**: `fl_tanf_base_benefit` (if needed)
  - Before adjustments or reductions

### Special Benefit Components (Florida-Specific)
- **Shelter tier**: `fl_tanf_shelter_tier`
  - Shelter cost category/tier
  
- **Family cap reduction**: `fl_tanf_family_cap_reduction`
  - Reduction amount for family cap policy

### Assistance Unit Variables (if needed)
- **Assistance unit size**: `fl_tanf_assistance_unit_size`
  - Number of people in the assistance unit
  
- **Eligible child**: `fl_tanf_eligible_child`
  - Type: `bool` (person-level)
  
- **Eligible parent**: `fl_tanf_eligible_parent`
  - Type: `bool` (person-level)

### Resource Variables
- **Countable resources**: `fl_tanf_countable_resources`
  - Total countable assets
  
- **Vehicle value**: `fl_tanf_vehicle_value` (if applicable)
  - Value of vehicles counted toward resource limit

## Parameter Naming Standards

### Parameter Path Structure
Base path: `gov.states.fl.dcf.tanf`

### Parameter Categories

#### Income Limits
- Path: `gov.states.fl.dcf.tanf.income_limits`
- Files:
  - `gross_income_limit.yaml` - Gross income test thresholds
  - `net_income_limit.yaml` - Net income test thresholds (if separate)

#### Payment Standards
- Path: `gov.states.fl.dcf.tanf.payment_standard`
- Files:
  - `base_amount.yaml` - Base payment amounts by family size
  - `shelter_tier.yaml` - Shelter tier amounts (if applicable)

#### Income Disregards
- Path: `gov.states.fl.dcf.tanf.income_disregards`
- Files:
  - `earned_income_flat.yaml` - Flat dollar disregard
  - `earned_income_percentage.yaml` - Percentage disregard
  - `work_expense.yaml` - Work-related expense disregards

#### Resource Limits
- Path: `gov.states.fl.dcf.tanf`
- Files:
  - `resource_limit.yaml` - Asset limits
  - `vehicle_limit.yaml` - Vehicle equity limits

#### Other Parameters
- `minimum_benefit.yaml` - Minimum benefit threshold
- `time_limit_months.yaml` - Time limit policies
- `family_cap.yaml` - Family cap policy parameters

## Directory Structure

### Variables
```
policyengine_us/variables/gov/states/fl/dcf/tanf/
├── fl_tanf.py                          # Main benefit variable
├── benefit/                            # Benefit calculation components
│   ├── fl_tanf_payment_standard.py
│   ├── fl_tanf_shelter_tier.py
│   └── fl_tanf_family_cap_reduction.py
├── eligibility/                        # Eligibility tests
│   ├── fl_tanf_eligible.py
│   ├── fl_tanf_income_eligible.py
│   ├── fl_tanf_resource_eligible.py
│   └── fl_tanf_categorically_eligible.py
└── income/                             # Income calculations
    ├── fl_tanf_gross_earned_income.py
    ├── fl_tanf_gross_unearned_income.py
    ├── fl_tanf_gross_income.py
    ├── fl_tanf_countable_earned_income.py
    ├── fl_tanf_countable_unearned_income.py
    ├── fl_tanf_countable_income.py
    └── fl_tanf_earned_income_disregard.py
```

### Parameters
```
policyengine_us/parameters/gov/states/fl/dcf/tanf/
├── income_limits/
│   └── gross_income_limit.yaml
├── income_disregards/
│   ├── earned_income_flat.yaml
│   └── earned_income_percentage.yaml
├── payment_standard/
│   ├── base_amount.yaml
│   └── shelter_tier.yaml
├── family_cap/
│   └── reduction.yaml
├── minimum_benefit.yaml
├── resource_limit.yaml
├── vehicle_limit.yaml
└── time_limit_months.yaml
```

### Tests
```
policyengine_us/tests/policy/baseline/gov/states/fl/dcf/tanf/
├── integration.yaml                    # Integration test (ALWAYS use this name)
├── fl_tanf.yaml                        # Unit test for main benefit
├── fl_tanf_eligible.yaml               # Unit test for eligibility
├── fl_tanf_income_eligible.yaml        # Unit test for income eligibility
├── fl_tanf_countable_income.yaml       # Unit test for countable income
└── [other unit tests matching variable names]
```

## Test File Naming Rules

### CRITICAL: Integration Test Naming
- **Integration test MUST be named**: `integration.yaml`
- **NOT**: `fl_tanf_integration.yaml`
- **NOT**: `integration_test.yaml`
- **NOT**: any other variation

### Unit Test Naming
- Unit tests should be named after the variable they test
- Format: `{variable_name}.yaml`
- Examples:
  - `fl_tanf.yaml` - Tests `fl_tanf` variable
  - `fl_tanf_eligible.yaml` - Tests `fl_tanf_eligible` variable
  - `fl_tanf_countable_income.yaml` - Tests `fl_tanf_countable_income` variable

## Common Naming Patterns from Other States

### Comparison with Similar Implementations

#### Colorado (co_tanf)
- Main: `co_tanf`
- Eligibility: `co_tanf_eligible`, `co_tanf_income_eligible`
- Income: `co_tanf_countable_earned_income_grant_standard`, `co_tanf_countable_gross_unearned_income`
- Benefit: `co_tanf_grant_standard`, `co_tanf_need_standard`

#### Illinois (il_tanf)
- Main: `il_tanf`
- Eligibility: `il_tanf_eligible`, `il_tanf_income_eligible`, `il_tanf_non_financial_eligible`
- Income: `il_tanf_gross_earned_income`, `il_tanf_countable_earned_income_for_grant_calculation`
- Benefit: `il_tanf_payment_level_for_grant_calculation`

#### Texas (tx_tanf)
- Main: `tx_tanf`, `tx_regular_tanf`, `tx_ottanf`
- Eligibility: `tx_tanf_eligible`, `tx_tanf_income_eligible`, `tx_tanf_resources_eligible`
- Income: `tx_tanf_gross_earned_income`, `tx_tanf_countable_earned_income`
- Benefit: `tx_tanf_payment_standard`

#### DC (dc_tanf)
- Main: `dc_tanf`
- Eligibility: `dc_tanf_eligible`, `dc_tanf_income_eligible`, `dc_tanf_resources_eligible`
- Income: `dc_tanf_gross_earned_income`, `dc_tanf_countable_earned_income`
- Benefit: `dc_tanf_standard_payment`

## What NOT to Do

### ❌ Avoid These Patterns
- **Don't use inconsistent prefixes**: 
  - ❌ `florida_tanf` (use state code, not full name)
  - ❌ `tanf_fl` (state code comes first)
  
- **Don't use verbose names**:
  - ❌ `fl_tanf_total_countable_income_for_benefit_calculation`
  - ✅ `fl_tanf_countable_income`
  
- **Don't use camelCase**:
  - ❌ `flTanfEligible`
  - ✅ `fl_tanf_eligible`
  
- **Don't use abbreviations inconsistently**:
  - ❌ `fl_tanf_cnt_inc` (use full words)
  - ✅ `fl_tanf_countable_income`
  
- **Don't create new patterns**:
  - Follow existing state patterns exactly
  - When in doubt, reference similar implementations

### ❌ Avoid These Test Naming Patterns
- ❌ `fl_tanf_integration.yaml` - Should be `integration.yaml`
- ❌ `test_fl_tanf.yaml` - Should be `fl_tanf.yaml`
- ❌ `FlTanf.yaml` - Should be `fl_tanf.yaml` (lowercase)

## Usage Examples

### Example 1: Basic Eligibility Check
```python
# Variable name: fl_tanf_eligible
class fl_tanf_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Florida TANF"
    definition_period = MONTH
    
    def formula(spm_unit, period, parameters):
        return (
            spm_unit("fl_tanf_income_eligible", period) &
            spm_unit("fl_tanf_resource_eligible", period) &
            spm_unit("fl_tanf_categorically_eligible", period)
        )
```

### Example 2: Income Calculation
```python
# Variable name: fl_tanf_countable_income
class fl_tanf_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "Florida TANF countable income"
    unit = USD
    definition_period = MONTH
    
    def formula(spm_unit, period, parameters):
        return add(
            spm_unit,
            period,
            [
                "fl_tanf_countable_earned_income",
                "fl_tanf_countable_unearned_income",
            ],
        )
```

### Example 3: Parameter Access
```python
def formula(spm_unit, period, parameters):
    p = parameters(period).gov.states.fl.dcf.tanf
    
    payment_standard = p.payment_standard.base_amount[family_size]
    income_limit = p.income_limits.gross_income_limit[family_size]
    earned_disregard_flat = p.income_disregards.earned_income_flat
    earned_disregard_pct = p.income_disregards.earned_income_percentage
```

## Consistency Check

Before implementing any new variable or parameter:

1. ✅ Does it follow the `fl_tanf_{component}` pattern?
2. ✅ Is it consistent with similar variables in other state TANF implementations?
3. ✅ Does the parameter path follow `gov.states.fl.dcf.tanf.{category}`?
4. ✅ Is the test file named correctly (unit test = variable name, integration = `integration.yaml`)?
5. ✅ Does it use snake_case throughout?
6. ✅ Is it descriptive without being overly verbose?

## References

This naming convention is based on analysis of existing implementations:
- Colorado TANF: `/policyengine_us/variables/gov/states/co/cdhs/tanf/`
- Illinois TANF: `/policyengine_us/variables/gov/states/il/dhs/tanf/`
- Texas TANF: `/policyengine_us/variables/gov/states/tx/tanf/`
- DC TANF: `/policyengine_us/variables/gov/states/dc/dhs/tanf/`
- New York TANF: `/policyengine_us/variables/gov/states/ny/otda/tanf/`
- California TANF: `/policyengine_us/variables/gov/states/ca/cdss/tanf/`

---

**Last Updated**: 2025-10-22
**Status**: Official naming standard for Florida TANF implementation

## Quick Reference Table

### Most Common Variables

| Purpose | Variable Name | Type | Entity |
|---------|---------------|------|--------|
| Main benefit | `fl_tanf` | float | SPMUnit |
| Overall eligibility | `fl_tanf_eligible` | bool | SPMUnit |
| Income eligibility | `fl_tanf_income_eligible` | bool | SPMUnit |
| Resource eligibility | `fl_tanf_resource_eligible` | bool | SPMUnit |
| Categorical eligibility | `fl_tanf_categorically_eligible` | bool | SPMUnit |
| Gross earned income | `fl_tanf_gross_earned_income` | float | SPMUnit |
| Gross unearned income | `fl_tanf_gross_unearned_income` | float | SPMUnit |
| Total gross income | `fl_tanf_gross_income` | float | SPMUnit |
| Countable earned income | `fl_tanf_countable_earned_income` | float | SPMUnit |
| Countable unearned income | `fl_tanf_countable_unearned_income` | float | SPMUnit |
| Total countable income | `fl_tanf_countable_income` | float | SPMUnit |
| Earned income disregard | `fl_tanf_earned_income_disregard` | float | SPMUnit |
| Payment standard | `fl_tanf_payment_standard` | float | SPMUnit |

### Florida-Specific Variables

| Purpose | Variable Name | Type | Entity |
|---------|---------------|------|--------|
| Shelter tier | `fl_tanf_shelter_tier` | Enum/int | SPMUnit |
| Family cap reduction | `fl_tanf_family_cap_reduction` | float | SPMUnit |

### Common Parameter Paths

| Parameter | Path |
|-----------|------|
| Gross income limit | `gov.states.fl.dcf.tanf.income_limits.gross_income_limit` |
| Payment standard base | `gov.states.fl.dcf.tanf.payment_standard.base_amount` |
| Shelter tier amounts | `gov.states.fl.dcf.tanf.payment_standard.shelter_tier` |
| Earned income flat disregard | `gov.states.fl.dcf.tanf.income_disregards.earned_income_flat` |
| Earned income % disregard | `gov.states.fl.dcf.tanf.income_disregards.earned_income_percentage` |
| Resource limit | `gov.states.fl.dcf.tanf.resource_limit` |
| Vehicle limit | `gov.states.fl.dcf.tanf.vehicle_limit` |
| Minimum benefit | `gov.states.fl.dcf.tanf.minimum_benefit` |

## Agent Reference Guide

### For @test-creator
- Unit test files: Named after the variable (e.g., `fl_tanf.yaml`, `fl_tanf_eligible.yaml`)
- Integration test: MUST be named `integration.yaml` (not `fl_tanf_integration.yaml`)

### For @rules-engineer
- All variables MUST use `fl_tanf_` prefix
- Follow the component naming structure from this document
- Reference similar variables in other states when uncertain

### For @parameter-architect
- Parameter base path: `gov.states.fl.dcf.tanf`
- Use subdirectories for categories: `income_limits/`, `income_disregards/`, `payment_standard/`
- Parameter file names should be descriptive and match variable references

### For @integration-agent
- Check that all variables follow the `fl_tanf_{component}` pattern
- Verify parameter paths use `gov.states.fl.dcf.tanf` base
- Ensure test files follow naming conventions (especially `integration.yaml`)

---

## Validation Checklist

Use this checklist to validate any new variable or parameter:

- [ ] Variable name starts with `fl_tanf_`
- [ ] Uses snake_case throughout
- [ ] Matches pattern from similar state implementations
- [ ] Not overly verbose (< 50 characters if possible)
- [ ] Parameter path starts with `gov.states.fl.dcf.tanf`
- [ ] Test file name matches variable name (or is `integration.yaml`)
- [ ] Descriptive but concise
- [ ] Documented in this file if it's a new pattern

