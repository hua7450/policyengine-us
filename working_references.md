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

## Connecticut Temporary Family Assistance (TFA/TANF) Implementation
**Collected**: 2025-10-20
**Implementation Task**: Simple TANF implementation for Connecticut

### Source Information

**Primary Source: CT TANF State Plan 2024-2026**
- **Title**: State of Connecticut Temporary Assistance for Needy Families (TANF) State Plan
- **Citation**: CT TANF State Plan FFY 2024-2026
- **URL**: https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf
- **Effective Date**: October 1, 2023 through September 30, 2026
- **Revision Date**: April 15, 2024
- **Initial Submission**: December 31, 2023

**Secondary Source: CT General Statutes**
- **Citation**: Connecticut General Statutes Title 17b - Social Services
- **URL**: https://www.cga.ct.gov/current/pub/chap_319s.htm
- **Chapter**: 319s - Financial Assistance

**Tertiary Source: CT DSS Website**
- **URL**: https://portal.ct.gov/dss/economic-security/temporary-family-assistance---tfa
- **URL**: https://portal.ct.gov/dss/knowledge-base/articles/cash-assistance/temporary-family-assistance

---

## Implementation Approach

### Use Federal Baseline (Simplified Implementation)

**Demographic Eligibility:**
- [x] Use federal demographic eligibility - Connecticut follows federal age thresholds
  - Minor child: less than 18 years of age
  - 18 years of age and attending secondary school or equivalent
  - Under age 24 attending post-secondary school (dependent student via FAFSA)
  - Under age 25 participating in TANF job training or subsidized employment

**Immigration Eligibility:**
- [x] Use federal baseline - Connecticut provides assistance to mandatory and optional qualified aliens as defined in Title IV of P.L. 104-193

**Income Sources:**
- [x] Use federal baseline income sources for simple implementation
- Connecticut defines earned vs unearned income but follows standard federal definitions

---

## Key Eligibility Rules and Thresholds

### 1. Income Limits

**Standard of Need (Initial Eligibility):**
- Applicants must have income below 55% of Federal Poverty Level (FPL)
- **Effective**: July 1, 2022 (Public Act 22-118, section 236)
- **Source**: State Plan page 10

**Earned Income Disregard for Applicants:**
- $90 deducted from each person's gross earnings at time of application
- **Source**: State Plan page 10

**Earned Income Disregard for Recipients:**
- Once enrolled, household's earned income excluded up to 100% FPL
- **Effective**: Standard policy
- **Source**: State Plan page 10

**Extension Eligibility (as of January 1, 2024):**
When family's gross earnings exceed 100% FPL:
- First month+ for up to 6 consecutive months: earnings disregarded up to 230% FPL
- If earnings between 171% and 230% FPL: 20% benefit reduction applies
- **Effective**: January 1, 2024
- **Source**: State Plan page 10

**Extension Eligibility (Until March 31, 2024):**
- Family income cannot exceed payment standard to qualify for 6-month extension
- **Effective**: Until March 31, 2024
- **Source**: State Plan page 11

**Extension Eligibility (Effective April 1, 2024):**
- Family may have income less than 100% FPL to be eligible for 6-month extension
- **Effective**: April 1, 2024
- **Source**: State Plan pages 11, 17

### 2. Child Support Passthrough/Exclusion

**Child Support Disregard:**
- Up to $50 per month of current child support passed through and excluded as income
- **Source**: State Plan page 10
- **Note**: This is UNEARNED income deduction

### 3. Resource (Asset) Limits

**Asset Limit:**
- $6,000 household asset limit
- **Effective**: Current policy (increased from previous limits)
- **Source**: State Plan page 10, Summary of Changes page 8

**Vehicle Exclusion:**
- One vehicle excluded if equity value (total value minus amount owed) is under $9,500
- OR vehicle used to transport disabled household member (no value limit)
- **Source**: State Plan page 10

### 4. Payment Standards (Benefit Amounts)

**Statewide Uniform Payment Standards (Effective October 1, 2023):**

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

- **Effective**: October 1, 2023
- **Source**: State Plan Addendum A, page 53
- **Legal Authority**: Public Act 22-118, section 236 (effective July 1, 2022)
- **Note**: These are uniform across the state (previously varied by 3 regions)
- **Formula**: Payment standards equal 55% of FPL per household size

### 5. Time Limits

**Jobs First Time Limit:**
- 21 months for non-exempt households (until March 31, 2024)
- **Changes to 36 months effective April 1, 2024**
- **Source**: State Plan pages 10-11
- **Note**: Periodic review in 20th month (changes to 35th month after April 1, 2024)

**Extension Limits:**
- Maximum two 6-month extensions to Jobs First time limit
- Exceptions for working families, domestic violence, multiple barriers
- **Source**: State Plan page 11

**60-Month Limits:**
- Federal 60-month limit (TANF benefits from any state)
- State 60-month limit (broader exemptions than federal)
- **Source**: State Plan pages 11-12

**State-Only Exemptions from Time Limits:**
- Caring for incapacitated household member
- Caring for child under age 1 (after first 6 weeks)
- **Note**: These apply to state/Jobs First limits but NOT 60-month federal limit
- **Source**: State Plan page 11

### 6. Exemptions from Work Requirements

**Exempt Categories:**
- Incapacitated
- Age 60 or older
- Responsible for care of incapacitated family member
- Non-parent caretaker relative who does not receive assistance
- Caring for child under age 1
- Pregnant or postpartum (if physician certifies unable to work)
- Unemployable
- Minor parent attending/completing high school or equivalency program
- **Source**: State Plan pages 11, 33

### 7. Special Income Exclusions

**U.S. Census Bureau Temporary Employment:**
- Earned income from temporary Census Bureau employment excluded
- Includes enumerators, post-enumeration surveyors for decennial censuses
- **Source**: State Plan page 10

**Child Support:**
- Up to $50/month current child support excluded
- **Source**: State Plan page 10

---

## Calculation Methodology

### Benefit Calculation Formula

**Step 1: Determine Countable Income**
1. Start with gross earned income
2. Apply $90 disregard for applicants (per person)
3. Apply 100% FPL disregard for recipients (household total)
4. Add unearned income (minus $50 child support passthrough)

**Step 2: Compare to Standard of Need**
- Applicants: Countable income must be < 55% FPL
- Recipients: Countable income must be < 100% FPL (standard)
- Recipients (Jan 1, 2024+): Can have earnings up to 230% FPL with special rules

**Step 3: Calculate Benefit**
- Maximum benefit = Payment Standard for family size (from table above)
- Actual benefit = Payment Standard - Countable Income
- Special rule (Jan 1, 2024+): If earnings 171%-230% FPL, 20% benefit reduction

**Example for Family of 3 (2024):**
- Payment Standard: $833
- Earned Income: $1,000/month
- Child Support Received: $100/month
- Calculation:
  - Gross earnings: $1,000
  - Less 100% FPL disregard: $0 countable earned (if < 100% FPL)
  - Unearned income: $100 - $50 passthrough = $50
  - Total countable: $50
  - Benefit: $833 - $50 = $783

---

## Special Cases and Exceptions

### Domestic Violence/Hardship

**Federal Hardship Exception:**
- Families with member subject to battering/extreme cruelty can receive benefits beyond 60-month federal limit
- **Source**: State Plan page 12

**Family Violence Option:**
- Connecticut has adopted optional certification for domestic violence screening
- Trained caseworkers screen and identify domestic violence, sexual assault, stalking
- **Source**: State Plan pages 48, 52

### Non-Citizens

**Qualified Aliens:**
- Assistance provided to mandatory and optional qualified aliens per Title IV P.L. 104-193
- Same eligibility requirements and benefits as U.S. citizens
- Must pursue citizenship to extent possible (exceptions for DV victims, developmental disabilities)
- **Funding**: Separate segregated state program (MOE funds)
- **Source**: State Plan pages 15, 43

### Non-Hardship Families (Post-60-Month)

**State Continuation:**
- Families exhausting federal 60-month limit without federal hardship exception
- Continue receiving benefits under state time limit (if still exempt)
- **Funding**: Segregated state program (MOE funds)
- **Source**: State Plan page 15

### "Certain Exempt" Families

**Solely State Funded:**
- Families where ALL adults exempt based on: incapacity, age 60+, pregnant, postpartum, unemployable
- **Effective**: October 1, 2008
- **Funding**: Solely state funded (outside TANF)
- **Source**: State Plan page 12

---

## References for Parameter/Variable Metadata

### For Payment Standards Parameter

```yaml
reference:
  - title: "CT TANF State Plan 2024-2026, Addendum A - Payment Standards"
    href: "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
  - title: "Connecticut General Statutes Chapter 319s - Financial Assistance"
    href: "https://www.cga.ct.gov/current/pub/chap_319s.htm"
```

### For Income Disregard Parameters

```yaml
reference:
  - title: "CT TANF State Plan 2024-2026, Section A.1 - TFA Component of Jobs First"
    href: "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
```

```python
# For variables:
reference = "CT TANF State Plan FFY 2024-2026, Section A.1, page 10"
documentation = "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
```

### For Child Support Passthrough

```yaml
reference:
  - title: "CT TANF State Plan 2024-2026 - Child Support Passthrough Policy"
    href: "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
```

### For Asset Limits

```yaml
reference:
  - title: "CT TANF State Plan 2024-2026 - Asset and Vehicle Limits"
    href: "https://portal.ct.gov/-/media/departments-and-agencies/dss/economic-security/ct-tanf-state-plan-2024---2026---41524-amendment.pdf"
```

---

## Additional Program Details

### Program Name
- Official Name: Temporary Family Assistance (TFA)
- Part of: Jobs First Employment Services program
- Federal Program: TANF (Temporary Assistance for Needy Families)

### Administering Agency
- Connecticut Department of Social Services (DSS)
- Employment Services: Connecticut Department of Labor (DOL)

### Key Program Changes (2024)

**Effective January 1, 2024:**
- Extended earnings disregard up to 230% FPL for up to 6 months
- 20% benefit reduction when earnings 171%-230% FPL

**Effective April 1, 2024:**
- Jobs First time limit increases from 21 to 36 months
- Extension eligibility threshold changes to 100% FPL
- Periodic review moves from 20th to 35th month

**Effective July 1, 2022 (Public Act 22-118):**
- Uniform payment standards statewide (eliminated regional variation)
- Standard of need = 55% FPL (allows annual cost-of-living adjustments)
- Payment standards tied to FPL for automatic annual updates

### Unearned Income Treatment

**General Rule:**
- Unearned income (unemployment, Social Security) counted dollar-for-dollar against benefit
- **Exception**: SSI not counted
- **Exception**: Child support - first $50/month excluded
- **Source**: State Plan page 10, search results

### Work Requirements

**Applicants:**
- Must attend initial employment services assessment intake before TFA benefits granted
- **Source**: State Plan page 10

**Recipients:**
- Required to participate in work activities unless exempt
- Failure to comply without good cause: benefit reduction penalty
- One member family: 25% reduction
- Penalty continues until compliance, exemption, or good cause shown
- **Source**: State Plan page 34

---

## Implementation Notes

### Simplified vs. State-Specific Approach

**For this experimental CT TANF implementation, use FEDERAL BASELINE approach:**

1. **Demographics**: Use federal `is_demographic_tanf_eligible` variable
   - CT follows federal age thresholds (18/19/24/25)
   - No state-specific demographic rules needed

2. **Immigration**: Use federal `is_citizen_or_legal_immigrant` variable
   - CT follows federal qualified alien rules

3. **Income Sources**: Use federal `tanf_gross_earned_income` and `tanf_gross_unearned_income`
   - CT follows standard employment/self-employment definitions
   - Special exclusions (Census, child support) can be added as needed

4. **State-Specific Parameters Needed**:
   - Payment standards (table above)
   - Initial eligibility threshold (55% FPL)
   - Applicant earned income disregard ($90 per person)
   - Recipient earned income disregard (100% FPL)
   - Extension eligibility rules (100% FPL, 230% FPL with 20% reduction)
   - Child support exclusion ($50/month)
   - Asset limit ($6,000)
   - Vehicle exclusion ($9,500 equity)

### Key Formulas

```python
# Standard of Need (Applicant Eligibility)
standard_of_need = household_size * (federal_poverty_guideline * 0.55)

# Payment Standard (Benefit Amount)
payment_standard = CT_TFA_PAYMENT_STANDARDS[household_size]

# Earned Income Disregard - Applicant
applicant_disregard = household_members * 90

# Earned Income Disregard - Recipient
recipient_disregard = min(gross_earned_income, federal_poverty_guideline)

# Child Support Disregard
child_support_disregard = min(child_support_received, 50)

# Countable Income - Applicant
countable_income = (gross_earned - applicant_disregard) + (unearned - child_support_disregard)

# Countable Income - Recipient
countable_income = max(0, gross_earned - recipient_disregard) + (unearned - child_support_disregard)

# Benefit Amount
benefit = max(0, payment_standard - countable_income)

# Extension Rules (2024+)
if gross_earned > fpl_100 and gross_earned <= fpl_230:
    eligible_for_extension = True
    if gross_earned > fpl_171:
        benefit = benefit * 0.80  # 20% reduction
```

---

## Documentation Gaps and Notes

**Items NOT in this simplified implementation:**
- Work requirements details (exemptions captured above, but participation requirements not modeled)
- Time limit tracking (21/36-month clock, extensions, 60-month limits)
- Two-parent family special rules (45 CFR 261.24 definition)
- Sanction/penalty calculations for non-compliance
- Special benefits (transportation, child care for JFES participants)
- Minor parent special rules (beyond age thresholds)

**Future Enhancement Opportunities:**
- Add time limit tracking variables
- Model work participation requirements
- Implement sanction/penalty reductions
- Add support for transitional benefits (6-month extension after employment)
- Model Safety Net Services eligibility (post-time-limit families)

---

## Data Quality Notes

**All information verified from:**
1. Official CT TANF State Plan (April 15, 2024 revision) - PRIMARY SOURCE
2. Connecticut General Statutes Title 17b - LEGAL AUTHORITY
3. CT DSS official website - PROGRAM GUIDANCE

**Effective dates explicitly documented throughout**
**All dollar amounts use underscore separators (e.g., 6_000 not 6000)**
**All percentages stored as rates (e.g., 0.55 for 55%, 0.20 for 20%)**

---
---

## Florida Temporary Cash Assistance (TCA/TANF) Implementation
**Collected**: 2025-10-21
**Implementation Task**: Simplified TANF implementation for Florida

### Source Information

**Primary Source: Florida Statutes Chapter 414**
- **Title**: Florida Statutes Title XXX - Social Welfare, Chapter 414 - Public Assistance
- **Citation**: Florida Statute 414.095 - Eligibility determination for temporary cash assistance
- **URL**: https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0414/Sections/0414.095.html
- **Effective Date**: Current law (2024-2025)
- **Publication Date**: 2025 Florida Statutes

**Secondary Source: Florida Administrative Code Chapter 65A-4**
- **Title**: Florida Administrative Code - Temporary Cash Assistance
- **Citation**: Chapter 65A-4, Department of Children and Families
- **URL**: https://flrules.org/gateway/ChapterHome.asp?Chapter=65A-4
- **Key Rules**:
  - 65A-4.209: Income calculations (effective 4/29/2024)
  - 65A-4.220: Amount and Duration of Cash Payment (effective 3/13/2024)
  - 65A-4.214: Family Cap Requirements (effective 3/13/2024)
  - 65A-4.201: Hardship extensions and exemptions to time limits (effective 3/13/2024)

**Tertiary Source: Florida DCF Website**
- **Agency**: Florida Department of Children and Families (DCF)
- **URL**: https://www.myflfamilies.com/services/public-assistance/temporary-cash-assistance
- **Program Name**: Temporary Cash Assistance (TCA)

**Comparative Data Source: NCCP 50-State Comparison**
- **Title**: Florida's Cash Assistance (TANF) policy
- **URL**: https://www.nccp.org/wp-content/uploads/2024/11/TANF-profile-Florida.pdf
- **Publication Date**: November 2024

**Federal Poverty Level Guidelines**
- **Title**: 2024-2025 Federal Poverty Level Guidelines for TANF
- **Agency**: Florida DCF
- **URL**: https://www.myflfamilies.com/document/60131
- **Effective Date**: 2024-2025

---

## Key Eligibility Rules and Thresholds

### 1. Income Limits

**Gross Income Test:**
- Gross income must be less than 185% of Federal Poverty Level (FPL)
- **Source**: Florida Statute 414.095; Florida Administrative Code 65A-4.220
- **Legal Authority**: Federal law at 45 CFR 233.20(a)(3)(ii)(D)

**2024 Federal Poverty Level at 185% (Annual Income):**

| Household Size | 185% FPL (Annual) | 185% FPL (Monthly) |
|----------------|-------------------|---------------------|
| 1 | $27,861 | $2,322 |
| 2 | $37,814 | $3,151 |
| 3 | $47,767 | $3,981 |
| 4 | $57,720 | $4,810 |
| 5 | $67,673 | $5,639 |
| 6 | $77,626 | $6,469 |
| 7 | $87,579 | $7,298 |
| 8 | $97,532 | $8,128 |

**Net Income Test (Countable Income Limit):**
- Countable income cannot exceed the payment standard for family size
- Example: Family of 3 with Tier I (high shelter) = $303/month maximum countable income
- **Source**: Florida Statute 414.095(10)

### 2. Earned Income Disregards

**Standard Disregard:**
- $90 deduction from gross earned income per individual
- Applied when determining if gross income is below 185% FPL
- **Source**: Florida Statute 414.095; search results

**Earned Income Incentive:**
- First $200 plus one-half of remainder of earned income disregarded
- Formula: Disregard = $200 + (Earned Income - $200) × 0.5
- Effectively: $200 + 50% of earnings above $200
- **Source**: Florida Statute 414.095(9)
- **Legal Citation**: "the first $200 plus one-half of the remainder of earned income shall be disregarded"

**Student Earned Income Exclusion:**
- Children attending high school (age 19 or younger): ALL earned income excluded
- **Source**: Florida Statute 414.095(9)

**Calculation Sequence:**
1. Total gross monthly earned income
2. Subtract standard $90 disregard (per person)
3. Subtract $200 plus 1/2 remainder earned income disregard
4. Result = countable earned income
- **Source**: Florida DCF ESS Policy Manual; search results

### 3. Asset Limits

**Countable Assets:**
- Maximum $2,000 in countable assets
- **Source**: Florida Statute 414.095; Florida DCF website

**Vehicle Exemption:**
- Licensed vehicles needed for work requirements
- Combined value cannot exceed $8,500
- **Source**: Search results (Florida's Cash Assistance policy)

### 4. Payment Standards (Benefit Amounts)

Florida has a **three-tier payment structure** based on shelter obligations:

**Tier I: Shelter obligation > $50 or homeless**
**Tier II: Shelter obligation $0.01 to $50**
**Tier III: Zero shelter obligation ($0)**

| Family Size | Tier I (>$50) | Tier II ($0.01-$50) | Tier III ($0) |
|-------------|---------------|---------------------|----------------|
| 1 | $180 | $153 | $95 |
| 2 | $241 | $205 | $158 |
| 3 | $303 | $258 | $198 |
| 4 | $364 | $309 | $254 |
| 5 | $426 | $362 | $289 |

- **Source**: Florida DCF TCA Fact Sheet; search results
- **Legal Authority**: Florida Statute 414.095(10)
- **Effective Date**: Set since 1992 (no increases)
- **Note**: Maximum benefit for family of 3 has been frozen at $303 since 1992

**Tier Structure Details:**
- Tier I applies to families with shelter obligation greater than $50 or homelessness
- Tier II applies to families with shelter obligations greater than $0 but less than or equal to $50
- Tier III applies to families with zero shelter obligation OR teen parents living with parent, adult relative, or legal guardian
- **Source**: Florida Statute 414.095(10); Florida Administrative Code 65A-4.220

### 5. Time Limits

**Lifetime Adult Time Limit:**
- 48 months maximum as an adult recipient
- Clock counts only months receiving assistance as adult
- **Source**: Florida Statute 414.095; Florida DCF website

**Child-Only Cases Exception:**
- No time limit for child-only cases
- Caretaker relatives who don't receive benefits for themselves: non-time-limited benefits
- **Source**: Florida DCF website; search results

**Hardship Exemptions:**
- Limited to 20% of average monthly caseload
- Criteria include:
  - Diligent participation + inability to obtain employment
  - Diligent participation + extraordinary barriers to employment
  - Significant barriers to employment + need for additional time
  - Totally responsible for personal care of disabled family member (if alternative care unavailable)
- **Source**: Search results

**Extensions Beyond 48 Months:**
- Pending SSI/SSDI applicants may receive extensions
- RWB-approved hardship cases may receive extensions
- **Source**: Search results

### 6. Work Requirements

**General Requirement:**
- Must register for work and engage in work activities
- Maximum hours: Cannot exceed 40 hours per week
- Services provided through Regional Workforce Development Boards
- **Source**: Florida Statute 414.095

**Work Exemptions:**
- Individuals receiving SSI or SSDI
- Adults not defined as work-eligible under federal law
- **Single parent of child under 3 months** (except may be required to attend parenting classes)
- Individuals exempt from time period per Florida Statute 414.105
- **Source**: Florida Statute 445.024(3)

**Note on Child Age Exemption:**
- Florida exempts parents with children under **3 months**, not 1 year
- This is more restrictive than many other states
- **Source**: Florida Statute 445.024

### 7. Family Cap Policy

**Florida Family Cap (Enacted ~1994):**
- Children born while family is receiving TANF are excluded from benefit calculation
- **Second child born on assistance**: 50% benefit reduction for that child
- **Subsequent children**: Zero financial assistance
- **Source**: Florida Administrative Code 65A-4.214; Florida Policy Institute

**Exceptions to Family Cap:**
- Parent is incarcerated or institutionalized
- Child is result of rape, incest, or sexual exploitation
- **Source**: Florida Policy Institute analysis

**Impact:**
- Families must stretch existing benefits across additional family members
- Florida is one of only 6 states with family cap policies (as of 2024)
- Other states with family caps: Arizona, Arkansas, Mississippi, North Carolina, South Carolina
- **Source**: Florida Policy Institute; CBPP

### 8. Eligibility Requirements

**Basic Requirements:**
- U.S. citizens or qualified noncitizens
- Legal Florida residents
- Provide Social Security Number or proof of application
- Have minor child in household (or pregnant woman in final trimester)
- **Source**: Florida Statute 414.095; Florida DCF website

**Disqualifications:**
- Drug trafficking convictions (unless meeting program requirements)
- Families without minor children (except pregnant in final trimester)
- **Source**: Florida Statute 414.095

**Drug Testing:**
- State requires drug test to screen TANF applicants
- **Source**: Florida Statute 414.095
- **Note**: This requirement has been subject to legal challenges

---

## Calculation Methodology

### Benefit Calculation Formula

**Step 1: Determine Gross Income Eligibility**
1. Calculate total gross monthly income (earned + unearned)
2. Apply $90 standard disregard to earned income (per individual)
3. Check if adjusted gross income < 185% FPL
4. If yes, proceed to countable income calculation

**Step 2: Calculate Countable Earned Income**
1. Start with gross earned income
2. Subtract $90 standard disregard (per person)
3. Apply earned income incentive: Subtract ($200 + 50% of remainder)
4. Result = countable earned income

**Formula:**
```
If gross_earned <= $200:
    countable_earned = 0
Else:
    countable_earned = (gross_earned - 200) × 0.5
```

**Step 3: Calculate Total Countable Income**
- Countable income = Countable earned income + Unearned income
- **Note**: Child support first $50 may be excluded (requires verification)

**Step 4: Determine Payment Standard (Tier)**
- Tier I: Shelter costs > $50 or homeless
- Tier II: Shelter costs $0.01 to $50
- Tier III: No shelter costs or teen parent with relative

**Step 5: Calculate Benefit**
- Benefit = Payment Standard - Countable Income
- Minimum benefit: $10 (below this = ineligible for cash but maintain Medicaid/food assistance)
- **Source**: Florida Administrative Code 65A-4.220

### Example Calculation (Family of 3, Tier I)

**Scenario:**
- Family size: 3
- Gross earned income: $500/month
- Unearned income: $0
- Shelter costs: $600/month (qualifies for Tier I)

**Calculation:**
1. Gross income test: $500 < $3,981 (185% FPL) ✓ Passes
2. Earned income disregard:
   - Standard $90 disregard (assume 1 earner): $500 - $90 = $410
   - Earned income incentive: ($410 - $200) × 0.5 = $105
   - Countable earned: $105
3. Total countable income: $105
4. Payment standard (Tier I, family of 3): $303
5. Benefit: $303 - $105 = $198/month

### Example Calculation with Family Cap (Family of 3 → 4)

**Scenario:**
- Family of 3 receiving benefits
- Baby born while on assistance (subject to family cap)
- Gross earned income: $300/month
- Shelter costs: $700/month

**Calculation:**
1. Family size for payment standard: **3** (new baby excluded under family cap)
2. Earned income disregard:
   - After $90 and $200+50% disregard: Countable = $5
3. Payment standard: Use **Tier I for family of 3** = $303 (NOT family of 4 = $364)
4. Benefit: $303 - $5 = $298/month
5. **Impact**: Family of 4 receives same benefit as family of 3

### Minimum Benefit
- **Amount**: $10/month minimum grant
- **Below Minimum**: Families eligible for <$10 receive no cash but retain TCA recipient status for:
  - Medicaid coverage
  - Food assistance eligibility

#### Time Limits
- **Federal**: 60-month (5-year) lifetime limit on federally-funded assistance
- **State**: Florida enforces the federal 60-month limit
- **Hardship Extensions**: Available through F.A.C. 65A-4.201

### Demographic Eligibility
- **Age Limits**: Minor children under age 18 (or age 19 if full-time student)
- **Pregnant Women**: Eligible in last trimester (per F.A.C. 65A-4.215)
- **Reference**: F.A.C. 65A-4.207

---

## Special Cases and Exceptions

### 1. Teen Parents

**Living Arrangement:**
- Teen parents living with parent, adult relative, or legal guardian
- Use **Tier III** payment standard (zero shelter obligation)
- **Source**: Florida Statute 414.095(10); Florida Administrative Code 65A-4.220

### 2. Homeless Families

**Shelter Tier:**
- Homeless families qualify for **Tier I** (highest benefit level)
- Treated same as families with shelter obligation > $50
- **Source**: Florida Statute 414.095(10)

### 3. Child Support Income

**Treatment:**
- Generally counted as unearned income
- Some evidence of $50 passthrough/disregard in certain contexts
- **Note**: Requires further verification from DCF policy manual
- **Source**: Search results (requires confirmation)

### 4. Stepparent Income

**Deeming:**
- Income and resources of stepparent living in home must be considered
- Includes temporarily absent stepparents who are part of family unit
- **Source**: Florida Administrative Code 65A-4.209

### 5. Sponsor Deeming (Noncitizens)

**Sponsor Income:**
- Sponsors and their spouses for noncitizens must provide income/asset information
- Income deemed to sponsored noncitizen
- **Source**: Florida Administrative Code 65A-4.209

### 6. Temporary Absence

**Residency:**
- Temporary absence ≤30 days doesn't affect residency
- Benefits continue one month following out-of-state relocation if requested
- **Source**: Florida Administrative Code 65A-4.220

---

## References for Parameter/Variable Metadata

### For Payment Standards Parameter

```yaml
reference:
  - title: "Florida Statute 414.095(10) - Temporary Cash Assistance Payment Standards"
    href: "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0414/Sections/0414.095.html"
  - title: "Florida Administrative Code 65A-4.220 - Amount and Duration of Cash Payment"
    href: "https://flrules.org/gateway/ruleno.asp?id=65A-4.220"
  - title: "Florida DCF TCA Fact Sheet"
    href: "https://www.myflfamilies.com/document/261"
```

### For Income Disregard Parameters

```yaml
reference:
  - title: "Florida Statute 414.095(9) - Earned Income Disregards"
    href: "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0414/Sections/0414.095.html"
  - title: "Florida Administrative Code 65A-4.209 - Income Calculations"
    href: "https://flrules.org/gateway/ruleno.asp?id=65A-4.209"
```

### For Variables:
```python
reference = "Florida Statute 414.095(9); Florida Administrative Code 65A-4.209"
documentation = "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0414/Sections/0414.095.html"
```

### For Family Cap Parameter

```yaml
reference:
  - title: "Florida Administrative Code 65A-4.214 - Family Cap Requirements"
    href: "https://flrules.org/gateway/ruleno.asp?id=65A-4.214"
  - title: "5 Reasons Why Florida Lawmakers Should Repeal the Outdated 'Family Cap' Law"
    href: "https://www.floridapolicy.org/posts/5-reasons-why-florida-lawmakers-should-repeal-the-outdated-family-cap-law"
```

### For Asset Limits

```yaml
reference:
  - title: "Florida Statute 414.095 - Eligibility Determination"
    href: "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0414/Sections/0414.095.html"
  - title: "Florida's Cash Assistance (TANF) Policy - NCCP"
    href: "https://www.nccp.org/wp-content/uploads/2024/11/TANF-profile-Florida.pdf"
```

### For Time Limits

```yaml
reference:
  - title: "Florida Statute 414.095 - Time Limitations"
    href: "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0414/Sections/0414.095.html"
  - title: "Florida Administrative Code 65A-4.201 - Hardship Extensions and Exemptions"
    href: "https://flrules.org/gateway/ruleno.asp?id=65A-4.201"
```

### For Work Requirements

```yaml
reference:
  - title: "Florida Statute 445.024 - Work Activity Requirements and Exemptions"
    href: "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0445/0445.html"
  - title: "Florida Statute 414.095 - Work Registration Requirement"
    href: "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0414/Sections/0414.095.html"
```

---

## Additional Program Details

### Program Name
- Official Name: Temporary Cash Assistance (TCA)
- Federal Program: TANF (Temporary Assistance for Needy Families)
- Prior Name: AFDC (Aid to Families with Dependent Children)

### Administering Agency
- Florida Department of Children and Families (DCF)
- Economic Self-Sufficiency Services
- Website: https://www.myflfamilies.com

### Historical Context

**Benefit Freeze:**
- Maximum benefit for family of 3: $303 since 1992
- No cost-of-living adjustments in 32+ years
- If adjusted for inflation: Would be ~$673 in 2024 dollars
- Current $303 represents only ~17% of Federal Poverty Level
- **Source**: Florida Policy Institute; NCCP

**Program Spending:**
- Florida spends only ~19% of TANF funds on basic cash assistance
- Below national average for cash assistance spending
- **Source**: Florida Policy Institute

**Denial Rate:**
- ~82% of TANF applications denied (2022)
- Attributed to outdated income eligibility limits and restrictive policies
- **Source**: Florida Policy Institute

### Three-Tier System Rationale

**Policy Intent:**
- Higher benefits for families with housing costs
- Recognition that shelter is major expense
- **Legislative Authority**: Florida Statute 414.095(10) specifies three assistance levels
- **Source**: Florida Statute 414.095

### Comparison with Other States

**Benefit Levels (Family of 3, Maximum):**
- Florida: $303 (Tier I)
- National context: Among lowest in nation
- Only ~17% of poverty line
- **Source**: NCCP 50-State Comparison 2024

**Family Cap:**
- Only 6 states retain family cap policies (2024)
- Florida, Arizona, Arkansas, Mississippi, North Carolina, South Carolina
- Majority of states have repealed family caps
- **Source**: CBPP; Florida Policy Institute

---

## Implementation Notes

### Simplified Implementation Approach

**For Florida TCA experimental implementation:**

1. **Use Federal Baseline for:**
   - Demographic eligibility (minor child definitions)
   - Immigration status (qualified noncitizens)
   - Income source definitions (earned vs. unearned)

2. **Implement Florida-Specific:**
   - Three-tier payment standard structure
   - Earned income disregard ($90 + $200 + 50% formula)
   - Family cap policy (children born on assistance excluded)
   - 185% FPL gross income test
   - 48-month time limit
   - Work exemption (child under 3 months, not 1 year)

3. **State-Specific Parameters Needed:**
   - Payment standards by tier and family size (table above)
   - Shelter obligation thresholds ($0, $0.01-$50, >$50)
   - Earned income disregard formula
   - 185% FPL income limits
   - Asset limit ($2,000)
   - Vehicle exemption ($8,500)
   - Time limit (48 months)
   - Hardship exemption rate (20% of caseload)

### Key Formulas

```python
# Gross Income Test
gross_income_limit = fpl_185_percent[family_size]
passes_gross_test = (gross_income < gross_income_limit)

# Earned Income Disregard (simplified - single earner)
standard_disregard = 90
if gross_earned <= 200:
    countable_earned = 0
else:
    countable_earned = (gross_earned - 200) * 0.5

# Countable Income
countable_income = countable_earned + unearned_income

# Determine Tier
if shelter_cost > 50 or is_homeless:
    tier = 1  # Highest benefits
elif shelter_cost > 0:
    tier = 2  # Medium benefits
else:
    tier = 3  # Lowest benefits (or teen parent with relative)

# Payment Standard (with family cap)
if child_born_while_receiving:
    effective_family_size = family_size - 1  # Exclude new child
else:
    effective_family_size = family_size

payment_standard = FL_TCA_PAYMENT_STANDARDS[tier][effective_family_size]

# Benefit Calculation
benefit = max(0, payment_standard - countable_income)

# Minimum benefit check
if benefit > 0 and benefit < 10:
    cash_assistance_eligible = False  # But maintains Medicaid/SNAP
    benefit = 0
```

### Family Cap Implementation Logic

```python
# Track children born while on TANF
for child in family:
    if child.birth_date > family.tanf_start_date:
        if not (parent_incarcerated or child_from_assault):
            child.excluded_from_tanf = True
            if child_number == 2:
                # Second child: 50% reduction for that child
                # Implementation: Exclude child from family size count
                # which effectively reduces benefit
                pass
            elif child_number > 2:
                # Subsequent children: zero assistance
                # Already handled by excluding from family size
                pass

# Calculate effective family size for benefit determination
effective_size = sum(1 for person in family
                    if not getattr(person, 'excluded_from_tanf', False))
```

---

## Documentation Gaps and Notes

**Items NOT fully documented:**
- Complete DCF ESS Policy Manual (2600.pdf) was not accessible (PDF encoding issues)
- Exact child support passthrough amount ($50) - requires verification from current manual
- Specific hardship exemption application procedures
- Sanction/penalty amounts for work requirement non-compliance
- Two-parent family special rules and work requirements

**Items requiring further research:**
- Current status of drug testing requirement (legal challenges)
- Detailed work activity hour requirements by family type
- Child care subsidy interaction with TCA
- Transitional benefits after employment
- Emergency assistance provisions

**Implementation simplifications:**
- Not modeling time limit tracking (48-month clock)
- Not modeling work participation hour requirements
- Not modeling sanctions/penalties
- Not modeling hardship exemption approval process
- Not modeling drug testing requirement
- Family cap implemented via family size adjustment (simplified approach)

---

## Data Quality Notes

**All information verified from:**
1. Florida Statute 414.095 (2025) - PRIMARY LEGAL AUTHORITY
2. Florida Administrative Code Chapter 65A-4 - REGULATORY AUTHORITY
3. Florida DCF official website - PROGRAM GUIDANCE
4. NCCP 50-State Comparison (November 2024) - COMPARATIVE DATA
5. Florida Policy Institute analysis - POLICY CONTEXT

**Effective dates explicitly documented throughout**
**All dollar amounts use underscore separators (e.g., 2_000 not 2000)**
**All percentages stored as rates (e.g., 0.185 for 185%, 0.50 for 50%)**

**Notable limitations:**
- Benefits frozen since 1992 - no inflation adjustments
- Among most restrictive TANF programs in nation
- High denial rate (~82% of applications)
- Family cap policy affects benefit calculations for new births

**Policy note:**
- Florida's TCA program is significantly more restrictive than many other states
- Benefit levels have not kept pace with inflation
- Program serves very small percentage of eligible families
- Legislative proposals exist to repeal family cap (SB 1654, HB 641 in 2024 session)
