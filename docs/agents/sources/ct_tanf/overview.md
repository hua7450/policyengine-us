# Connecticut Temporary Family Assistance (TFA) - Program Overview

## Program Information

**Official Name**: Temporary Family Assistance (TFA)
**Federal Program**: Temporary Assistance for Needy Families (TANF)
**State**: Connecticut
**Administering Agency**: Connecticut Department of Social Services (DSS)
**State Plan Period**: Federal Fiscal Years 2024-2026 (October 1, 2023 - September 30, 2026)

## Legal Authorities

### Federal
- Social Security Act, Section 402 (TANF program requirements)
- 45 CFR Part 233 (TANF regulations)

### State
- Connecticut General Statutes Title 17b (Social Services)
  - Chapter 319s (Financial Assistance)
  - § 17b-112 (Temporary family assistance program)
  - § 17b-688c (Employment services for TANF recipients)
- Public Act 22-118 (2022) - Adjusted TFA benefits and tied to FPL

## Primary Sources

1. **Connecticut TANF State Plan 2024-2026**
   - URL: https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf
   - Initial Submission: December 31, 2023
   - Revision Date: April 15, 2024
   - Effective: October 1, 2023 through September 30, 2026

2. **Connecticut Department of Social Services - TFA Information**
   - URL: https://portal.ct.gov/dss/knowledge-base/articles/cash-assistance/temporary-family-assistance
   - Current program information and eligibility details

3. **Connecticut DSS Economic Security Portal**
   - URL: https://portal.ct.gov/dss/economic-security/economic-security---financial-assistance/eligibility
   - Program eligibility requirements

## Program Philosophy

Connecticut's Temporary Family Assistance (TFA) program is:
- **Employment-focused**: Based on assumption that cash assistance should be temporary
- **Time-limited**: Non-exempt families subject to time limits
- **Work-oriented**: Employment can help lift families out of poverty
- **Self-sufficiency driven**: Recipients encouraged to assume personal responsibility for economic independence

## TANF Purposes Addressed

Connecticut's TFA program addresses all four federal TANF purposes:

1. **Purpose 1**: Provide assistance to needy families so children may be cared for in their own homes or homes of relatives
2. **Purpose 2**: End dependence of needy parents on government benefits by promoting job preparation, work, and marriage
3. **Purpose 3**: Prevent and reduce incidence of out-of-wedlock pregnancies
4. **Purpose 4**: Encourage formation and maintenance of two-parent families

## Key Policy Changes

### Public Act 22-118 (Effective July 1, 2022)
- **Unified payment standards**: Eliminated regional variation (previously 3 regions)
- **Tied to FPL**: Benefits now calculated as percentage of Federal Poverty Level
- **Standard of Need**: Set at 55% of FPL
- **Payment calculation**: 73% of Standard of Need = effectively 40% of FPL
- **Automatic adjustments**: Benefits increase automatically as FPL updates

### 2024 Program Enhancements
- **April 1, 2024**: Jobs First time limit increased from 21 to 36 months
- **January 1, 2024**: Transitional benefits allowing earnings up to 230% FPL
- **Asset limit increase**: Raised to $6,000 (from previous lower amount)

## Program Structure

### Program Name: Jobs First Employment Services (JFES)
TFA is the cash assistance component of the Jobs First Employment Services program

**Components**:
- **Cash Assistance**: Monthly payment based on family size
- **Employment Services**: Job search, training, and work activities (administered by CT Department of Labor)
- **Child Care Assistance**: For unemployed persons preparing for employment
- **Transportation Benefits**: To support participation in work activities
- **Supportive Services**: Case management and barrier resolution

### Related Programs
- **Safety Net Services**: For families who exhaust time limits with income below 100% FPL
- **Child Care Assistance for Employed Persons**: Transitional support for working families (Office of Early Childhood)

## Two-Parent Families Special Treatment

**Note**: Two-parent TFA cases as defined at 45 CFR 261.24 are funded as Solely State Funded (SSF) program and are not part of federal TANF program. Other TFA families with two parents (not meeting this specific federal definition) continue to be part of TANF program.

## Documentation Organization

This documentation is organized into the following sections:

1. **eligibility.md**: Demographic and categorical eligibility criteria
2. **income_limits.md**: Income thresholds and tests for eligibility
3. **benefit_calculation.md**: Payment standards and benefit determination
4. **income_deductions.md**: Earned and unearned income disregards and exclusions
5. **time_limits.md**: Time limit rules and exemptions
6. **work_requirements.md**: Work participation requirements and sanctions
7. **resources.md**: Asset limits and excluded resources
8. **special_provisions.md**: Domestic violence, transitional benefits, and other special rules

## Quick Reference

| Element | Value/Rule |
|---------|-----------|
| Standard of Need | 55% of Federal Poverty Level |
| Payment Standard | See benefit_calculation.md (ranges from $489-$1,693) |
| Asset Limit | $6,000 |
| Vehicle Exclusion | Equity under $9,500 or used for disabled member |
| Jobs First Time Limit | 36 months (effective 4/1/2024) |
| Federal Time Limit | 60 months lifetime |
| Work Requirement | Yes (unless exempt) |
| Child Support Passthrough | $50/month excluded |

## Implementation Notes for PolicyEngine

**Federal Baseline Usage**:
- ✓ Demographic eligibility: Use federal age thresholds
- ✓ Immigration eligibility: Use federal qualified alien rules
- ✓ Income sources: Use standard earned/unearned definitions

**State-Specific Implementation Required**:
- Income limits (55% FPL Standard of Need)
- Benefit calculation (40% FPL formula)
- Income deductions ($90 applicant, 100% FPL recipient)
- Time limits (36-month state limit)
- Transitional benefits (230% FPL policy)
