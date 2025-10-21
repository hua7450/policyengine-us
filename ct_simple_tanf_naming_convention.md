# Connecticut Simple TANF - Variable Naming Convention

**Program**: Connecticut Temporary Family Assistance (TFA/TANF) - Simplified Implementation  
**State**: Connecticut (CT)  
**Created**: 2025-10-20  
**Branch**: ct-tanf-experiment

## Purpose

This document establishes the variable naming conventions for Connecticut's simplified TANF implementation. These conventions are based on:
1. Existing CT TANF implementation in the ct-tanf-experiment branch
2. Analysis of similar state TANF programs (IL, TX, DC, MD, CA, CO, NY)
3. PolicyEngine US codebase standards

## Core Naming Pattern

**ALL VARIABLES MUST USE THIS EXACT PATTERN:**

```
ct_tanf_{component}
```

Where:
- `ct` = State code (Connecticut, lowercase)
- `tanf` = Program identifier (lowercase)
- `component` = Descriptive component name (snake_case)

### ✅ Correct Examples
- `ct_tanf` - Main benefit variable
- `ct_tanf_eligible` - Eligibility variable
- `ct_tanf_countable_income` - Income variable
- `ct_tanf_payment_standard` - Payment standard variable

### ❌ Incorrect Examples
- `tanf_ct` - State code must come first
- `ct_tfa` - Use `tanf` not `tfa` for consistency
- `connecticut_tanf` - Use 2-letter state code
- `CT_TANF` - Use lowercase only
- `ctTanf` - Use snake_case not camelCase

## Complete Variable Specification

### 1. Main Benefit Variable

| Variable Name | Entity | Type | Period | Description |
|--------------|--------|------|--------|-------------|
| `ct_tanf` | SPMUnit | float | MONTH | Connecticut TANF benefit amount |

**Implementation Pattern:**
```python
class ct_tanf(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut Temporary Family Assistance (TFA/TANF)"
    unit = USD
    defined_for = "ct_tanf_eligible"
```

### 2. Eligibility Variables

#### Primary Eligibility

| Variable Name | Entity | Type | Period | Description |
|--------------|--------|------|--------|-------------|
| `ct_tanf_eligible` | SPMUnit | bool | MONTH | Overall TANF eligibility |
| `ct_tanf_income_eligible` | SPMUnit | bool | MONTH | Meets income requirements |
| `ct_tanf_resources_eligible` | SPMUnit | bool | MONTH | Meets resource/asset requirements |

**Note**: For simplified TANF, use federal variables for demographic and immigration eligibility:
- `is_demographic_tanf_eligible` (federal)
- `is_citizen_or_legal_immigrant` (federal)

### 3. Income Variables

#### Earned Income

| Variable Name | Entity | Type | Period | Description |
|--------------|--------|------|--------|-------------|
| `ct_tanf_countable_earned_income` | SPMUnit | float | MONTH | Earned income after disregards |
| `ct_tanf_earned_income_after_disregard` | SPMUnit | float | MONTH | Earned income post-disregard calculation |

**Important**: For simplified TANF, use federal gross income baseline:
- Use `tanf_gross_earned_income` (federal) - DO NOT create `ct_tanf_gross_earned_income`

#### Unearned Income

| Variable Name | Entity | Type | Period | Description |
|--------------|--------|------|--------|-------------|
| `ct_tanf_countable_unearned_income` | SPMUnit | float | MONTH | Unearned income after exclusions |

**Important**: For simplified TANF, use federal gross income baseline:
- Use `tanf_gross_unearned_income` (federal) - DO NOT create `ct_tanf_gross_unearned_income`

#### Combined Income

| Variable Name | Entity | Type | Period | Description |
|--------------|--------|------|--------|-------------|
| `ct_tanf_countable_income` | SPMUnit | float | MONTH | Total countable income (earned + unearned) |

**Implementation Pattern:**
```python
class ct_tanf_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA countable income"
    unit = USD
    defined_for = StateCode.CT
    
    adds = [
        "ct_tanf_countable_earned_income",
        "ct_tanf_countable_unearned_income",
    ]
```

### 4. Benefit Calculation Variables

| Variable Name | Entity | Type | Period | Description |
|--------------|--------|------|--------|-------------|
| `ct_tanf_payment_standard` | SPMUnit | float | MONTH | Maximum benefit by family size |

### 5. Resource/Asset Variables

| Variable Name | Entity | Type | Period | Description |
|--------------|--------|------|--------|-------------|
| `ct_tanf_countable_resources` | SPMUnit | float | MONTH | Total countable resources/assets |

### 6. Federal Variables to Use (DO NOT recreate with ct_tanf prefix)

These federal baseline variables should be used directly:

| Variable Name | Purpose |
|--------------|---------|
| `tanf_gross_earned_income` | Federal baseline for gross earned income |
| `tanf_gross_unearned_income` | Federal baseline for gross unearned income |
| `tanf_fpg` | Federal Poverty Guideline for TANF |
| `is_demographic_tanf_eligible` | Federal demographic eligibility |
| `is_citizen_or_legal_immigrant` | Federal immigration eligibility |
| `is_tanf_enrolled` | Enrollment status (applicant vs recipient) |

## Parameter Naming Pattern

**ALL PARAMETERS MUST USE THIS PATH:**

```
gov.states.ct.dss.tanf.{category}.{parameter}
```

### Parameter Path Structure

```yaml
gov.states.ct.dss.tanf.
├── payment_standard                    # Maximum benefit amounts
├── income/
│   ├── standards/
│   │   ├── initial_eligibility        # Income limit for initial eligibility
│   │   ├── continuing_eligibility     # Income limit for continuing eligibility
│   │   ├── extended_eligibility_lower # Lower extended eligibility threshold
│   │   ├── extended_eligibility_upper # Upper extended eligibility threshold
│   │   └── extended_eligibility_reduction_threshold
│   ├── disregards/
│   │   └── initial_disregard          # Earned income disregard
│   ├── deductions/
│   │   └── child_support_passthrough  # Child support passthrough
│   └── standard_of_need/
│       └── rate                        # Standard of need rate
├── resources/
│   ├── limit                           # Resource limit
│   └── vehicle_exclusion               # Vehicle value exclusion
├── benefit_reduction/
│   ├── rate                            # Benefit reduction rate
│   └── threshold                       # Benefit reduction threshold
└── income_limit/
    └── rate                            # Maximum income limit rate
```

### Parameter Examples

```yaml
# Payment standard (breakdown by family size)
gov.states.ct.dss.tanf.payment_standard:
  1: 489
  2: 661
  3: 833

# Income limit (percentage of FPG)
gov.states.ct.dss.tanf.income_limit.rate: 2.30  # 230% FPG

# Benefit reduction rate
gov.states.ct.dss.tanf.benefit_reduction.rate: 0.20  # 20%
```

## Directory Structure

### Variable Files

```
policyengine_us/variables/gov/states/ct/dss/tanf/
├── ct_tanf.py                              # Main benefit
├── ct_tanf_payment_standard.py             # Payment standard
├── eligibility/
│   ├── ct_tanf_eligible.py                 # Overall eligibility
│   ├── ct_tanf_income_eligible.py          # Income eligibility
│   └── ct_tanf_resources_eligible.py       # Resource eligibility
├── income/
│   ├── ct_tanf_countable_income.py         # Total countable income
│   ├── ct_tanf_countable_earned_income.py  # Countable earned income
│   ├── ct_tanf_countable_unearned_income.py # Countable unearned income
│   └── ct_tanf_earned_income_after_disregard.py
└── resources/
    └── ct_tanf_countable_resources.py      # Countable resources
```

### Parameter Files

```
policyengine_us/parameters/gov/states/ct/dss/tanf/
├── payment_standard.yaml
├── income_limit/
│   └── rate.yaml
├── income/
│   ├── standards/
│   │   ├── initial_eligibility.yaml
│   │   ├── continuing_eligibility.yaml
│   │   ├── extended_eligibility_lower.yaml
│   │   ├── extended_eligibility_upper.yaml
│   │   └── extended_eligibility_reduction_threshold.yaml
│   ├── disregards/
│   │   └── initial_disregard.yaml
│   ├── deductions/
│   │   └── child_support_passthrough.yaml
│   └── standard_of_need/
│       └── rate.yaml
├── benefit_reduction/
│   ├── rate.yaml
│   └── threshold.yaml
└── resources/
    ├── limit.yaml
    └── vehicle_exclusion.yaml
```

### Test Files

```
policyengine_us/tests/policy/baseline/gov/states/ct/dss/tanf/
├── ct_tanf.yaml                            # Unit test for main benefit
├── ct_tanf_payment_standard.yaml           # Unit test for payment standard
├── eligibility/
│   ├── ct_tanf_eligible.yaml               # Unit test for eligibility
│   ├── ct_tanf_income_eligible.yaml        # Unit test for income eligibility
│   └── ct_tanf_resources_eligible.yaml     # Unit test for resource eligibility
├── income/
│   ├── ct_tanf_countable_unearned_income.yaml
│   └── ct_tanf_earned_income_after_disregard.yaml
└── integration.yaml                        # Integration test (NOT ct_tanf_integration.yaml)
```

## Test File Naming Rules

### ✅ CORRECT Test File Naming

**Unit Tests**: Name after the variable being tested
- `ct_tanf.yaml` - tests `ct_tanf` variable
- `ct_tanf_eligible.yaml` - tests `ct_tanf_eligible` variable
- `ct_tanf_countable_income.yaml` - tests `ct_tanf_countable_income` variable

**Integration Tests**: Always use `integration.yaml`
- `integration.yaml` - tests full program flow
- Place in module directory: `policyengine_us/tests/policy/baseline/gov/states/ct/dss/tanf/integration.yaml`

### ❌ INCORRECT Test File Naming

- `ct_tanf_integration.yaml` - Use `integration.yaml` instead
- `test_ct_tanf.yaml` - Don't add `test_` prefix
- `ct_tanf_test.yaml` - Don't add `_test` suffix

## Simple TANF Specific Considerations

### What Makes This "Simple TANF"?

1. **Uses Federal Income Baselines**
   - Uses `tanf_gross_earned_income` (federal)
   - Uses `tanf_gross_unearned_income` (federal)
   - Does NOT create state-specific gross income variables

2. **Uses Federal Demographic Rules**
   - Uses `is_demographic_tanf_eligible` (federal)
   - Does NOT create `ct_tanf_demographic_eligible`

3. **Uses Federal Immigration Rules**
   - Uses `is_citizen_or_legal_immigrant` (federal)
   - Does NOT create `ct_tanf_immigration_eligible`

4. **State-Specific Components Only**
   - Income disregards/deductions (if different from federal)
   - Payment standards (state-specific)
   - Resource limits (state-specific)
   - Eligibility thresholds (state-specific)

### Federal vs State Variables Decision Tree

```
Is this component...
├── Income source definition? → Use federal `tanf_gross_*_income`
├── Demographic eligibility? → Use federal `is_demographic_tanf_eligible`
├── Immigration eligibility? → Use federal `is_citizen_or_legal_immigrant`
├── Federal Poverty Guideline? → Use federal `tanf_fpg`
└── State-specific rule/limit? → Create `ct_tanf_*` variable
```

## Variable Implementation Checklist

When implementing a CT TANF variable:

- [ ] Variable name follows `ct_tanf_{component}` pattern
- [ ] Uses correct entity (SPMUnit for most variables)
- [ ] Uses MONTH for definition_period (unless different period needed)
- [ ] Includes proper `defined_for` (usually `StateCode.CT` or `ct_tanf_eligible`)
- [ ] Includes regulatory `reference` URL
- [ ] Uses federal baseline variables where appropriate
- [ ] Does NOT recreate federal variables with ct_ prefix
- [ ] Parameter references use `gov.states.ct.dss.tanf.*` path
- [ ] Test file named correctly (variable name or `integration.yaml`)

## Parameter Implementation Checklist

When creating a CT TANF parameter:

- [ ] Parameter path follows `gov.states.ct.dss.tanf.*` structure
- [ ] Includes metadata (description, unit, reference)
- [ ] Uses proper breakdown structure for family size variations
- [ ] Includes effective dates in YAML
- [ ] References authoritative sources (CT DSS, state regulations)
- [ ] Uses consistent naming with other state TANF parameters

## Common Mistakes to Avoid

### ❌ Creating Redundant Variables
```python
# WRONG - Don't create if federal variable exists
class ct_tanf_gross_earned_income(Variable):
    # This should use tanf_gross_earned_income instead
```

### ❌ Wrong State Code Order
```python
# WRONG - state must come first
class tanf_ct(Variable):
    
# CORRECT
class ct_tanf(Variable):
```

### ❌ Using Full State Name
```python
# WRONG
class connecticut_tanf(Variable):

# CORRECT
class ct_tanf(Variable):
```

### ❌ Wrong Agency Abbreviation
```yaml
# WRONG
gov.states.ct.dhs.tanf

# CORRECT
gov.states.ct.dss.tanf  # Connecticut uses DSS not DHS
```

### ❌ Wrong Test File Name
```yaml
# WRONG
ct_tanf_integration.yaml

# CORRECT
integration.yaml
```

## Code Examples

### Example 1: Main Benefit Variable

```python
from policyengine_us.model_api import *


class ct_tanf(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut Temporary Family Assistance (TFA/TANF)"
    unit = USD
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = "ct_tanf_eligible"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf
        
        payment_standard = spm_unit("ct_tanf_payment_standard", period)
        countable_income = spm_unit("ct_tanf_countable_income", period)
        
        # Basic benefit calculation
        standard_benefit = max_(payment_standard - countable_income, 0)
        
        # Extended eligibility benefit reduction (if applicable)
        total_gross_earnings = spm_unit("tanf_gross_earned_income", period)
        fpg = spm_unit("tanf_fpg", period)
        
        reduction_threshold = p.benefit_reduction.threshold * fpg
        upper_threshold = p.income_limit.rate * fpg
        
        in_reduction_tier = (
            (total_gross_earnings >= reduction_threshold) 
            & (total_gross_earnings <= upper_threshold)
        )
        
        reduction_rate = p.benefit_reduction.rate
        reduced_benefit = standard_benefit * (1 - reduction_rate)
        
        return where(in_reduction_tier, reduced_benefit, standard_benefit)
```

### Example 2: Eligibility Variable

```python
from policyengine_us.model_api import *


class ct_tanf_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA eligibility"
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-112/"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        # Use federal demographic eligibility
        demographic_eligible = spm_unit("is_demographic_tanf_eligible", period)
        
        # Use federal immigration eligibility
        immigration_eligible = spm_unit.any(
            spm_unit.members("is_citizen_or_legal_immigrant", period)
        )
        
        # State-specific tests
        income_eligible = spm_unit("ct_tanf_income_eligible", period)
        resources_eligible = spm_unit("ct_tanf_resources_eligible", period)
        
        return (
            demographic_eligible
            & immigration_eligible
            & income_eligible
            & resources_eligible
        )
```

### Example 3: Income Variable Using Federal Baseline

```python
from policyengine_us.model_api import *


class ct_tanf_countable_earned_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA countable earned income"
    unit = USD
    reference = "https://law.justia.com/codes/connecticut/title-17b/chapter-319s/"
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        # Use federal gross earned income baseline
        gross_earned = spm_unit("tanf_gross_earned_income", period)
        
        # Apply CT-specific disregard
        earned_after_disregard = spm_unit(
            "ct_tanf_earned_income_after_disregard", period
        )
        
        return earned_after_disregard
```

### Example 4: Parameter File

```yaml
description: Connecticut TANF payment standard (maximum benefit amount)
metadata:
  unit: currency-usd
  period: month
  reference:
    - title: Connecticut TANF Payment Standards
      href: https://portal.ct.gov/DSS/Economic-Security/TFA-Program
  breakdown:
    - household_size
values:
  2024-01-01:
    1: 489
    2: 661
    3: 833
    4: 1_002
    5: 1_122
    6: 1_256
    7: 1_388
    8: 1_520
```

## Summary

**Key Takeaways:**

1. **Pattern**: Always use `ct_tanf_{component}`
2. **Federal Baseline**: Use federal `tanf_gross_*_income` variables, don't recreate
3. **Simple = Minimal State-Specific**: Only create state variables for state-specific rules
4. **Agency**: Use `dss` (Department of Social Services) for Connecticut
5. **Test Files**: Unit tests named after variable, integration test named `integration.yaml`
6. **Entity**: Use SPMUnit for household-level calculations
7. **Period**: Use MONTH for Connecticut TANF
8. **Parameters**: Always use `gov.states.ct.dss.tanf.*` path structure

---

**Document Version**: 1.0  
**Last Updated**: 2025-10-20  
**Maintainer**: PolicyEngine US Development Team  
**Status**: Experimental Implementation
