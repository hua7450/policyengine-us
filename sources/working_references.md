# Collected Documentation

## Alabama SSI/SSP (State Supplementary Payment) Implementation
**Collected**: 2026-03-18
**Implementation Task**: Implement Alabama's State Supplementary Payment (SSP) to the federal Supplemental Security Income (SSI) program

---

## Official Program Name

**Federal Program**: Supplemental Security Income (SSI)
**State's Official Name**: State Supplementation (SUP) -- also referred to as Optional Supplementation
**Abbreviation**: SUP (in DHR documents), SSP (federal terminology)
**Source**: Alabama Administrative Code Chapter 660-2-4, "STATE SUPPLEMENTATION"; Code of Alabama 1975, Title 38
**Administering Agency**: Alabama Department of Human Resources (DHR), Economic Assistance Division -- administered at the county level through County Departments of Human Resources

**Variable Prefix**: `al_ssp` (using federal SSP terminology for consistency with other state implementations)

---

## Program Overview

Alabama provides a state-administered optional supplement to SSI recipients (and certain grandfathered non-SSI recipients) who require care in specific living arrangements. The program is entirely state-funded (both administration and assistance).

**Key characteristics:**
- State-administered (NOT federally administered -- SSA does not issue these payments)
- Extremely small caseload: approximately 20 recipients statewide as of January 2025 (9 OAP + 0 AB + 11 APTD)
- Payment amounts have been frozen since at least 1995 (no COLA adjustments)
- Limited to persons requiring care in specified living arrangements
- No additional income disregards beyond federal SSI rules

**Program categories (legacy names from pre-1974 adult assistance programs):**
- **OAP** - Old Age Pension (aged 65+)
- **AB** - Aid to the Blind
- **APTD** - Aid to the Permanently and Totally Disabled

---

## Source 1: Alabama Administrative Code, Chapter 660-2-4

### Source Information
- **Title**: Alabama Administrative Code, Chapter 660-2-4 -- STATE SUPPLEMENTATION
- **Citation**: Ala. Admin. Code r. 660-2-4-.01 through 660-2-4-.29 and Appendix A
- **URL**: https://admincode.legislature.state.al.us/api/chapter/660-2-4
- **Effective Date**: Original effective June 28, 1983; various amendments through January 15, 1992. Supplement dated 3/31/95
- **Format**: 61-page PDF

### Key Rules and Thresholds

#### General Eligibility (660-2-4-.15)

Eligibility on the factors of age, disability, blindness, residence, citizenship, resources, and income is established by Supplemental Security Income (SSI) Program staff based on Title XVI of the Social Security Act.

**Meaning**: Alabama defers to federal SSI rules for all basic eligibility factors. No separate state eligibility determination for these factors.

#### Eligibility Factors Other Than Need (660-2-4-.16)

A person meeting general eligibility criteria must ALSO meet one of these care requirements:

1. **Independent Homelife Care (IHC)**: Must be certified as needing independent homelife care in:
   - A private home, OR
   - A foster home licensed/approved by DHR
   - *Note: Personal care (pre-9/30/1986 recipients only) -- grandfathered*

2. **Specialized Independent Homelife Care**: Must be certified as needing (on or after 10/1/1986) specialized IHC AND:
   - Must be receiving benefits under the Elderly/Disabled Medicaid Waiver Program
   - Must meet skilled nursing facility criteria per 660-2-4-.28

**Physician certification required**: Recommendation for care must be made by a legally licensed physician.

#### Definition of Independent Homelife Care (660-2-4-.17)

Care from someone else to enable a person to live as independently as possible outside a nursing home. Services include:
- Help with prescribed exercise routines
- Changing bandages/dressings on physician's advice
- Administering prescribed medication
- Assisting with prostheses or ambulation aids
- Assistance in locomotion
- Maintaining acceptable state of cleanliness
- Maintaining orientation to time, place, and events
- Reminding of medication needs
- Other health-related functions

**Not included**: Companionship for pleasure or convenience rather than protection and necessity.

#### Definition of Specialized Independent Homelife Care (660-2-4-.27)

Services incidental to a medical need to assist the functionally impaired individual with:
- Personal hygiene
- Dressing
- Ambulation
- Meal preparation
- Eating
- Self-administering medications
- Maintaining a safe and sanitary environment

#### Care in Cerebral Palsy Treatment Centers (660-2-4-.18)

- Limited to persons who were eligible for optional supplementation as of June 1, 1981
- Supplement amount: **$196/month**
- For non-SSI recipients: difference between $196 and income in excess of the SSI federal benefit rate
- Only for APTD category
- **Effectively closed to new enrollment since June 1981**

#### Need Requirement (660-2-4-.19)

To be eligible for SUP based on need, an individual must be a recipient of SSI through the Social Security Administration.

**Critical rule**: SSI recipients are considered needy and entitled to the **full supplement**, if otherwise eligible. No separate income/resource determination is necessary for SSI recipients.

#### Amount of Assistance Payment (660-2-4-.10)

The amount of assistance payment is determined by the **kind of care needed**, subject to funds available. When available funds are expended on current recipients, the State Department may freeze the caseload.

#### Non-SSI Supplementation (SUP) Recipients (660-2-4-.26)

- Limited to persons receiving optional supplementation as of March 7, 1986
- **Effectively closed to new non-SSI enrollment since March 1986**
- Must meet all eligibility requirements AND only be ineligible for SSI due to income
- Supplement = difference between countable income and applicable supplement amount
- Must not have:
  - Resources exceeding Title XVI maximum
  - Gross countable income exceeding Alabama Medicaid Agency limit
  - Net countable income exceeding appropriate supplement
- Income/resource rules per 20 CFR 416, Subparts K and L

#### Care Provider Requirements (660-2-4-.29)

Effective February 14, 1992:
- Must be employed by a certified home health agency, OR
- If County Health Department does not make services available: an individual who declares in writing having at least 6th grade education, is physically/mentally able, has not been convicted of a serious crime, has not been fired for dereliction of duty
- **Cannot be**: child, stepchild, adoptive child, son/daughter-in-law, parent, stepparent, adoptive parent, spouse, brother, sister, brother/sister-in-law

### Payment Amounts (Attachment 660-2-4-.19a)

**SPECIAL NEEDS OF APPLICANTS AND RECIPIENTS**

| Living Arrangement / Care Type | Monthly Payment | Maximum Budgeted |
|---|---|---|
| FCMP Nursing Care (when required) | $100.00 | $60.00 |
| Nursing Care Supplement | $60.00 | $60.00 |
| Personal Care Supplement -- Level of Independence "A" | $60.00 | $60.00 |
| Personal Care Supplement -- Level of Independence "B" | $56.00 | $56.00 |
| Personal Care or Nursing Care Supplement in Foster Care | $110.00 | $110.00 |
| Care in a Cerebral Palsy Treatment Center (APTD) | $196.00 | $196.00 |

**Source**: Attachment 660-2-4-.19a, PDF page 24 of Chapter 660-2-4
**PDF URL**: https://admincode.legislature.state.al.us/api/chapter/660-2-4#page=24

#### Level A vs Level B Distinction

- **Level A ($60)**: Higher level of independence -- person requires less intensive care
- **Level B ($56)**: Lower level of independence -- person requires more intensive care
- The exact clinical criteria for Level A vs Level B are determined by physician certification

### Federal Benefit Rate Chart (Attachment 660-2-4-.26a)

This chart is used for Non-SSI SUP recipients to determine gross income eligibility. Values shown are from January 1, 1995 (frozen in regulations but the actual FBR used follows current federal rates):

| Living Arrangement | FBR | Gross Income Limit |
|---|---|---|
| Individual in own home | $458.00 | $1,374.00 |
| Individual in household of another (receiving support and maintenance) | $305.34 | $916.02 |
| Individual with spouse both in household of another (Couple standard) | $687.00 | $2,748.00 |
| Individual in nursing home | $30.00 | -- |

**Source**: Attachment 660-2-4-.26a, PDF page 26 of Chapter 660-2-4
**PDF URL**: https://admincode.legislature.state.al.us/api/chapter/660-2-4#page=26

**NOTE**: The FBR values in the regulation text are from 1995 and are outdated. The actual FBR follows current federal SSI rates. But the state supplement amounts ($56/$60/$110/$196) have NOT changed and remain frozen at 1995 levels as confirmed by January 2025 DHR statistical reports.

---

## Source 2: Alabama DHR Public Assistance Payment Manual (Appendix N, Section 3)

### Source Information
- **Title**: Appendix N Sec 3 -- Public Assistance Payment Manual
- **Citation**: Alabama DHR Policy Manual, Section 12200 (Income)
- **URL**: https://dhr.alabama.gov/wp-content/uploads/2022/04/Appendix-N-Sec-3-Public-Assistance-Payment-Manual.pdf
- **Effective Date**: Various revisions through Rev 770 (April 2012)

### Key Rules

#### Income Determination for SSI Recipients (Section 12200)

"In determining eligibility for a supplement, a separate income/resource determination is not necessary for persons receiving SSI. **SSI recipients are considered needy and entitled to the full supplement**, if otherwise eligible."

"SSI recipient" includes a person who was determined eligible for SSI, but whose SSI payment is "in suspense", or withheld, for a reason other than ineligibility.

#### Income Determination for Non-SSI Recipients (Section 12200)

A person not receiving SSI may receive optional supplementation only if his gross income is within certain limits. Refer to the Federal Benefit Rate Chart in Appendix I.

#### Income Exclusions

Federal SSI income exclusions apply (20 CFR 416, Subpart K). No additional state-specific income disregards beyond federal SSI rules.

#### Resource Limits

Under the reserve policy for the Supplementation Program:
- Individual: $2,000
- Married couple living together: $3,000 (whether one or both eligible)
- These match the federal SSI resource limits

#### Deeming Rules (Section 12100)

Follows federal SSI deeming rules:
- **Spouse to spouse**: Uses SSI deeming methodology (20 CFR 416)
- **Parent to child**: Uses SSI deeming methodology
- $65 earned income exclusion and 1/2 remainder applied
- 1/2 FBR individual comparison for deemed income threshold

---

## Source 3: Alabama DHR Monthly Statistical Reports (Green Books)

### Source Information
- **Title**: Alabama DHR Monthly Statistical Reports
- **URLs**:
  - January 2025: https://dhr.alabama.gov/wp-content/uploads/2025/07/STAT0125.pdf
  - March 2024: https://dhr.alabama.gov/wp-content/uploads/2024/09/STAT0324.pdf
  - November 2023: https://dhr.alabama.gov/wp-content/uploads/2024/02/STAT1123.pdf

### Current Caseload and Payment Data (January 2025)

| Category | Total Recipients | Average Payment/Case |
|---|---|---|
| OAP (Old Age Pensions) | 9 | $57.33 |
| AB (Aid to Blind) | 0 | $0.00 |
| APTD (Aid to Permanently/Totally Disabled) | 11 | $56.73 |
| **TOTAL** | **20** | -- |

Individual payment amounts observed in January 2025 data:
- $56.00 (most common -- Level B)
- $60.00 (Level A)
- $58.00 (appears to be an average or partial-month payment)

**APTD footnote (January 2025)**: "Includes home life supplements of $168.00 for 3 adults and 0 children in foster homes licensed or approved by the Department of Human Resources." ($168 / 3 = $56 per adult)

### Historical Consistency

Comparing November 2023, March 2024, and January 2025 reports confirms:
- Payment amounts ($56/$60) have been unchanged
- Caseload is stable at approximately 20 recipients statewide
- No foster care supplement ($110) or cerebral palsy supplement ($196) recipients appear in recent data (though the regulatory authority remains)

---

## Source 4: SSA State Assistance Programs for SSI Recipients (2011 report)

### Source Information
- **Title**: State Assistance Programs for SSI Recipients, January 2011 -- Alabama
- **Citation**: SSA Publication
- **URL**: https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/al.html
- **Note**: Returns 403 error -- content obtained from WorkWorld mirror and web search excerpts

### Key Information from SSA Report

**Administration**: State-administered (not federally administered). SSA does not issue these payments.

**Statutory Authority**: Code of Alabama 1975 as amended, Title 38

**Funding**: Both administration and assistance funded with state funds

**Coverage**: All SSI recipients (including children) and certain grandfathered non-SSI recipients in specified living arrangements

**Benefit amounts (2011 data, per SSA):**
- Level A Individual (IHC in private home/personal care home): $60 supplement
- Level B Individual: $56 supplement
- Specialized IHC: $60 supplement
- Foster Home Care: $110 supplement
- Cerebral Palsy Treatment Center: $196 supplement
- Couples receive double the individual amounts

**No additional disregards**: Beyond federal SSI standards

**Resource limits**: Federal SSI limitations apply

**Recoveries/Liens**: None

**Financial responsibility**: Spouse for spouse; parent/stepparent for child under 18

---

## Source 5: WorkWorld SSI State Supplement -- Alabama

### Source Information
- **Title**: SSI State Supplement -- Alabama
- **URL**: https://help.workworldapp.com/wwwebhelp/ssi_state_supplement_alabama.htm
- **Data Year**: Calendar year 2010 payment levels

### Combined Benefit Amounts (Federal SSI + State Supplement)

This source provides the **combined** amounts (federal FBR + state supplement). The state supplement amount is the difference:

| Living Arrangement | State Supplement | Combined Total (2010) |
|---|---|---|
| IHC Level A (Private Home) | $60 | $734 |
| IHC Level B (Private Home) | $56 | $730 |
| IHC Level A (with Support & Maintenance) | $60 | $509.34 |
| IHC Level B (with Support & Maintenance) | $56 | $505.34 |
| Specialized IHC | $60 | $734 |
| Foster Home Care | $110 | $784 |
| Cerebral Palsy Treatment Center | $196 | $870 |

**Couple amounts**: Double the individual amounts

---

## Source 6: Code of Alabama 1975, Title 38

### Source Information
- **Title**: Code of Alabama 1975, Title 38 -- Public Welfare
- **Citation**: Code of Alabama 1975, Title 38, Chapter 4 (Public Assistance Generally)
- **URL**: https://law.justia.com/codes/alabama/title-38/chapter-4/
- **Key Section**: Section 38-4-1 (Persons to Whom Public Assistance Payable)

### Statutory Provisions

Public assistance payable to:
- Needy blind persons (AB category)
- Needy persons over age 65 (OAP category)
- Dependent children
- Permanently and totally disabled persons (APTD category)

**Restrictions**: No assistance to inmates of public institutions (except patients in institutions where payments are matchable under the Social Security Act).

**For APTD eligibility (Section 38-4-1)**: Person must be:
1. Age 18 or older
2. Permanently and totally disabled per state department definition
3. Unable to provide himself with necessities of life due to disability
4. Without sufficient income and resources from all sources
5. Alabama resident at time of application
6. Has not disposed of property to qualify
7. Not receiving other federally-matched public assistance

---

## Benefit Calculation

### For SSI Recipients (Current -- the vast majority of cases)

**Formula**: Flat supplement amount based on living arrangement

```
State Supplement = Flat amount per living arrangement
```

The SSI recipient receives the full supplement amount regardless of their SSI payment amount. No income test or offset applies -- SSI eligibility IS the need determination.

| Living Arrangement | Individual/Month | Couple/Month |
|---|---|---|
| Independent Homelife Care -- Level A | $60 | $120 |
| Independent Homelife Care -- Level B | $56 | $112 |
| Foster Home Care | $110 | $220 |
| Cerebral Palsy Treatment Center (APTD only) | $196 | $392 |
| Specialized Independent Homelife Care | $60 | $120 |

### For Non-SSI SUP Recipients (Grandfathered -- effectively closed since March 1986)

**Formula**: Difference between supplement level and countable income above FBR

```
State Supplement = Applicable Supplement Level - (Countable Income - Federal Benefit Rate)
```

If the result is negative, no supplement is paid.

**Eligibility test**: Gross countable income must not exceed the Medicaid Agency gross income limit.

### For Cerebral Palsy Treatment Center (Non-SSI)

```
State Supplement = $196 - (Income in excess of SSI Federal Benefit Rate)
```

---

## Implementation Approach

### Relationship to Existing Federal SSI Implementation

The existing PolicyEngine SSI implementation (`ssi` variable) handles all federal eligibility and benefit calculation. The Alabama SSP is an ADD-ON to SSI.

**Key design decision**: The Alabama SSP is primarily a flat supplement for SSI recipients in specific living arrangements. The implementation requires:

1. **Eligibility**: Person must be `is_ssi_eligible_individual` AND in a qualifying living arrangement
2. **Benefit**: Flat amount based on living arrangement (no income offset for SSI recipients)
3. **Living arrangement**: New input variable needed (or reuse existing `ssi_living_arrangement` if one exists)

### Implementation Complexity: SIMPLE

- No complex income calculations (uses federal SSI eligibility)
- Flat payment amounts (no formula-based computation for SSI recipients)
- No state-specific deductions or disregards
- Payment amounts frozen since 1995 (no COLA mechanism)
- Very small caseload (~20 people)
- The non-SSI recipient path is effectively closed and could be excluded from initial implementation

### Recommended Variables

1. `al_ssp` -- Main benefit variable (Person, YEAR, float)
2. `al_ssp_eligible` -- Eligibility variable (Person, YEAR, bool)
3. Input variable for living arrangement category needed (or adapt existing)

### Parameter Structure

```
gov/states/al/dhr/ssp/
  amount/
    level_a.yaml       # $60/month (IHC Level A and Specialized IHC)
    level_b.yaml       # $56/month (IHC Level B)
    foster_care.yaml   # $110/month
    cerebral_palsy.yaml # $196/month (APTD only, grandfathered)
```

### References for Metadata

```yaml
# For parameters:
reference:
  - title: "Ala. Admin. Code r. 660-2-4-.19a -- Special Needs of Applicants and Recipients"
    href: "https://admincode.legislature.state.al.us/api/chapter/660-2-4#page=24"
  - title: "Alabama DHR Monthly Statistical Report (January 2025)"
    href: "https://dhr.alabama.gov/wp-content/uploads/2025/07/STAT0125.pdf#page=5"
```

```python
# For variables:
reference = "https://admincode.legislature.state.al.us/api/chapter/660-2-4#page=24"
```

---

## Demographic Eligibility

**SSI Eligibility Required**: Person must be eligible for federal SSI (aged, blind, or disabled)

**Implementation approach:**
- [x] Use federal SSI eligibility (`is_ssi_eligible_individual` or `is_ssi_aged_blind_disabled`)
- [x] No state-specific age/disability thresholds (defers to federal SSI Title XVI)

## Immigration Eligibility

**Implementation approach:**
- [x] Use federal SSI immigration eligibility (state follows federal rules per 660-2-4-.15)
- No state-specific immigration rules for SSP

## Income/Resource Rules

**Implementation approach:**
- [x] Use federal SSI income/resource rules (per 660-2-4-.15 and 660-2-4-.26)
- [x] No additional state income disregards
- For SSI recipients: no separate income test (SSI eligibility = need determination)

---

## Special Cases and Exceptions

1. **Grandfathered populations**: Several categories are closed to new enrollment:
   - Non-SSI SUP recipients (closed since March 7, 1986)
   - Personal care recipients (closed since September 30, 1986)
   - Cerebral Palsy Treatment Center residents (closed since June 1981)
   - These are extremely small populations and may not need modeling

2. **SSI payment in suspense**: A person whose SSI payment is "in suspense" or withheld for a reason OTHER than ineligibility is still considered an SSI recipient for SUP purposes

3. **Caseload freeze**: Alabama reserves the right to freeze the caseload when funds are exhausted -- not implementable in a microsimulation model

4. **Living arrangement requirement**: The supplement is ONLY available to persons requiring specific care arrangements, not to all SSI recipients. This is the most significant limiting factor.

---

## PDFs Downloaded and Extracted

1. **Alabama Administrative Code Chapter 660-2-4** (61 pages)
   - URL: https://admincode.legislature.state.al.us/api/chapter/660-2-4
   - Saved to: /tmp/al_admin_code_660-2-4.pdf
   - Text extracted to: /tmp/al_admin_code_660-2-4.txt
   - Key pages rendered at 300 DPI: pages 24-26 (payment tables)

2. **Alabama DHR Payment Manual Section 3** (large file)
   - URL: https://dhr.alabama.gov/wp-content/uploads/2022/04/Appendix-N-Sec-3-Public-Assistance-Payment-Manual.pdf
   - Saved to: /tmp/al_dhr_payment_manual_sec3.pdf
   - Text extracted to: /tmp/al_dhr_sec3.txt

3. **Alabama DHR Monthly Statistical Report -- January 2025**
   - URL: https://dhr.alabama.gov/wp-content/uploads/2025/07/STAT0125.pdf
   - Saved to: /tmp/al_dhr_stat_0125.pdf
   - Text extracted to: /tmp/al_dhr_stat_0125.txt
   - Key pages rendered at 300 DPI: pages 5-10 (supplementation tables)

4. **Alabama DHR Monthly Statistical Report -- March 2024**
   - URL: https://dhr.alabama.gov/wp-content/uploads/2024/09/STAT0324.pdf
   - Saved to: /tmp/al_dhr_stat_0324.pdf
   - Key pages rendered at 300 DPI: pages 5-10

5. **Alabama DHR Monthly Statistical Report -- November 2023**
   - URL: https://dhr.alabama.gov/wp-content/uploads/2024/02/STAT1123.pdf
   - Saved to: /tmp/al_dhr_stat_1123.pdf

---

## Failed Fetches

1. **SSA State Assistance Programs for SSI Recipients -- Alabama (2011)**
   - URL: https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/al.html
   - Error: 403 Forbidden
   - Expected content: Comprehensive overview of Alabama's state assistance programs for SSI recipients with payment levels, eligibility rules, and program structure
   - Mitigation: Content obtained from WorkWorld mirror and web search excerpts

2. **SSA State Assistance Programs for SSI Recipients -- Alabama (2006, 2007)**
   - URLs: https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2006/al.html, .../2007/al.html
   - Error: 403 Forbidden
   - Expected content: Earlier editions of same report

3. **SSA Annual Statistical Supplement 2024, Section 7B**
   - URL: https://www.ssa.gov/policy/docs/statcomps/supplement/2024/7b.html
   - Error: 403 Forbidden
   - Expected content: SSI data by state including supplementation payments. However, since Alabama's SSP is state-administered, this report likely does NOT contain Alabama SSP data.

4. **Justia Alabama Code Title 38, Chapter 4**
   - URL: https://law.justia.com/codes/alabama/title-38/chapter-4/
   - Error: 403 Forbidden
   - Expected content: Complete statutory text for Alabama public assistance
   - Mitigation: Section 38-4-1 content obtained from web search excerpts

5. **Justia Alabama Administrative Code Chapter 660-2-4**
   - URL: https://regulations.justia.com/states/alabama/title-660/chapter-660-2-4/
   - Error: 403 Forbidden
   - Mitigation: Full chapter obtained directly from admincode.legislature.state.al.us as PDF
