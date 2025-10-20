# Connecticut TFA - Income Deductions and Exclusions

## Source
Connecticut TANF State Plan 2024-2026, Section A, Part I, A.1 (Pages 10-12) and Section B, Part III (Pages 44-45)

## Earned Income Deductions

### For Applicants (Initial Eligibility)

**$90 Per Person Deduction**:
- **$90 is deducted** from each person's gross earnings at the time of application
- Applied to determine eligibility against 55% FPL Standard of Need
- This is a **flat dollar amount**, not a percentage

**Example**:
- Family of 3 with one working parent earning $700/month
- Deduction: $90 (per person who has earnings, not per family member)
- Adjusted earnings: $700 - $90 = $610
- This $610 is compared to Standard of Need (55% FPL)

**Source**: TANF State Plan pp. 10, 44-45

**Important Notes**:
- Only applies to earnings (not unearned income)
- Only applies during application/initial eligibility determination
- Each person with earnings gets the $90 deduction

### For Recipients (Continuing Eligibility)

**100% FPL Earned Income Disregard**:
- Once enrolled, a household's earned income is **excluded up to 100% FPL**
- This means all earned income up to the poverty level for family size is not counted

**Example** (2024 FPL):
- Family of 3: 100% FPL = $2,072/month
- If family earns $1,500/month: **$1,500 excluded** (counted as $0)
- If family earns $2,500/month: **$2,072 excluded** (counted as $428)

**Eligibility Impact Through December 31, 2023**:
- Once earnings reach 100% FPL, family becomes **ineligible** for assistance
- No grace period or transitional benefits

**Source**: TANF State Plan p. 10

### Transitional Earnings Disregard (Effective January 1, 2024)

**Extended Eligibility Period**:
In the first month in which a family's total gross earnings exceed 100% of FPL, and for a period **not to exceed six consecutive months**:

**Earnings up to 100% FPL**:
- Family continues to receive full benefit (if no other income)
- No reduction applied

**Earnings between 100% and 171% FPL**:
- Earnings disregarded for eligibility purposes (up to 230% FPL)
- Family continues to receive full benefit
- No reduction applied

**Earnings between 171% and 230% FPL**:
- Earnings disregarded for eligibility purposes (family remains eligible)
- **20% benefit reduction** applied
- Reduction calculation: Payment Standard × 0.20

**Earnings exceeding 230% FPL**:
- Family becomes **ineligible** for assistance
- Transitional period ends

**Source**: TANF State Plan p. 10

**Timeline Example**:
1. Month 1: Earnings jump to $2,300 (111% FPL for family of 3)
   - Still eligible, no benefit reduction
2. Months 2-6: Earnings continue at $2,300-$3,500 (111-169% FPL)
   - Still eligible, no benefit reduction (if under 171% FPL)
3. Months 2-6: Earnings at $3,700 (179% FPL)
   - Still eligible, 20% benefit reduction applied
4. Month 7: Earnings at $4,000 (193% FPL)
   - If 6 months elapsed: Ineligible (reverts to 100% FPL limit)
   - If within 6 months: Still eligible, 20% benefit reduction
5. Any month: Earnings at $5,000 (241% FPL)
   - Ineligible (exceeds 230% FPL threshold)

## Unearned Income Exclusions

### Child Support Passthrough and Exclusion

**$50 Monthly Exclusion**:
- Up to **$50 per month** of current child support is passed through to the family
- This $50 is **excluded as income** (not counted toward eligibility or benefit)
- Only applies to **current** child support (not arrears)

**Example**:
- Family receives $150/month in child support
- $50 is excluded (passed through to family)
- Remaining $100 is counted as unearned income

**Source**: TANF State Plan p. 10

**Note**: The State Plan states "up to $50 per month" but does not specify if this is per child or per family. Based on standard TANF policy, this is typically **per family per month**, not per child.

### U.S. Census Bureau Earnings

**Complete Exclusion**:
Earned income from **temporary employment with the U.S. Census Bureau** in support of decennial censuses is completely excluded from TFA eligibility determinations.

**Positions included**:
- Enumerators
- Post-enumeration surveyors
- Other temporary Census positions

**Important**: This exclusion only applies to:
- **Decennial census** work (every 10 years)
- **Temporary** employment
- Does NOT apply to permanent Census Bureau employment

**Source**: TANF State Plan pp. 10, 45

### Standard Unearned Income Treatment

**General Rule**:
- Unearned income must be **less than the department's Standard of Need** for family to be eligible
- Standard of Need = 55% of FPL for family size
- No general disregard or exclusion for unearned income (except child support passthrough)

**Types of unearned income** (not explicitly listed but implied):
- Unemployment compensation
- Social Security benefits (not SSI)
- Pension/retirement income
- Interest and dividends
- Other non-work income

**Source**: TANF State Plan p. 45

## Income Verification Standards

### Verification Methods

**Primary sources**:
- Documents are the primary sources of verification
- Examples: Pay stubs, benefit award letters, bank statements

**Secondary sources**:
- Affidavits are accepted when other sources of verification are not available
- Affidavits must be signed statements attesting to income/circumstances

**Standard of proof**:
- **Preponderance of evidence** is the department's standard of verification
- This means "more likely than not" based on available evidence

**Source**: TANF State Plan p. 44

## Interaction with Other Benefits

### Child Care and Transportation

**Not counted as income**:
- Child care assistance provided to support employment activities
- Transportation benefits provided to support employment activities
- These are **supportive services**, not income

**Source**: TANF State Plan pp. 10, 26

## Special Income Treatment

### Restricted Payment Situations

When family demonstrates financial mismanagement:
- Department may pay benefits directly to third parties (e.g., landlord, utilities)
- This does not change income calculation
- Benefits still count as income to family for other purposes

**Source**: TANF State Plan p. 45

## Implementation Notes

### For PolicyEngine

**Earned income deduction for applicants**:
```python
# Simple implementation
earned_income_after_deduction = max(total_earned_income - (90 * number_of_earners), 0)

# Compare to Standard of Need (55% FPL)
eligible = earned_income_after_deduction < (household_size_fpl * 0.55)
```

**Earned income disregard for recipients**:
```python
# Recipients: 100% FPL disregard
fpl_100 = household_size_fpl
countable_earned_income = max(total_earned_income - fpl_100, 0)
```

**Transitional period logic** (effective 1/1/2024):
```python
if transitional_period_active and months_in_transition <= 6:
    # Eligible if earnings under 230% FPL
    if total_earned_income <= (household_size_fpl * 2.30):
        eligible = True

        # Calculate benefit reduction
        earnings_percent_fpl = (total_earned_income / household_size_fpl) * 100

        if earnings_percent_fpl >= 171 and earnings_percent_fpl <= 230:
            benefit = payment_standard * 0.80  # 20% reduction
        else:
            benefit = payment_standard  # No reduction if under 171% FPL
    else:
        eligible = False
else:
    # Standard 100% FPL limit
    eligible = total_earned_income <= household_size_fpl
```

**Child support exclusion**:
```python
# Exclude up to $50/month
excluded_child_support = min(child_support_received, 50)
countable_child_support = max(child_support_received - 50, 0)
```

### Variables to Create

1. `ct_tanf_earned_income_deduction_applicant` - $90 per earner
2. `ct_tanf_earned_income_disregard_recipient` - 100% FPL amount
3. `ct_tanf_transitional_earnings_limit` - 230% FPL
4. `ct_tanf_transitional_reduction_threshold` - 171% FPL
5. `ct_tanf_child_support_exclusion` - $50/month
6. `ct_tanf_countable_earned_income`
7. `ct_tanf_countable_unearned_income`

### References for Metadata

```yaml
reference:
  - title: "Connecticut TANF State Plan 2024-2026, Section A, Part I, A.1"
    href: "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
  - title: "Connecticut TANF State Plan 2024-2026, Section B, Part III - Objective Criteria"
    href: "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
```

## Key Takeaways

1. **Applicants get $90 deduction** per earner, recipients get 100% FPL disregard
2. **Major policy change January 1, 2024**: Transitional benefits allow earnings up to 230% FPL
3. **Child support**: $50/month excluded from income
4. **Census work**: Completely excluded from income
5. **No general unearned income disregard** except child support passthrough
6. **Transitional benefits are time-limited**: Maximum 6 consecutive months
