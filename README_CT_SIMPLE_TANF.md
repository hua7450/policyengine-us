# Connecticut Simple TANF - Documentation Index

**Created**: 2025-10-20  
**Purpose**: Guide agents implementing Connecticut Simple TANF  
**Branch**: ct-tanf-experiment

## Documentation Files

This directory contains comprehensive naming convention documentation for Connecticut Simple TANF implementation:

### 1. Quick Reference Guide ⚡
**File**: `ct_simple_tanf_quick_reference.md` (7KB)

**Use this when you need:**
- Quick lookup of variable naming patterns
- Code templates for common variables
- Parameter path examples
- Test naming rules
- Common mistakes to avoid

**Best for**: Day-to-day implementation work

### 2. Complete Naming Convention 📘
**File**: `ct_simple_tanf_naming_convention.md` (17KB, 530 lines)

**Use this when you need:**
- Complete variable specification
- Detailed directory structure
- Full code examples with explanations
- Implementation checklists
- Decision trees for variable creation

**Best for**: Comprehensive reference, onboarding new agents

### 3. Analysis Summary 📊
**File**: `ct_simple_tanf_analysis_summary.md` (11KB)

**Use this when you need:**
- Background on naming decisions
- Comparison with other states
- Pattern validation data
- Git history analysis
- Rationale for conventions

**Best for**: Understanding why conventions were chosen

## Quick Start for Agents

### @rules-engineer
1. Read: `ct_simple_tanf_quick_reference.md`
2. Reference: Code templates section
3. Remember: Use federal `tanf_gross_*_income` variables, don't recreate

### @test-creator  
1. Read: Test naming section in quick reference
2. Remember: Unit tests = `{variable_name}.yaml`, Integration = `integration.yaml`
3. Use: MONTH periods (2024-01 not 2024)

### @parameter-architect
1. Read: Parameter path section in quick reference
2. Remember: `gov.states.ct.dss.tanf.*` path structure
3. Reference: Existing parameters in ct-tanf-experiment branch

### @integration-agent
1. Read: Complete naming convention document
2. Check: Variable naming consistency
3. Validate: Federal baseline usage (no recreated federal variables)

## Key Conventions

### Variable Naming
```
ct_tanf_{component}
```

**Examples:**
- `ct_tanf` - Main benefit
- `ct_tanf_eligible` - Eligibility
- `ct_tanf_countable_income` - Income

### Parameter Paths
```
gov.states.ct.dss.tanf.{category}.{parameter}
```

**Examples:**
- `gov.states.ct.dss.tanf.payment_standard`
- `gov.states.ct.dss.tanf.income.standards.initial_eligibility`
- `gov.states.ct.dss.tanf.resources.limit`

### Test Files
- **Unit Tests**: `{variable_name}.yaml` (e.g., `ct_tanf.yaml`)
- **Integration Test**: `integration.yaml` (NOT `ct_tanf_integration.yaml`)

## Federal Variables to Use

**DO NOT recreate these with ct_tanf prefix:**
- `tanf_gross_earned_income`
- `tanf_gross_unearned_income`
- `tanf_fpg`
- `is_demographic_tanf_eligible`
- `is_citizen_or_legal_immigrant`

## Common Patterns

### Main Benefit Variable
```python
class ct_tanf(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    defined_for = "ct_tanf_eligible"
```

### Eligibility Variable
```python
class ct_tanf_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = MONTH
    defined_for = StateCode.CT
```

### Income Variable
```python
class ct_tanf_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = MONTH
    defined_for = StateCode.CT
    
    adds = [
        "ct_tanf_countable_earned_income",
        "ct_tanf_countable_unearned_income",
    ]
```

## File Locations

### Variables
```
policyengine_us/variables/gov/states/ct/dss/tanf/
├── ct_tanf.py
├── eligibility/
├── income/
└── resources/
```

### Parameters
```
policyengine_us/parameters/gov/states/ct/dss/tanf/
├── payment_standard.yaml
├── income/
├── resources/
└── benefit_reduction/
```

### Tests
```
policyengine_us/tests/policy/baseline/gov/states/ct/dss/tanf/
├── ct_tanf.yaml
├── eligibility/
├── income/
└── integration.yaml
```

## Existing Implementation

The ct-tanf-experiment branch already has:
- ✅ 13 variables implemented
- ✅ 16 parameters defined
- ✅ 8 unit tests
- ✅ 1 integration test

**Review existing implementation for patterns:**
```bash
git checkout ct-tanf-experiment
ls policyengine_us/variables/gov/states/ct/dss/tanf/
```

## Validation Checklist

Before submitting implementation:

- [ ] All variables follow `ct_tanf_{component}` pattern
- [ ] No recreated federal variables (checked for `ct_tanf_gross_*`)
- [ ] Parameters use `gov.states.ct.dss.tanf.*` paths
- [ ] Test files named correctly
- [ ] Uses SPMUnit entity (unless person-level needed)
- [ ] Uses MONTH definition_period
- [ ] Includes regulatory references
- [ ] Code formatted with `make format`

## Additional Resources

- **Codebase Guide**: `/Users/ziminghua/vscode/policyengine-us/CLAUDE.md`
- **Existing CT TANF**: ct-tanf-experiment branch
- **Similar Implementations**: IL TANF, DC TANF, TX TANF

## Questions?

1. Check quick reference first
2. Review complete naming convention
3. Examine existing CT TANF implementation
4. Consult @naming-coordinator agent

---

**Documentation Status**: Complete  
**Last Updated**: 2025-10-20  
**Maintainer**: PolicyEngine US Development Team
