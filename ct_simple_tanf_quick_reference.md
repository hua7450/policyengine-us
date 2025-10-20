# Connecticut Simple TANF - Quick Reference Guide

**For**: All agents implementing CT Simple TANF  
**Date**: 2025-10-20

## Variable Naming Pattern

```
ct_tanf_{component}
```

## Required Variables

### Core Variables
- `ct_tanf` - Main benefit amount (SPMUnit, float, MONTH)
- `ct_tanf_eligible` - Overall eligibility (SPMUnit, bool, MONTH)
- `ct_tanf_payment_standard` - Maximum benefit (SPMUnit, float, MONTH)
- `ct_tanf_countable_income` - Total countable income (SPMUnit, float, MONTH)

### Eligibility Variables
- `ct_tanf_income_eligible` - Income eligibility (SPMUnit, bool, MONTH)
- `ct_tanf_resources_eligible` - Resource eligibility (SPMUnit, bool, MONTH)

### Income Variables
- `ct_tanf_countable_earned_income` - Earned income after disregards (SPMUnit, float, MONTH)
- `ct_tanf_countable_unearned_income` - Unearned income after exclusions (SPMUnit, float, MONTH)
- `ct_tanf_earned_income_after_disregard` - Earned income post-disregard (SPMUnit, float, MONTH)

### Resource Variables
- `ct_tanf_countable_resources` - Total countable resources (SPMUnit, float, MONTH)

## Federal Variables to Use (DO NOT Recreate)

✅ **Use these federal variables directly:**
- `tanf_gross_earned_income` - Federal gross earned income
- `tanf_gross_unearned_income` - Federal gross unearned income
- `tanf_fpg` - Federal Poverty Guidelines
- `is_demographic_tanf_eligible` - Federal demographic eligibility
- `is_citizen_or_legal_immigrant` - Federal immigration status
- `is_tanf_enrolled` - TANF enrollment status

❌ **Do NOT create:**
- `ct_tanf_gross_earned_income`
- `ct_tanf_gross_unearned_income`
- `ct_tanf_fpg`
- `ct_tanf_demographic_eligible`

## Parameter Path Pattern

```
gov.states.ct.dss.tanf.{category}.{parameter}
```

### Common Parameters
```
gov.states.ct.dss.tanf.payment_standard
gov.states.ct.dss.tanf.income_limit.rate
gov.states.ct.dss.tanf.income.standards.initial_eligibility
gov.states.ct.dss.tanf.income.disregards.initial_disregard
gov.states.ct.dss.tanf.resources.limit
gov.states.ct.dss.tanf.benefit_reduction.rate
```

## Test File Naming

### Unit Tests
```
ct_tanf.yaml                              # Tests ct_tanf variable
ct_tanf_eligible.yaml                     # Tests ct_tanf_eligible variable
ct_tanf_countable_income.yaml             # Tests ct_tanf_countable_income variable
```

### Integration Test
```
integration.yaml                          # NOT ct_tanf_integration.yaml
```

## File Locations

### Variables
```
policyengine_us/variables/gov/states/ct/dss/tanf/
├── ct_tanf.py
├── ct_tanf_payment_standard.py
├── eligibility/
│   ├── ct_tanf_eligible.py
│   ├── ct_tanf_income_eligible.py
│   └── ct_tanf_resources_eligible.py
├── income/
│   ├── ct_tanf_countable_income.py
│   ├── ct_tanf_countable_earned_income.py
│   ├── ct_tanf_countable_unearned_income.py
│   └── ct_tanf_earned_income_after_disregard.py
└── resources/
    └── ct_tanf_countable_resources.py
```

### Parameters
```
policyengine_us/parameters/gov/states/ct/dss/tanf/
├── payment_standard.yaml
├── income_limit/
├── income/
│   ├── standards/
│   ├── disregards/
│   └── deductions/
├── resources/
└── benefit_reduction/
```

### Tests
```
policyengine_us/tests/policy/baseline/gov/states/ct/dss/tanf/
├── ct_tanf.yaml
├── ct_tanf_payment_standard.yaml
├── eligibility/
│   ├── ct_tanf_eligible.yaml
│   └── ct_tanf_income_eligible.yaml
├── income/
│   ├── ct_tanf_countable_unearned_income.yaml
│   └── ct_tanf_earned_income_after_disregard.yaml
└── integration.yaml
```

## Code Templates

### Main Benefit Variable
```python
from policyengine_us.model_api import *

class ct_tanf(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut Temporary Family Assistance (TFA/TANF)"
    unit = USD
    reference = "https://law.justia.com/codes/connecticut/..."
    defined_for = "ct_tanf_eligible"

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.ct.dss.tanf
        payment_standard = spm_unit("ct_tanf_payment_standard", period)
        countable_income = spm_unit("ct_tanf_countable_income", period)
        return max_(payment_standard - countable_income, 0)
```

### Eligibility Variable
```python
from policyengine_us.model_api import *

class ct_tanf_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA eligibility"
    reference = "https://law.justia.com/codes/connecticut/..."
    defined_for = StateCode.CT

    def formula(spm_unit, period, parameters):
        demographic_eligible = spm_unit("is_demographic_tanf_eligible", period)
        immigration_eligible = spm_unit.any(
            spm_unit.members("is_citizen_or_legal_immigrant", period)
        )
        income_eligible = spm_unit("ct_tanf_income_eligible", period)
        resources_eligible = spm_unit("ct_tanf_resources_eligible", period)
        
        return (
            demographic_eligible
            & immigration_eligible
            & income_eligible
            & resources_eligible
        )
```

### Income Variable Using Federal Baseline
```python
from policyengine_us.model_api import *

class ct_tanf_countable_earned_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA countable earned income"
    unit = USD
    reference = "https://law.justia.com/codes/connecticut/..."
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

### Adds Pattern for Combined Income
```python
from policyengine_us.model_api import *

class ct_tanf_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    label = "Connecticut TFA countable income"
    unit = USD
    reference = "https://law.justia.com/codes/connecticut/..."
    defined_for = StateCode.CT

    adds = [
        "ct_tanf_countable_earned_income",
        "ct_tanf_countable_unearned_income",
    ]
```

## Common Mistakes to Avoid

### ❌ Wrong Variable Names
```python
tanf_ct                    # State must come first
ct_tfa                     # Use tanf not tfa
connecticut_tanf           # Use 2-letter code
CT_TANF                    # Use lowercase
ctTanf                     # Use snake_case
ct_tanf_gross_earned_income  # Use federal variable instead
```

### ❌ Wrong Parameter Paths
```python
gov.states.ct.dhs.tanf     # Connecticut uses dss not dhs
gov.ct.tanf                # Missing states level
gov.states.connecticut.dss.tanf  # Use ct not connecticut
```

### ❌ Wrong Test Names
```python
ct_tanf_integration.yaml   # Use integration.yaml
test_ct_tanf.yaml          # Don't add test_ prefix
ct_tanf_test.yaml          # Don't add _test suffix
```

### ❌ Wrong Entity
```python
# Most CT TANF variables use SPMUnit, not Person
class ct_tanf(Variable):
    entity = Person  # WRONG - use SPMUnit
```

### ❌ Wrong Period
```python
# Connecticut TANF uses MONTH, not YEAR
class ct_tanf(Variable):
    definition_period = YEAR  # WRONG - use MONTH
```

## Checklist for New Variables

- [ ] Name follows `ct_tanf_{component}` pattern
- [ ] Entity is SPMUnit (unless person-level needed)
- [ ] definition_period is MONTH
- [ ] Includes `reference` URL to CT regulations
- [ ] Uses `defined_for = StateCode.CT` or `defined_for = "ct_tanf_eligible"`
- [ ] Uses federal baseline variables (don't recreate)
- [ ] Parameters use `gov.states.ct.dss.tanf.*` path
- [ ] Test file named correctly (variable name or `integration.yaml`)
- [ ] Imports use `from policyengine_us.model_api import *`

## Checklist for Parameters

- [ ] Path follows `gov.states.ct.dss.tanf.*` structure
- [ ] Includes description metadata
- [ ] Includes unit metadata
- [ ] Includes reference with title and href
- [ ] Uses proper breakdown for family size variations
- [ ] Includes effective dates
- [ ] Values use underscore thousands separators (1_000 not 1000)

## Checklist for Tests

- [ ] Unit test named after variable (`ct_tanf.yaml`)
- [ ] Integration test named `integration.yaml`
- [ ] Uses MONTH periods (2024-01 not 2024)
- [ ] Uses underscore thousands separators (1_000 not 1000)
- [ ] Includes descriptive test names
- [ ] Tests edge cases and boundaries
- [ ] Documents calculation steps in comments

## Quick Decision Tree

```
Need to create a variable?
├── Is it gross income? → Use federal tanf_gross_*_income
├── Is it demographic eligibility? → Use federal is_demographic_tanf_eligible
├── Is it FPG? → Use federal tanf_fpg
└── Is it CT-specific rule? → Create ct_tanf_* variable
    ├── Household-level? → Use SPMUnit entity
    └── Person-level? → Use Person entity (rare in simple TANF)
```

## Resources

- **Full Convention**: `ct_simple_tanf_naming_convention.md` (530 lines)
- **Analysis Summary**: `ct_simple_tanf_analysis_summary.md` (detailed analysis)
- **Existing Implementation**: ct-tanf-experiment branch
- **CLAUDE.md**: `/Users/ziminghua/vscode/policyengine-us/CLAUDE.md`

## Contact

For questions about naming conventions:
1. Read `ct_simple_tanf_naming_convention.md` first
2. Check existing CT TANF implementation in ct-tanf-experiment branch
3. Consult @naming-coordinator agent

---

**Last Updated**: 2025-10-20  
**Version**: 1.0  
**Status**: Experimental Implementation
