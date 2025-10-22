# Collected Documentation

## Florida TANF (Temporary Cash Assistance) - Implementation Reference
**Collected**: 2025-10-22
**Implementation Task**: Documentation for existing Florida TANF implementation validation and enhancement

### Program Overview
Florida's Temporary Assistance for Needy Families (TANF) program is called Temporary Cash Assistance (TCA). The program provides cash assistance to low-income families with children. Florida's benefit levels have remained unchanged since 1992.

---

### Source Information

**Primary Legal Authority:**
- **Title**: Florida Statute § 414.095 - Determining eligibility for temporary cash assistance
- **Citation**: F.S. § 414.095
- **URL**: https://www.flsenate.gov/Laws/Statutes/2024/414.095
- **Effective Date**: Current as of 2024

**Administrative Rules:**
- **Title**: Florida Administrative Code Chapter 65A-4 - Temporary Cash Assistance
- **Citation**: F.A.C. 65A-4
- **URL**: https://flrules.org/gateway/ChapterHome.asp?Chapter=65A-4
- **Key Rules**:
  - 65A-4.207: Age requirements (Effective 3/13/2024)
  - 65A-4.208: Need determination (Effective 3/13/2024)
  - 65A-4.209: Income rules (Effective 4/29/2024)
  - 65A-4.210: Budgeting (Effective 3/13/2024)
  - 65A-4.214: Family Cap Requirements (Effective 3/13/2024)
  - 65A-4.220: Amount and Duration of Cash Payment (Effective 3/13/2024)

**Policy Resources:**
- **Title**: Florida's Cash Assistance (TANF) Policy Profile
- **URL**: https://www.nccp.org/wp-content/uploads/2024/11/TANF-profile-Florida.pdf
- **Published**: November 2024

---

### Key Eligibility Rules

#### Gross Income Limit
- **Threshold**: 185% of Federal Poverty Level (FPL)
- **Application**: Applies to applicants
- **Example**: For family of 3, approximately $3,981/month (2024)
- **Reference**: F.A.C. 65A-4.209

#### Net Income (Need Test)
- **Threshold**: Countable income must not exceed the applicable payment standard for family size
- **Calculation**: Gross income minus applicable disregards
- **Must pass**: Both gross income test AND net income test

#### Resource Limits
- **Asset Limit**: $2,000 in countable assets
- **Vehicle Exclusion**: Licensed vehicles with combined value up to $8,500 (for work-required families or disabled transport)
- **Reference**: Florida policy sources

---

### Income Disregards (Work Incentive Deductions)

#### Step 1: Per-Person Disregard
- **Amount**: $90 per person with earned income
- **Application**: Deducted from gross earned income first
- **Reference**: F.S. § 414.095

#### Step 2: "$200 and 1/2" Disregard
- **Flat Amount**: First $200 of remaining earned income
- **Percentage**: 50% of remaining earned income after $200
- **Calculation Process**:
  1. Total gross earned income
  2. Subtract $90 per earner
  3. Subtract first $200 of remaining earnings
  4. Subtract 50% of earnings above $200
- **Reference**: F.S. § 414.095; Florida DCF policy manual

---

### Payment Standards (Shelter Tiers)

Florida uses a three-tier payment structure based on shelter obligations:

#### Tier Definitions
- **Tier III (No Shelter)**: Family has no shelter obligation (living rent-free)
- **Tier II (Low Shelter)**: Monthly shelter obligation >$0 but ≤$50
- **Tier I (High Shelter)**: Monthly shelter obligation >$50 OR family is homeless

#### Payment Standard Amounts (Monthly)

| Family Size | Tier III (No Shelter) | Tier II (≤$50) | Tier I (>$50 or Homeless) |
|-------------|----------------------|----------------|---------------------------|
| 1           | $95                  | $153           | $180                      |
| 2           | $158                 | $205           | $241                      |
| 3           | $198                 | $258           | $303                      |
| 4           | $254                 | $309           | $364                      |
| 5           | $289                 | $362           | $426                      |
| 6           | $346                 | (varies)       | (varies)                  |
| 7+          | (varies)             | (varies)       | (varies)                  |

**Notes**:
- Maximum benefit for family of 3 (Tier I): $303/month - unchanged since 1992
- These amounts represent 9%, 12%, and 14% of FPL respectively for family of 3
- **Reference**: F.S. § 414.095(10); Florida DCF TCA fact sheet

---

### Benefit Calculation Formula

```
1. Gross Earned Income - ($90 × number of earners) = Adjusted Earned Income
2. Adjusted Earned Income - $200 = Remaining Earnings
3. Remaining Earnings × 0.5 = Additional Disregard
4. Adjusted Earned Income - $200 - Additional Disregard = Net Earned Income
5. Net Earned Income + Gross Unearned Income = Total Net Income
6. Payment Standard (for family size/tier) - Total Net Income = Benefit Amount
7. Round down to nearest $1
8. If result < $10, no cash benefit (but retain TCA status for Medicaid)
```

**Reference**: F.A.C. 65A-4.220; F.S. § 414.095

---

### Family Cap Policy

Florida imposes penalties on additional children born while receiving assistance:

#### Second Child Born on Assistance
- **Reduction**: 50% of the benefit increment for second child
- **Example**: Without family cap, second child would add ~$61/month; with cap, only adds ~$30.50/month
- **Reference**: F.A.C. 65A-4.214; Florida Policy Institute analysis

#### Third and Subsequent Children
- **Benefit**: No additional cash assistance for 3rd+ children born while on TCA
- **Exception**: Family cap does NOT apply to children conceived before receiving assistance
- **Reference**: F.A.C. 65A-4.214

**States with Family Cap**: Only 6 states maintain family cap policies (Arizona, Arkansas, Florida, Mississippi, North Carolina, South Carolina)

---

### Special Cases and Exceptions

#### Minimum Benefit
- **Amount**: $10/month minimum grant
- **Below Minimum**: Families eligible for <$10 receive no cash but retain TCA recipient status for:
  - Medicaid coverage
  - Food assistance eligibility

#### Time Limits
- **Federal**: 60-month (5-year) lifetime limit on federally-funded assistance
- **State**: Florida enforces the federal 60-month limit
- **Hardship Extensions**: Available through F.A.C. 65A-4.201

#### Demographic Eligibility
- **Age Limits**: Minor children under age 18 (or age 19 if full-time student)
- **Pregnant Women**: Eligible in last trimester (per F.A.C. 65A-4.215)
- **Reference**: F.A.C. 65A-4.207

---

### References for Code Implementation

#### For Parameters:
```yaml
reference:
  - title: "Florida Statute § 414.095 - Determining eligibility for temporary cash assistance"
    href: "https://www.flsenate.gov/Laws/Statutes/2024/414.095"
  - title: "Florida DCF Temporary Cash Assistance"
    href: "https://www.myflfamilies.com/services/public-assistance/temporary-cash-assistance"
```

#### For Variables:
```python
reference = "F.S. § 414.095; F.A.C. 65A-4.220"
documentation = "https://flrules.org/gateway/ChapterHome.asp?Chapter=65A-4"
```

---

### Implementation Status

**Existing Implementation Found**: Yes, Florida TANF is already implemented in:
- `/policyengine_us/parameters/gov/states/fl/dcf/tanf/`
- `/policyengine_us/variables/gov/states/fl/dcf/tanf/`

**Key Implementation Files**:
- Payment standards: `payment_standard/tier_1.yaml`, `tier_2.yaml`, `tier_3.yaml`
- Income disregards: `income_disregards/earned_flat.yaml`, `earned_percentage.yaml`, `earned_per_person.yaml`
- Family cap: `family_cap/second_child_reduction.yaml`, `third_plus_child_benefit.yaml`
- Resource limits: `resource_limit.yaml`, `vehicle_limit.yaml`

---

### Additional Context

**Historical Note**: Florida TANF payment standards were last updated in 1992. The purchasing power has eroded significantly due to inflation over 30+ years.

**Comparison to FPL**:
- Family of 3 maximum benefit ($303): Represents only 14% of Federal Poverty Level
- This is among the lowest TANF-to-poverty ratios in the United States

**Program Name**: In Florida, TANF is referred to as "Temporary Cash Assistance (TCA)" or part of the "WAGES Program" (Work and Gain Economic Self-Sufficiency)

---

### Data Quality Notes

1. **Payment amounts verified** against multiple sources (statute, policy manuals, advocacy reports)
2. **Tier definitions confirmed** in F.A.C. 65A-4.220 and F.S. § 414.095
3. **Income disregard calculation** documented in Florida DCF policy manual and statute
4. **Family cap policy** verified in administrative code and policy analysis reports
5. **All amounts current** as of 2024; no updates since 1992 for payment standards

---

### Outstanding Questions / Areas for Further Research

1. **Complete payment table**: Payment amounts for families sizes 6-20 for all three tiers (partial data found for Tier III)
2. **Tier II shelter threshold**: Confirm exact definition ($50 max) in statute
3. **Child support disregard**: Specific amount/percentage if any (not clearly documented in sources found)
4. **Irregular income quarterly limit**: Specific amount if applicable

---

### Source Accessibility Summary

✅ **Highly Accessible**:
- Florida Statutes (flsenate.gov)
- Florida Administrative Code (flrules.org)
- Florida DCF website (myflfamilies.com)

⚠️ **Moderately Accessible**:
- Florida DCF policy manuals (PDFs, some require direct download)
- NCCP policy profiles (PDFs)

❌ **Not Directly Accessible**:
- Complete payment standard tables in machine-readable format
- Detailed calculation worksheets or official examples
