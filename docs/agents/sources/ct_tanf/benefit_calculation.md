# Connecticut TFA - Benefit Calculation and Payment Standards

## Source
Connecticut TANF State Plan 2024-2026, Addendum A (Page 53) and Section A, Part I, A.1 (Pages 10-12)

## Payment Standards (Effective October 1, 2023)

### Uniform Statewide Standards

Pursuant to Public Act 22-118, Section 236, effective July 1, 2022, Connecticut established a **single statewide standard of need** and **uniform payment standards** for TFA based on household size, without regard to geographic region.

| Family Size | Payment Standard |
|-------------|------------------|
| 1 | $489 |
| 2 | $661 |
| 3 | $833 |
| 4 | $1,044 |
| 5 | $1,177 |
| 6 | $1,349 |
| 7 | $1,520 |
| 8 | $1,693 |

**Source**: TANF State Plan Addendum A, p. 53

## Calculation Methodology

### Formula Basis

Connecticut's payment standards are calculated using the following formula:

**Payment Standard = 73% × Standard of Need**

Where:
- **Standard of Need** = 55% of Federal Poverty Level (FPL) for household size

Therefore:
- **Effective percentage of FPL** = 0.73 × 0.55 = **0.4015** (approximately 40% of FPL)

**Source**: TANF State Plan p. 10, 12

### Why This Formula Matters

1. **Automatic Annual Adjustments**: Because payment standards are tied to FPL, they automatically increase each year when federal poverty guidelines are updated

2. **Transparent Calculation**: The formula ensures consistent, predictable benefit levels

3. **Legislative Intent**: Public Act 22-118 designed this system to ensure benefits keep pace with cost of living

### Historical Context

**Before July 1, 2022**:
- Payment standards varied across **three geographic regions**
- Regional variation based on average cost of rent in each area
- No automatic adjustment mechanism

**After July 1, 2022** (Public Act 22-118):
- **Uniform statewide** payment standard
- **Tied to FPL** for automatic adjustments
- **Simplified administration**

**Source**: TANF State Plan p. 12

## Benefit Reduction Scenarios

### Standard Benefit

For families with no countable income:
- Receive **full payment standard** for their family size

### Income-Based Reductions

**While income is below eligibility threshold**:
- Benefits are reduced by countable income
- Calculation: Payment Standard - Countable Income = Benefit Amount
- Minimum benefit: Program does not specify a minimum, so benefits can reduce to $0 before case closes

### Transitional Period Reduction (Effective January 1, 2024)

When family's total gross earnings are **between 171% and 230% of FPL**:
- Household's benefit reduced by **20%** for months with earnings in this range
- This reduction applies during the transitional 6-month period
- If earnings are between 100% and 171% FPL during transitional period: No reduction (full benefit if otherwise eligible)

**Source**: TANF State Plan p. 10

### Sanction-Related Reductions

**For non-compliance with work requirements**:

If only one family member is eligible for TFA and that member fails without good cause to comply with employment services requirement:
- **25% benefit reduction** in each month of non-compliance

If multiple family members are eligible:
- Noncompliant member's portion removed from benefit
- Other family members continue to receive their portion

**Source**: TANF State Plan p. 34 (Section A Part III)

## Payment Delivery Method

### Electronic Benefit Transfer (EBT)

Benefits are paid through:
1. **Electronic Benefit Transfer (EBT)** card, OR
2. **Direct deposit** to recipient's own bank account (Electronic Fund Transfer)

**Connecticut does NOT issue checks** for TFA cash assistance.

**Source**: TANF State Plan pp. 10, 13

### EBT Card Features

- Usable at all Point of Service (POS) devices (for cash back with purchase)
- Usable at all ATMs displaying the Quest logo
- **Two free cash withdrawals** per month at ATMs
- **Unlimited cash back** with purchase at POS locations allowing this
- After two free withdrawals: Normal bank fees + $0.50 EBT charge per transaction

**Source**: TANF State Plan p. 13

### Restricted Payment

The department may limit a person's control over their EBT account through:
- **Restricted payment**, OR
- **Direct payment to third party**

When authorized:
- Person has been determined to have mismanaged finances

**Source**: TANF State Plan p. 45 (Section B Part III)

## Calculation Examples

### Example 1: Family of 3 with No Income

**Family composition**: Parent + 2 children
**Countable income**: $0

**Calculation**:
- Payment Standard for family of 3: $833
- Countable Income: $0
- **Monthly benefit = $833**

### Example 2: Family of 3 with Earned Income (Recipient)

**Family composition**: Parent + 2 children
**Gross earned income**: $1,200/month
**FPL for family of 3** (2024): $2,072/month

**Calculation**:
- Payment Standard: $833
- Earned income up to 100% FPL ($2,072) is **excluded**
- Countable earned income: $0 (all excluded by 100% FPL disregard)
- **Monthly benefit = $833**

**Note**: Family remains eligible because gross earnings ($1,200) are below 100% FPL ($2,072)

### Example 3: Family of 3 in Transitional Period

**Family composition**: Parent + 2 children
**Gross earned income**: $3,700/month (179% of FPL)
**FPL for family of 3** (2024): $2,072/month
**Period**: Within first 6 months after earnings exceeded 100% FPL

**Calculation**:
- Earnings are between 171% and 230% of FPL
- Benefit reduction: 20%
- Base payment standard: $833
- Reduction amount: $833 × 0.20 = $166.60
- **Monthly benefit = $833 - $167 = $666**

### Example 4: Family of 1 Applying (New Applicant)

**Family composition**: Pregnant woman (counts as family of 1)
**Gross earned income**: $500/month
**FPL for family of 1** (2024): $1,215/month
**Standard of Need** (55% FPL): $668.25

**Calculation**:
- Earned income deduction at application: $90
- Adjusted earned income: $500 - $90 = $410
- Standard of Need (55% FPL): $668.25
- Income test: $410 < $668.25 ✓ (Eligible)
- Payment Standard: $489
- Countable income for benefit: $410 (after $90 deduction)
- **Monthly benefit = $489 - $410 = $79**

**Note**: Once enrolled, the 100% FPL earned income disregard would apply, increasing benefit to full $489.

## Special Payment Circumstances

### Extensions

When receiving a 6-month extension:
- Benefit calculated same as regular TFA
- Income eligibility threshold changes (see income_limits.md)
- Payment standard remains the same

### Safety Net Services

Families who exhaust Jobs First time limit may be eligible for:
- **Safety Net Services** (non-financial support services)
- **Basic needs payments** for rent, utilities, food, and essential household items
- Funded by **non-TANF** (Solely State Funded) sources

**Source**: TANF State Plan pp. 17-18 (Section C.3)

## Implementation Notes

### For PolicyEngine Parameters

**Payment standard parameter structure**:
```python
# Parameter file: ct_tanf_payment_standard.yaml
# This should be a scale parameter based on household size

description: Connecticut TFA payment standard by household size
values:
  2023-10-01:
    1: 489
    2: 661
    3: 833
    4: 1_044
    5: 1_177
    6: 1_349
    7: 1_520
    8: 1_693
unit: currency-USD
period: month
```

**Effective dates**:
- Current values: Effective October 1, 2023
- Update annually based on FPL adjustments
- Formula: Payment Standard = 0.73 × 0.55 × FPL = 0.4015 × FPL

### Calculation Logic

**Basic benefit calculation**:
```python
benefit = max(payment_standard - countable_income, 0)
```

**With transitional reduction** (if applicable):
```python
if transitional_period and (earnings_percent_fpl >= 171 and earnings_percent_fpl <= 230):
    benefit = payment_standard * 0.80  # 20% reduction
else:
    benefit = payment_standard - countable_income

benefit = max(benefit, 0)
```

### References for Metadata

```yaml
reference:
  - title: "Connecticut TANF State Plan 2024-2026, Addendum A - Temporary Family Assistance Payment Standards"
    href: "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
  - title: "Connecticut Public Act 22-118, Section 236 (2022)"
    href: "https://www.cga.ct.gov/2022/act/Pa/pdf/2022PA-00118-R00SB-00001-PA.PDF"
```
