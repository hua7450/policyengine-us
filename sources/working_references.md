# Collected Documentation

## Washington State Income Tax (Millionaires Tax) - SB 6346-S Implementation
**Collected**: 2026-03-12
**Implementation Task**: Implement WA state income tax on high earners per Senate Bill 6346-S

---

## Official Program Name

**Federal Program**: N/A (state-level income tax; no federal counterpart)
**State's Official Name**: Washington Millionaires Tax / Income Tax on High Earners
**Bill Number**: Substitute Senate Bill 6346 (SSB 6346)
**Legislature**: 69th Legislature, 2026 Regular Session
**Source**: SSB 6346, to be codified as Title 82A RCW (Sec. 1003)

**Variable Prefix**: `wa_income_tax`

---

## Legislative Status

- **Senate passed**: February 16, 2026
- **House passed**: March 9, 2026 (51-46 vote, after 24+ hours of floor debate)
- **Senate concurred in House amendments**: March 11, 2026 (27-21 vote)
- **Current status**: On governor's desk; Governor Ferguson has pledged to sign
- **Expected to become law**: Yes

---

## Source Information

### Primary source
- **Title**: Substitute Senate Bill 6346 (SSB 6346)
- **Citation**: SSB 6346, 69th Legislature, 2026 Regular Session
- **URL**: https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf
- **Bill summary URL**: https://app.leg.wa.gov/billsummary/?BillNumber=6346&Year=2025&Initiative=false
- **To be codified as**: Title 82A RCW
- **Effective date**: January 1, 2028 (tax year 2028, first payments due 2029)

---

## Key Definitions (Sec. 101)

### Federal adjusted gross income (Sec. 101(3))
"adjusted gross income as determined under section 62 of the internal revenue code"

### Internal revenue code (Sec. 101(5))
"the United States internal revenue code of 1986, as amended and in effect on January 1, 2026, or such subsequent date as the department may provide by rule consistent with the purpose of this chapter"

### Washington base income (Sec. 101(11))
"federal adjusted gross income as modified under sections 302 through 306 and 401 through 407 of this act"

### Washington taxable income (Sec. 101(12))
"Washington base income as further modified by sections 307 through 310 of this act"

### Resident (Sec. 101(8))
An individual who:
- (a)(i) Is domiciled in this state during the taxable year, UNLESS the individual (A) maintained no permanent place of abode in this state during the entire taxable year, (B) maintained a permanent place of abode outside of this state during the entire taxable year, and (C) spent in the aggregate not more than 30 days of the taxable year in this state; OR
- (a)(ii) Is not domiciled in this state during the taxable year, but maintained a place of abode and was physically present in this state for more than 183 days during the taxable year.

---

## Tax Rate and Threshold (Sec. 201)

### Tax imposed (Sec. 201(1))
**Exact statutory language**: "Beginning January 1, 2028, a tax is imposed on the receipt of Washington taxable income. Only individuals are subject to payment of the tax, which equals 9.90 percent multiplied by an individual's Washington taxable income."

- **Tax rate**: 9.9% (flat rate)
- **Effective date**: January 1, 2028
- **Applies to**: Individuals only (not entities directly)

### Negative income (Sec. 201(2))
"If an individual's Washington taxable income is less than zero for a taxable year, no tax is due under this section and no amount is allowed as a carryover for use in the calculation of that individual's Washington taxable income, for any taxable year."

Exception: Loss carryforwards derived from or connected with Washington sources ARE included in Washington taxable income calculation.

---

## Standard Deduction - The $1,000,000 threshold (Sec. 310)

### One million dollar standard deduction (Sec. 310)
**Exact statutory language**: "In computing a taxpayer's Washington taxable income, a taxpayer may deduct from the taxpayer's Washington base income a standard deduction of $1,000,000 per individual, or in the case of spouses or domestic partners, their combined standard deduction is limited to $1,000,000, regardless of whether they file joint or separate returns."

- **Standard deduction**: $1,000,000
- **Per individual**: $1,000,000 (single filers)
- **Per married couple / domestic partners**: $1,000,000 COMBINED (NOT $1M each)
- **Indexed for inflation**: Yes, annually per Sec. 312

**CRITICAL for implementation**: The $1M threshold is implemented as a standard deduction from Washington base income, NOT as an income eligibility threshold. The tax applies to Washington taxable income (which is Washington base income MINUS the standard deduction and other adjustments).

### Filing status considerations (Sec. 703(4))
"individuals who are spouses or state registered domestic partners are not considered separate taxpayers for the purposes of this chapter regardless of whether they file a joint or separate return... The activities and assets of each spouse or state registered domestic partner are combined as if they were one individual for the purposes of determining the applicability of any threshold amounts, caps, deductions, credits, or any other amounts"

**Implementation note**: Married couples and domestic partners share a SINGLE $1,000,000 deduction regardless of filing status. This is a household-level (marital unit level) deduction, not a per-person deduction.

---

## Inflation adjustment (Sec. 312)

### Index for inflation (Sec. 312(1))
- **When**: Beginning October 2029 and each October thereafter
- **Method**: Multiply current standard deduction by (1 + CPI percentage change)
- **Rounding**: To nearest $1,000
- **Floor**: No downward adjustment (if CPI change would reduce the deduction, it stays the same)
- **CPI definition**: Consumer price index for all urban consumers, all items, for the Seattle area (Sec. 312(2)(a))
- **Takes effect**: For taxes due in the following calendar year

---

## Income calculation: Federal AGI to Washington taxable income

The bill defines a multi-step process to arrive at Washington taxable income:

### Step 1: Start with federal adjusted gross income (IRC Sec. 62)

### Step 2: Compute Washington base income (Secs. 302-306, 401-407)
Modifications to federal AGI:

**Sec. 302 - Long-term capital gains and losses:**
- SUBTRACT long-term capital gains included in federal AGI
- ADD BACK long-term capital losses included in federal AGI
- ADD Washington capital gains subject to tax under chapter 82.87 RCW (WA capital gains tax) plus amounts deducted under RCW 82.87.060(1) and (4) -- only for taxpayers owing WA capital gains tax

**Sec. 303 - State and local obligations:**
- ADD tax-exempt interest income excluded under IRC Sec. 103, EXCEPT interest on WA state or local obligations

**Sec. 304 - State/local income taxes and B&O taxes:**
- ADD state/local income taxes deducted on federal return
- ADD taxes for which B&O or public utility tax credit is allowed

**Sec. 305 - Carryovers:**
- ADD amounts carried over from taxable years before the effective date of the act

**Sec. 306 - Federal obligations:**
- SUBTRACT income from US obligations that states cannot tax (reduced by related expenses)

**Secs. 401-407 - Allocation and apportionment (for nonresidents/part-year residents):**
- Complex rules for allocating income to Washington sources
- Residents: entire Washington base income is taxable
- Nonresidents: only income derived from Washington sources

### Step 3: Compute Washington taxable income (Secs. 307-310)
Further modifications to Washington base income:

**Sec. 307 - Charitable contributions:**
- SUBTRACT charitable contributions claimed under IRC Sec. 170
- Maximum: $100,000 per individual, or $100,000 combined for spouses/domestic partners

**Sec. 308 - Pass-through entity tax payments:**
- ADD BACK distributive share of pass-through entity tax expense (Sec. 502) deducted on federal return

**Sec. 309 - Capital construction fund:**
- SUBTRACT amounts deposited in capital construction fund under IRC Sec. 7518

**Sec. 310 - Standard deduction:**
- SUBTRACT $1,000,000 standard deduction (see details above)

### Summary formula
```
Washington taxable income =
    Federal AGI
    - Long-term capital gains + Long-term capital losses
    + WA capital gains (if applicable)
    + Tax-exempt interest (except WA obligations)
    + State/local income taxes deducted federally
    + Pre-effective-date carryovers
    - Federal obligation income
    [allocation adjustments for nonresidents]
    - Charitable contributions (max $100K)
    + Pass-through entity tax add-back
    - Capital construction fund deposits
    - $1,000,000 standard deduction

Tax = max(0, Washington taxable income) * 9.9%
```

---

## Filing status rules (Sec. 703)

### Joint vs. separate returns (Sec. 703(1)-(2))
- If spouses file a joint federal return, they MUST file a joint WA return
- If spouses file separate federal returns, they MUST file separate WA returns
- State registered domestic partners MAY file jointly even if they filed separate federal returns

### Combined treatment (Sec. 703(4)(a))
Spouses and domestic partners are NOT considered separate taxpayers. Their "activities and assets... are combined as if they were one individual for the purposes of determining the applicability of any threshold amounts, caps, deductions, credits, or any other amounts."

### Separate return allocation (Sec. 703(4)(b))
When filing separately, spouses must allocate marital community assets and activity. If they cannot agree, each gets one-half.

---

## Credits

### Credit for income taxes paid to other jurisdictions (Sec. 203)
- Residents get credit for income taxes paid to other states
- Limited to the lesser of: (a) tax paid to other jurisdiction, or (b) WA tax * (income taxed in other jurisdiction / total WA base income)

### Credit for B&O and public utility taxes (Sec. 204)
- Beginning tax year 2028 (due 2029)
- Credit to avoid double-taxation of same income

---

## Pass-through entity tax election (Sec. 502)

- Rate: 9.9% of taxable income of electing entity
- Effective: January 1, 2028
- Election: Annual, irrevocable for taxable year, filed by April 15th
- Members get credit against individual tax for their share of entity-level tax paid

---

## Relationship to Initiative 2111 (Sec. 1001)

The bill amends RCW 1.90.100 (from Initiative Measure No. 2111, which prohibited state income taxes) to add an exemption:
"Subsection (1) of this section does not apply to the tax authorized in chapter 82A.--- RCW"

This explicitly carves out SSB 6346 from the income tax prohibition passed by voters.

---

## Null and void provision (Sec. 1002)

"If a court of final jurisdiction invalidates section 201 of this act, this act is null and void in its entirety."

---

## Implementation notes for PolicyEngine

### Simplified implementation approach

For PolicyEngine modeling purposes, the key variables needed are:

1. **`wa_income_tax`** - The final WA income tax amount
   - Formula: `max(0, wa_taxable_income) * 0.099`
   - Level: Tax unit

2. **`wa_taxable_income`** - Washington taxable income
   - For a simplified implementation: `federal_agi - wa_income_tax_standard_deduction`
   - For full implementation: Apply all Sec. 302-310 modifications
   - Level: Tax unit

3. **`wa_income_tax_standard_deduction`** - The $1M standard deduction
   - $1,000,000 per individual, $1,000,000 combined for married couples
   - Indexed for inflation starting October 2029 (for tax year 2030)
   - Level: Tax unit

### Parameters needed

```yaml
# Tax rate
gov.states.wa.tax.income.rate:
  values:
    2028-01-01: 0.099
  metadata:
    label: Washington income tax rate
    unit: /1
    reference:
      - title: SSB 6346 Sec. 201(1)
        href: https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf

# Standard deduction (individual)
gov.states.wa.tax.income.standard_deduction.individual:
  values:
    2028-01-01: 1_000_000
  metadata:
    label: Washington income tax standard deduction (individual)
    unit: currency-USD
    reference:
      - title: SSB 6346 Sec. 310
        href: https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf

# Standard deduction (joint / married / domestic partners)
gov.states.wa.tax.income.standard_deduction.joint:
  values:
    2028-01-01: 1_000_000
  metadata:
    label: Washington income tax standard deduction (joint)
    unit: currency-USD
    reference:
      - title: SSB 6346 Sec. 310
        href: https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf

# Charitable contribution deduction cap (individual)
gov.states.wa.tax.income.charitable_deduction.cap.individual:
  values:
    2028-01-01: 100_000
  metadata:
    label: Washington income tax charitable deduction cap (individual)
    unit: currency-USD
    reference:
      - title: SSB 6346 Sec. 307
        href: https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf

# Charitable contribution deduction cap (joint)
gov.states.wa.tax.income.charitable_deduction.cap.joint:
  values:
    2028-01-01: 100_000
  metadata:
    label: Washington income tax charitable deduction cap (joint)
    unit: currency-USD
    reference:
      - title: SSB 6346 Sec. 307
        href: https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf
```

### Key implementation considerations

1. **The $1M deduction is the SAME for individuals and married couples** - This is unusual. Most tax systems give married couples a higher threshold. Here, married couples share a single $1M deduction.

2. **Income definition is complex** - The full "Washington taxable income" requires multiple modifications to federal AGI. A simplified implementation could start with federal AGI minus the $1M deduction, with notes about the simplification.

3. **The tax only applies starting 2028** - No parameters should exist before 2028-01-01.

4. **Inflation indexing begins for tax year 2030** - The $1M amount is fixed for 2028 and 2029, then CPI-indexed starting with October 2029 adjustments for 2030.

5. **CPI index used**: Seattle-area CPI-U (all items, all urban consumers). This is a specific regional CPI, not the national CPI-U.

6. **Rounding**: Inflation-adjusted deduction rounded to nearest $1,000.

7. **Legal challenge expected** - The bill includes a "null and void" provision (Sec. 1002) if the tax imposition is invalidated by a court of final jurisdiction.

---

## References for metadata

```yaml
# For parameters:
reference:
  - title: "SSB 6346, Sec. 201 - Tax Imposed"
    href: "https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf"
  - title: "SB 6346 Bill Summary - Washington State Legislature"
    href: "https://app.leg.wa.gov/billsummary/?BillNumber=6346&Year=2025&Initiative=false"
```

```python
# For variables:
reference = "https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Senate%20Bills/6346-S.pdf"
```
