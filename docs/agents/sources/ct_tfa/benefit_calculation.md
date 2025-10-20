# Connecticut TFA Benefit Calculation

## Payment Standards

### Geographic Variation

Connecticut has different benefit levels based on geographic location due to variations in housing costs across the state. The income limit differs by region because of the cost of housing differences.

**Confirmed Payment Amount:**
- Family of 3 with no income in highest-cost area: $833/month
- Family of 3 with no income in most populous region: $833/month

**References:**
- Connecticut General Statutes § 17b-112
- Connecticut TANF State Plan 2024-2026
- https://portal.ct.gov/dss/knowledge-base/articles/cash-assistance/temporary-family-assistance
- Connecticut DSS Uniform Policy Manual Section 6000 (Calculation of Benefits)

**Effective Date:** Current as of 2024

**Implementation Notes:**
- Complete payment standard tables by household size (1-8+) and geographic region are contained in the Connecticut TANF State Plan 2024-2026
- Payment standards appear to be fixed dollar amounts, not percentage-based formulas (e.g., not X% of FPG)
- The $833 amount for family of 3 is consistent across multiple official sources
- Geographic regions are defined by housing costs, with highest-cost and most populous regions having same benefit level

### Payment Standard Table Structure

**Required Data (Not Yet Extracted):**
- Payment amounts for household sizes 1-8+
- Definition of geographic regions (Region A, B, C, or similar)
- County or town assignments to each region
- Effective dates of current payment standards

**Source for Complete Table:**
Connecticut TANF State Plan 2024-2026, available at:
https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf

## Income Counting and Deductions

### Earned Income Treatment

#### For New Applicants

**$90 Earned Income Disregard:**
At the time of application, $90 is deducted from each person's gross earnings.

**Formula for Applicants:**
```
Countable Earned Income = (Person 1 Gross Earnings - $90) + (Person 2 Gross Earnings - $90) + ...
```

**References:**
- https://singlemotherguide.com/state/connecticut/TANF
- Connecticut DSS Uniform Policy Manual Section 5000 (Treatment of Income)

**Effective Date:** Current as of 2024

#### For Active Recipients

**100% FPL Earned Income Exclusion:**
Once enrolled in TFA, a household's earned income is entirely excluded up to 100% of the Federal Poverty Level for their household size.

**Formula for Recipients:**
```
Countable Earned Income = max(0, Total Gross Earned Income - 100% FPL Amount)
```

**Practical Example (2024 FPL):**
- Family of 3: 100% FPL = $25,820 annually ($2,152/month)
- If family earns $2,000/month: Countable earned income = $0
- If family earns $2,500/month: Countable earned income = $348

**References:**
- Connecticut General Statutes § 17b-112
- https://portal.ct.gov/dss/knowledge-base/articles/cash-assistance/temporary-family-assistance
- https://singlemotherguide.com/state/connecticut/TANF

**Effective Date:** Current as of 2024

**Implementation Notes:**
- This is an "all-or-nothing" exclusion up to 100% FPL threshold
- Different from traditional percentage disregards (e.g., $90 + 50% of remainder)
- Strongly encourages work up to full-time at minimum wage
- Creates work incentive without gradual benefit reduction until 100% FPL

### Unearned Income Treatment

**General Rule:**
Unearned income is counted dollar-for-dollar against the TFA benefit amount.

**Types of Unearned Income Counted:**
- Unemployment benefits
- Social Security benefits (RSDI, survivor benefits)
- Workers' compensation
- Pension income
- Interest and dividends
- Other unearned income

**Formula:**
```
Countable Unearned Income = Total Unearned Income - Excluded Amounts
```

**References:**
- https://singlemotherguide.com/state/connecticut/TANF
- Connecticut DSS Uniform Policy Manual Section 5000 (Treatment of Income)

**Effective Date:** Current as of 2024

### Income Exclusions

**Supplemental Security Income (SSI):**
SSI benefits are completely excluded and do not count toward TFA income eligibility or benefit calculation.

**Earned Income Tax Credit (EITC):**
The EITC (both federal and Connecticut state EITC) does not affect eligibility for TFA or other benefits such as cash assistance, Medicaid, SNAP, or subsidized housing.

**U.S. Census Bureau Employment:**
Earned income from temporary employment with the U.S. Census Bureau in support of decennial censuses (including positions as enumerators or post-enumeration surveyors) is excluded in TFA eligibility determinations.

**References:**
- Connecticut General Statutes § 17b-112
- https://singlemotherguide.com/state/connecticut/TANF
- https://uwc.211ct.org/earned-income-tax-credit-eiceitc-federal-earned-income-tax-credit-connecticut-earned-income-tax-credit/
- Connecticut DSS Uniform Policy Manual Section 5015 (Excluded Income)

**Effective Date:** Current as of 2024

**Implementation Notes:**
- UPM Section 5015 has separate subsections for different programs (AFDC/TFA, SNAP, etc.)
- Additional income exclusions may be detailed in UPM 5015
- Common exclusions often include: educational assistance, child support pass-through, certain irregular income

## Benefit Calculation Formula

### Standard Benefit Calculation (No Extended Eligibility)

**For New Applicants:**
```
1. Calculate Countable Earned Income:
   Countable Earned Income = sum of (each earner's gross earnings - $90)

2. Calculate Countable Unearned Income:
   Countable Unearned Income = Total Unearned Income - Exclusions

3. Calculate Total Countable Income:
   Total Countable Income = Countable Earned Income + Countable Unearned Income

4. Determine Payment Standard:
   Payment Standard = Amount for household size and geographic region

5. Calculate Monthly Benefit:
   Monthly Benefit = max(0, Payment Standard - Total Countable Income)
```

**For Active Recipients:**
```
1. Calculate Countable Earned Income:
   Countable Earned Income = max(0, Total Gross Earned Income - 100% FPL Amount)

2. Calculate Countable Unearned Income:
   Countable Unearned Income = Total Unearned Income - Exclusions

3. Calculate Total Countable Income:
   Total Countable Income = Countable Earned Income + Countable Unearned Income

4. Determine Payment Standard:
   Payment Standard = Amount for household size and geographic region

5. Calculate Monthly Benefit:
   Monthly Benefit = max(0, Payment Standard - Total Countable Income)
```

**References:**
- Connecticut General Statutes § 17b-112
- Connecticut DSS Uniform Policy Manual Section 6000 (Calculation of Benefits)
- https://portal.ct.gov/dss/lists/uniform-policy-manual/upm6---calculation-of-benefits-benefit-issuance

**Effective Date:** Current as of 2024

### Extended Eligibility Benefit Calculation (Effective April 1, 2024)

**Applicability:**
When a family's total gross earnings exceed 100% FPL, for a period not to exceed 6 consecutive months.

**Step 1: Determine Eligibility Tier**
```
If Total Gross Earnings < 100% FPL:
    → Not in extended eligibility (use standard calculation)
Else if Total Gross Earnings < 171% FPL:
    → Tier 1 Extended Eligibility (full benefit, no reduction)
Else if Total Gross Earnings < 230% FPL:
    → Tier 2 Extended Eligibility (20% benefit reduction)
Else:
    → Ineligible for TFA
```

**Step 2: Calculate Base Benefit**
```
For Tier 1 (100-171% FPL):
    Monthly Benefit = Standard Payment Amount (no income counting)

For Tier 2 (171-230% FPL):
    Base Benefit = Standard Payment Amount
    Monthly Benefit = Base Benefit × 0.80 (20% reduction)
```

**Duration:**
Up to 6 consecutive months maximum.

**References:**
- Connecticut General Statutes § 17b-112 (as amended, effective April 1, 2024)
- https://portal.ct.gov/dss/knowledge-base/articles/cash-assistance/temporary-family-assistance
- https://singlemotherguide.com/state/connecticut/TANF

**Effective Date:** April 1, 2024

**Implementation Notes:**
- This is a NEW policy as of April 1, 2024
- The 20% reduction applies to the benefit amount, not to income
- Extended eligibility is available once per TFA episode
- Designed to prevent cliff effects and support families transitioning to work
- Families must have had income less than 100% FPL to qualify for extension

## Calculation Examples

### Example 1: New Applicant with Earned Income

**Household:**
- Single parent with 2 children (family of 3)
- Highest-cost region
- Parent earns $1,200/month gross
- No unearned income

**Calculation:**
```
1. Countable Earned Income = $1,200 - $90 = $1,110
2. Countable Unearned Income = $0
3. Total Countable Income = $1,110
4. Payment Standard = $833 (family of 3, highest-cost region)
5. Monthly Benefit = $833 - $1,110 = $0 (not eligible)
```

**Eligibility Check:**
- 55% FPL for family of 3 (2024) = $25,820 × 0.55 = $14,201/year = $1,183/month
- Gross earnings ($1,200) > 55% FPL ($1,183)
- **Result: Not eligible** (income exceeds Standard of Need)

### Example 2: Active Recipient with Earned Income

**Household:**
- Single parent with 2 children (family of 3)
- Highest-cost region
- Parent earns $2,000/month gross
- No unearned income

**Calculation:**
```
1. 100% FPL for family of 3 (2024) = $25,820/year = $2,152/month
2. Countable Earned Income = max(0, $2,000 - $2,152) = $0
3. Countable Unearned Income = $0
4. Total Countable Income = $0
5. Payment Standard = $833
6. Monthly Benefit = $833 - $0 = $833
```

**Result:** Family receives full TFA benefit of $833/month while earning $2,000/month.

**Total Monthly Income:** $833 (TFA) + $2,000 (earnings) = $2,833

### Example 3: Active Recipient with Earnings Above 100% FPL

**Household:**
- Single parent with 2 children (family of 3)
- Highest-cost region
- Parent earns $2,500/month gross
- No unearned income

**Calculation:**
```
1. 100% FPL for family of 3 (2024) = $2,152/month
2. Countable Earned Income = $2,500 - $2,152 = $348
3. Countable Unearned Income = $0
4. Total Countable Income = $348
5. Payment Standard = $833
6. Monthly Benefit = $833 - $348 = $485
```

**Result:** Family receives reduced TFA benefit of $485/month.

**Total Monthly Income:** $485 (TFA) + $2,500 (earnings) = $2,985

### Example 4: Extended Eligibility - Tier 1 (100-171% FPL)

**Household:**
- Single parent with 2 children (family of 3)
- Highest-cost region
- Parent earns $3,000/month gross (139% FPL)
- No unearned income
- In extended eligibility period

**Calculation:**
```
1. 100% FPL = $2,152/month; 171% FPL = $3,680/month
2. Earnings ($3,000) are between 100% and 171% FPL → Tier 1
3. Monthly Benefit = $833 (full payment standard, no reduction)
```

**Result:** Family receives full TFA benefit of $833/month.

**Total Monthly Income:** $833 (TFA) + $3,000 (earnings) = $3,833

**Duration:** Up to 6 consecutive months

### Example 5: Extended Eligibility - Tier 2 (171-230% FPL)

**Household:**
- Single parent with 2 children (family of 3)
- Highest-cost region
- Parent earns $4,000/month gross (186% FPL)
- No unearned income
- In extended eligibility period

**Calculation:**
```
1. 171% FPL = $3,680/month; 230% FPL = $4,950/month
2. Earnings ($4,000) are between 171% and 230% FPL → Tier 2
3. Base Benefit = $833
4. Monthly Benefit = $833 × 0.80 = $666.40 (20% reduction)
```

**Result:** Family receives reduced TFA benefit of $666.40/month.

**Total Monthly Income:** $666.40 (TFA) + $4,000 (earnings) = $4,666.40

**Duration:** Up to 6 consecutive months

### Example 6: Family with Unearned Income

**Household:**
- Single parent with 2 children (family of 3)
- Highest-cost region
- Parent earns $1,500/month gross
- Parent receives $500/month unemployment benefits

**Calculation (as active recipient):**
```
1. 100% FPL for family of 3 = $2,152/month
2. Countable Earned Income = max(0, $1,500 - $2,152) = $0
3. Countable Unearned Income = $500 (unemployment counted dollar-for-dollar)
4. Total Countable Income = $0 + $500 = $500
5. Payment Standard = $833
6. Monthly Benefit = $833 - $500 = $333
```

**Result:** Family receives TFA benefit of $333/month.

**Total Monthly Income:** $333 (TFA) + $1,500 (earnings) + $500 (unemployment) = $2,333

## Special Considerations

### Stepparent Income

When a stepparent lives in the household, their income may be considered in the TFA eligibility and benefit calculation under certain circumstances.

**References:**
- Connecticut General Statutes § 17b-180 (Consideration of stepparent's income)
- https://law.justia.com/codes/connecticut/title-17b/chapter-319s/

**Implementation Notes:**
- Specific rules for stepparent income deeming are in CGS § 17b-180
- This is separate from standard earned/unearned income counting
- May involve deemed income calculations similar to SSI methodology

### Child Support

**Treatment:**
Child support received by custodial parents is generally counted as unearned income, though there may be partial disregards or pass-through provisions.

**Collection Requirement:**
Custodial parents receiving TFA must cooperate with child support enforcement to collect support from non-custodial parents.

**References:**
- Connecticut General Statutes § 17b-179 (Child Support Enforcement)
- https://www.cga.ct.gov/PS99/rpt/olr/htm/99-R-0187.htm

### Prorating for Partial Months

**General Rule:**
A month counts toward time limits if the family receives assistance for any day of the month.

**Benefit Amount:**
Benefits may be prorated based on the number of days in the month that the family is eligible.

**References:**
- Connecticut General Statutes § 17b-112
- Connecticut DSS Uniform Policy Manual Section 6000

## Benefit Issuance

**Payment Method:**
TFA benefits are typically issued via Electronic Benefit Transfer (EBT) card.

**Payment Schedule:**
Benefits are issued monthly, typically at the beginning of the month for the upcoming month.

**References:**
- Connecticut DSS Uniform Policy Manual Section 6000 (Benefit Issuance)

**Effective Date:** Current as of 2024

## Updates and Adjustments

### Cost-of-Living Adjustments

Connecticut law provides for cost-of-living adjustments to TFA benefits, though the frequency and methodology are determined by state appropriations and policy decisions.

**References:**
- Connecticut General Statutes § 17b-112

### Federal Poverty Level Updates

The Federal Poverty Level is updated annually by the federal Department of Health and Human Services (HHS), typically in January.

**Impact on Connecticut TFA:**
- Standard of Need (55% FPL) adjusts automatically with FPL updates
- 100% FPL earned income exclusion adjusts automatically
- Extended eligibility thresholds (171% FPL, 230% FPL) adjust automatically

**Implementation Notes:**
- FPL updates must be implemented promptly to maintain accurate eligibility determinations
- Payment standards are separate from FPL and may not adjust automatically

## Outstanding Research Needs

1. **Complete Payment Standard Table:**
   - Need full table of benefit amounts for household sizes 1-8+ and all geographic regions
   - Need definition of geographic regions and county/town assignments
   - Source: Connecticut TANF State Plan 2024-2026 (requires PDF extraction)

2. **UPM Section 6030 Details:**
   - Specific calculation procedures from Uniform Policy Manual
   - Source: https://portal.ct.gov/dss/lists/uniform-policy-manual

3. **Child Support Treatment:**
   - Exact disregards or pass-through amounts for child support
   - Source: UPM Section 5015 (Excluded Income) and CGS § 17b-179

4. **Stepparent Income Deeming:**
   - Detailed methodology from CGS § 17b-180
   - Source: https://law.justia.com/codes/connecticut/title-17b/chapter-319s/section-17b-180/

5. **Historical Payment Standards:**
   - When were current payment standards established?
   - What is the adjustment methodology?
   - Source: Connecticut TANF State Plan historical versions
