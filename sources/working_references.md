# Rhode Island CCAP - Working References

## Collected Documentation

**Collected**: 2026-03-03
**Implementation Task**: Rhode Island Child Care Assistance Program (CCAP) / Child Care Development Fund (CCDF) implementation

---

## Official Program Name

**Federal Program**: Child Care and Development Fund (CCDF)
**State's Official Name**: Starting RIght Child Care Assistance Program (CCAP)
**Abbreviation**: CCAP
**Administering Agency**: Rhode Island Department of Human Services (DHS), Office of Child Care (OCC)
**Source**: R.I. Gen. Laws 42-12-23; 218-RICR-20-00-4.1.1(A)(1)

**Variable Prefix**: `ri_ccap`

---

## Program Overview

The Starting RIght Child Care Assistance Program (CCAP), adopted in 1998, provides financial assistance for authorized child care services to eligible Rhode Island families. It subsidizes the cost of child care for:
1. Rhode Island Works (RI Works / TANF) cash assistance recipients
2. Income-eligible working families
3. Families in approved education/training programs
4. Families enrolled in degree programs at RI public institutions of higher education

The program operates under 218-RICR-20-00-4 and is authorized by R.I. Gen. Laws 42-12-23 and Chapter 40-6.2 (Child Care -- State Subsidies).

---

## Eligibility Requirements

### Three Eligibility Pathways

Per 218-RICR-20-00-4.3(A), there are three pathways:

1. **RI Works CCAP** (Section 4.5): Categorical eligibility through RI Works cash assistance or Teen and Family Development (TFD) participation
2. **Income Eligibility** (Section 4.6): Working families, families in approved education/training, or TFD participants not receiving RI Works cash assistance
3. **CCAP for College** (Section 4.6.2(A)(4)): Parents enrolled in Associate's or Bachelor's degree programs at CCRI, RIC, or URI

### Income Eligibility

**Legal Citation**: 218-RICR-20-00-4.6.1(A)(1)(a)
**Quote**: "The countable income of the financial unit shall be at or below two hundred sixty-one percent (261%) of the Federal poverty level (FPL), based on family size."

- **Initial Eligibility**: Income at or below 261% FPL
- **Transitional Child Care** (Section 4.6.1(A)(1)(a)(1)): Families currently eligible whose income rises above 261% FPL may continue receiving CCAP as long as income remains below 300% FPL
- **Exit Threshold**: Income above 300% FPL -- family is no longer eligible (Section 4.6.1(A)(1)(a)(2))
- **New applicants** with income over 261% FPL are NOT eligible for Transitional Child Care (Section 4.6.1(A)(1)(a)(3))
- **Effective Date**: 261% FPL threshold effective January 1, 2025 (prior limit was 200% FPL, effective July 1, 2022)

**Implementation approach:**
- [x] Store entry threshold as FPL rate: 2.61
- [x] Store exit/transitional threshold as FPL rate: 3.00
- [x] Use `is_ccap_enrolled` or equivalent to distinguish new applicants from existing recipients for transitional eligibility

#### 2026 Income Limits by Family Size (from 2026 Co-Pay Chart, effective 02/15/2026)

These are derived from 261% FPL. The annual FPL values for 2026 are:

| Family Size | 100% FPL (Annual) | 261% FPL (Entry, Annual) | 300% FPL (Exit, Annual) |
|---|---|---|---|
| 2 | $21,640 | $56,480 | $64,920 |
| 3 | $27,320 | $71,305 | $81,960 |
| 4 | $33,000 | $86,130 | $99,000 |
| 5 | $38,680 | $100,955 | $116,040 |
| 6 | $44,360 | $115,780 | $133,080 |
| 7 | $50,040 | $130,604 | $150,120 |
| 8 | $55,720 | $145,429 | $167,160 |
| 9 | $61,400 | $160,254 | $184,200 |
| 10 | $67,080 | $175,079 | $201,240 |
| 11 | $72,760 | $189,904 | $218,280 |
| 12 | $78,440 | $204,728 | $235,320 |
| 13 | $84,120 | $219,553 | $252,360 |
| 14 | $89,800 | $234,378 | $269,400 |
| 15 | $95,480 | $249,203 | $286,440 |

**Note**: Add $5,680 for each additional person over 15.
**Source**: CCAP 2026 Family Income Co-Pay Chart, effective 02/15/2026 (https://dhs.ri.gov/media/10606/download?language=en)

**Implementation Note**: Since income limits are defined as percentage of FPL, parameters should store rates (2.61 and 3.00), not dollar amounts. Dollar amounts update automatically when FPL changes.

### Asset / Resource Limit

**Legal Citation**: 218-RICR-20-00-4.6.1(B)(1)
**Value**: $1,000,000
**Level**: Per family (financial unit)
**Type**: Assets (vehicles excluding primary, real estate excluding primary residence, cash, bank accounts, investments)
**Excluded from assets**: Educational savings accounts/plans/programs; retirement accounts/plans/programs; accounts held jointly with non-spouse non-household member (to the extent from other person's sources)
**Source**: 218-RICR-20-00-4.6.1(B)(1)-(3); also confirmed by CCDF State Plan FFY 2025-2027, Section 2.2.6

**Note**: If assets exceed $1,000,000 during the certification period, there is no impact until recertification (Section 4.6.1(B)(1)(d)).

### Child Age Requirements

**Legal Citation**: 218-RICR-20-00-4.2(A)(18) ("Dependent child") and 218-RICR-20-00-4.3.1(C)
- **Minimum age**: At least one (1) week old (regulation text says six (6) weeks per 218-RICR-20-00-4.2(A)(32), but center rates use 6 weeks)
- **Maximum age**: Below thirteen (13) years old
- **Disability exception**: Through age eighteen (18) if the child has a documented physical or mental disability
- **Turning 13 exception**: Children turning thirteen (13) during the certification period (but under age 14) may continue receiving CCAP through the end of the 24-month certification period

**Age Categories for Rate Purposes** (218-RICR-20-00-4.12(B)(2)):
- **Infant**: 6 weeks up to 18 months of age
- **Toddler**: 18 months up to 3 years of age
- **Preschool**: 3 years up to 1st grade entry (includes ALL Kindergarten children)
- **School Age**: 1st grade up to 13 years of age

**Note**: Licensed Center rates separate Infant and Toddler categories; Licensed Family and License Exempt rates combine them as "Infant/Toddler."

### Work/Activity Requirements

**Legal Citation**: 218-RICR-20-00-4.6.2

**Income-Eligible Families - Employment:**
- **Two-parent home** (Section 4.6.2(A)(1)(a)): EACH parent must be employed a minimum of an average of 20 hours per week in a month. The 20-hour requirement cannot be met by combining both parents' hours.
- **One-parent home** (Section 4.6.2(A)(1)(b)(2)): Parent must be employed a minimum of an average of 20 hours per week in a month.
- **Minimum wage**: Working parents must earn per hour an average of the greater of State or Federal minimum wage (Section 4.6.2(A)(1)(b)(2)).

**Income-Eligible Families - Training:**
- Parent must participate in approved education/training activities for minimum 20 hours per week on average in a month (Section 4.6.2(A)(3)(c)).

**Income-Eligible Families - College:**
- Enrolled in Associate's or Bachelor's degree at CCRI, RIC, or URI for minimum 7 credit hours per semester (Section 4.6.2(A)(4)(b)(1))
- College credit-based hours: 2 hours of outside work per 1 credit hour in classroom; 7 credits = 21 hours of activity, meeting the 20-hour minimum
- OR: combination of approved college credit hours + work hours totaling at least 20 hours/week (Section 4.6.2(A)(4)(b)(2))

**RI Works CCAP:**
- Must maintain signed RI Works employment plan (Section 4.5.1)
- Participate in approved plan activities

### Residency and Citizenship

**Legal Citation**: 218-RICR-20-00-4.3.1(C)

- **Residency**: Applicant parent(s) and any applicant children must be residents of Rhode Island
- **Citizenship for child**: The applicant child must be either a citizen of the United States or a "qualified immigrant"
  - Qualified immigrants include: lawful permanent residents (LPRs), refugees, asylees, trafficking victims, battered relatives meeting specific criteria
- **Citizenship for parent**: No citizenship documentation is required from the applicant parent (per DHS website)

### Child Support Cooperation

**Legal Citation**: 218-RICR-20-00-4.3.2

All families with an absent parent must cooperate with the Office of Child Support Services (OCSS) to:
- Identify the absent parent
- Establish paternity
- Obtain support payments

**Good cause exception** (Section 4.3.4): Domestic violence, rape/incest, pending adoption. Requires assessment by a domestic violence advocate.

**Consequence of non-cooperation**: Case closure (Section 4.3.3).

### Certification Period

**Legal Citation**: 218-RICR-20-00-4.2(A)(13)
- Minimum twenty-four (24) months in duration
- **Note**: The regulation text shows strikethrough from "twelve (12)" to "twenty-four (24)" indicating this was recently extended.

### Housing Insecure Families

**Legal Citation**: 218-RICR-20-00-4.5.4(B)
- Housing insecure families applying for CCAP receive a co-payment of zero ($0.00)
- This applies regardless of income level

---

## Income Calculation

### Financial Unit Definition

**Legal Citation**: 218-RICR-20-00-4.2(A)(26)
**Quote**: "Financial unit means the dependent children, including both applicant and non-applicant child(ren), and the parent(s) and the legal spouse(s) of the parent(s) who live with them in the same household."
- May also include applicant children determined to be a relative of acceptable degree
- The financial unit determines family size for income determination purposes

### Countable Income

**Legal Citation**: 218-RICR-20-00-4.2(A)(30) (definition of "Income")
**Quote**: "Income means any money, goods or services available to the financial unit used to calculate eligibility for the CCAP."

Countable income includes, but is not limited to:
1. Monetary compensation for services (gross wages, salary, commissions, work-based fees, stipends, tips, bonuses)
2. Adjusted gross income from self-employment
3. Social Security Benefits (RSDI)
4. Supplemental Security Income (SSI)
5. Dividends or interest on savings or bonds
6. Income from estates or trusts
7. Adjusted Gross Rental Income
8. Adjusted Gross Room and Board Income
9. Public assistance payments
10. Unemployment Compensation
11. Temporary Disability Insurance (TDI)
12. Workers' Compensation
13. Government civilian employee or military retirement; Private pensions or annuities
14. Cash payouts for waiving employer sponsored health insurance
15. Adoption subsidies
16. Alimony
17. Child support payments
18. Regular contributions from persons not living in the household
19. Royalties
20. Strike Benefits
21. Trade Readjustment Allowance
22. VA Compensation Payments, VA Educational Benefits, Spousal/Dependent Allowances and Military Allotments
23. Payments to volunteers under Americorps (but NOT Americorps/VISTA)
24. Foster care payments from DCYF (when child IS included in the assistance unit)
25. In-Kind Assistance
26. Non-citizen Sponsor Income (sponsor + sponsor's spouse)

### Excluded Income

**Legal Citation**: 218-RICR-20-00-4.2(A)(24)

Excluded income includes, but is not limited to:
1. Value of USDA donated foods
2. Payments under Title II of the Uniform Relocation Assistance and Real Property Acquisition Policies Act of 1970
3. Value of certain assistance to undergraduate students (grants/loans for educational purposes)
4. Per capita payments to Indian tribe members under specified public laws
5. Benefits under Title VII, Nutrition Program for the Elderly (Older Americans Act)
6. Payments to individual volunteers (foster grandparents, senior health aides, senior companions, SCORE, ACE, and Title II/III of Domestic Volunteer Service Act)
7. Value of supplemental food assistance under Child Nutrition Act
8. Payments of Experimental Housing Allowance Program
9. Receipts to members of certain Indian tribes per Pub. Law 94-114
10. Tax-exempt portions of Alaska Native Claims Settlement Act payments
11. Foster care payments from DCYF (when child is NOT in the assistance unit)
12. Value of food assistance benefits
13. Value of government rent or housing subsidies
14. Home energy assistance (state/federal/nonprofit)
15. Income from college work study programs
16. Earned income of a dependent child included in the financial unit
17. Stipends, earned income, and reimbursements through WIOA
18. EITC refunds and advance payment of EITC
19. Loans and grants used for non-living-cost educational purposes
20. PASS program or IRWE program monies
21. Income of the parents with whom a teen parent resides
22. Section 8 Utility Payment
23. Veterans Aid and Attendant Allowances
24. Payments to Americorps/VISTA volunteers (but NOT regular Americorps)
25. Rhode Island Works (RIW) cash assistance payments
26. Veteran's Disability Pension payments from military service

### Income Budgeting Method

**Legal Citation**: 218-RICR-20-00-4.6.1(A)(1)(c)

- **Prospective budgeting** is used
- Eligibility based on knowledge and reasonable expectation of income for the month a payment is authorized
- **Weekly to monthly conversion**: Weekly income is converted using the **4.3333 weeks per month** conversion factor (Section 4.6.1(A)(1)(c)(1))
- **Self-employment income**: Calculated per RI Works Program Rules and Regulations, Section 2.15.4

### Income Verification

- Based on income for the 30-day period immediately preceding the application date
- Used to project anticipated income during the eligibility period
- If prior 30 days not representative (e.g., seasonal work), agency may use the most recent comparable season

---

## Co-Payment / Family Share

### Co-Payment Schedule

**Legal Citation**: 218-RICR-20-00-4.6.1(C)(1)
**Quote**: "Eligible families with countable income above one hundred percent (100%) of the FPL shall pay a share of the expense for the child care services."

The family share is assessed as a **percentage of gross countable income**:

| Level | FPL Range | Co-Payment Rate | Applies To |
|---|---|---|---|
| Level 0 | At or below 100% FPL | 0% (No Family Share) | New applicants and ongoing |
| Level 1 | Above 100% up to and including 125% FPL | 2% of gross countable income | New applicants and ongoing |
| Level 2 | Above 125% up to and including 150% FPL | 5% of gross countable income | New applicants and ongoing |
| Level 3 | Above 150% up to and including 261% FPL | 7% of gross countable income | New applicants and ongoing |
| Level 4 | Above 261% up to and including 300% FPL | 7% of gross countable income | **Transitional Child Care only** (at recertification) |

**Source**: 218-RICR-20-00-4.6.1(C)(1)(c); confirmed by 2026 Co-Pay Chart (https://dhs.ri.gov/media/10606/download?language=en)

### Co-Payment Rules

1. **One co-payment per family** regardless of number of eligible children enrolled (Section 4.6.1(C)(2))
2. **Assigned to youngest child**: The family share is assigned to the youngest eligible child enrolled in care (i.e., the child receiving authorized services at the highest rate) (Section 4.6.1(C)(2)(a))
3. **Distribution among providers**: Only distributed among providers when total family share exceeds the rate paid for the youngest eligible child enrolled (Section 4.6.1(C)(2)(b))
4. **Recalculation**: Recalculated when family reports a change or at recertification; only adjusted downward during the certification period (Section 4.6.1(C)(3))
5. **Maximum federal cap**: 7% of family income (per CCDF rules, 45 CFR 98; confirmed in CCDF State Plan Section 3.1.1)

### RI Works Co-Payments

**Legal Citation**: 218-RICR-20-00-4.5.4

- RI Works recipients receiving Child Care Assistance as a supportive service: **$0.00** co-payment
- Loco-parentis applicants receiving RI Works cash on behalf of child but not included in RI Works payment: assessed co-payment per the Family Cost Sharing Requirement
- Housing insecure families: **$0.00** co-payment

---

## Provider Payment Rates

### Rate Structure

**Legal Citation**: 218-RICR-20-00-4.12; R.I. Gen. Laws 40-6.2-1.1

Weekly reimbursement is paid based on:
- **Provider type**: Licensed Center, Licensed Family, License Exempt
- **QRIS BrightStars rating**: Star rating 1 through 5 (4 steps for License Exempt)
- **Time authorized and enrolled**: Full-time, Three-quarter time, Half-time, Quarter-time
- **Age of child**: Infant, Toddler, Preschool, School Age

### Time Authorization Categories (218-RICR-20-00-4.12(B)(1))

| Category | Hours per Week |
|---|---|
| Full-time (FT) | 30 or more hours |
| Three-quarter time (3QT) | 20-29 hours |
| Half-time (HT) | 10-19 hours |
| Quarter-time (QT) | 0-9 hours |

### Licensed Center Weekly Rates (Effective July 1, 2025)

**Source**: https://dhs.ri.gov/media/9356/download?language=en

#### Full Time (30+ hours/week)

| Star Rating | Infant | Toddler | Preschool | School Age |
|---|---|---|---|---|
| 1 | $334.00 | $278.00 | $236.00 | $210.00 |
| 2 | $341.00 | $284.00 | $247.00 | $215.00 |
| 3 | $355.00 | $296.00 | $255.00 | $231.00 |
| 4 | $364.00 | $303.00 | $263.00 | $250.00 |
| 5 | $378.00 | $315.00 | $273.00 | $263.00 |

#### Three Quarter Time (20-29 hours/week)

| Star Rating | Infant | Toddler | Preschool | School Age |
|---|---|---|---|---|
| 1 | $250.50 | $208.50 | $177.00 | $157.50 |
| 2 | $255.75 | $213.00 | $185.25 | $161.25 |
| 3 | $266.25 | $222.00 | $191.25 | $173.25 |
| 4 | $273.00 | $227.25 | $197.25 | $187.50 |
| 5 | $283.50 | $236.25 | $204.75 | $197.25 |

#### Half Time (10-19 hours/week)

| Star Rating | Infant | Toddler | Preschool | School Age |
|---|---|---|---|---|
| 1 | $167.00 | $139.00 | $118.00 | $105.00 |
| 2 | $170.50 | $142.00 | $123.50 | $107.50 |
| 3 | $177.50 | $148.00 | $127.50 | $115.50 |
| 4 | $182.00 | $151.50 | $131.50 | $125.00 |
| 5 | $189.00 | $157.50 | $136.50 | $131.50 |

#### Quarter Time (0-9 hours/week)

| Star Rating | Infant | Toddler | Preschool | School Age |
|---|---|---|---|---|
| 1 | $83.50 | $69.50 | $59.00 | $52.50 |
| 2 | $85.25 | $71.00 | $61.75 | $53.75 |
| 3 | $88.75 | $74.00 | $63.75 | $57.75 |
| 4 | $91.00 | $75.75 | $65.75 | $62.50 |
| 5 | $94.50 | $78.75 | $68.25 | $65.75 |

### Licensed Family Child Care Weekly Rates (Effective July 1, 2024)

**Source**: https://dhs.ri.gov/media/7481/download?language=en

**Note**: Family child care combines Infant/Toddler into one category.

#### Full Time (30+ hours/week)

| Star Rating | Infant/Toddler | Preschool | School Age |
|---|---|---|---|
| 1 | $262.66 | $220.63 | $194.37 |
| 2 | $266.86 | $231.14 | $199.62 |
| 3 | $270.02 | $239.54 | $215.38 |
| 4 | $273.16 | $251.10 | $236.40 |
| 5 | $276.31 | $262.66 | $246.90 |

#### Three Quarter Time (20-29 hours/week)

| Star Rating | Infant/Toddler | Preschool | School Age |
|---|---|---|---|
| 1 | $196.99 | $165.47 | $145.78 |
| 2 | $200.14 | $173.35 | $149.71 |
| 3 | $202.51 | $179.66 | $161.54 |
| 4 | $204.87 | $188.33 | $177.30 |
| 5 | $207.23 | $196.99 | $185.18 |

#### Half Time (10-19 hours/week)

| Star Rating | Infant/Toddler | Preschool | School Age |
|---|---|---|---|
| 1 | $131.33 | $110.32 | $97.19 |
| 2 | $133.43 | $115.57 | $99.81 |
| 3 | $135.01 | $119.77 | $107.69 |
| 4 | $136.58 | $125.55 | $118.20 |
| 5 | $138.15 | $131.33 | $123.45 |

#### Quarter Time (0-9 hours/week)

| Star Rating | Infant/Toddler | Preschool | School Age |
|---|---|---|---|
| 1 | $65.66 | $55.16 | $48.59 |
| 2 | $66.71 | $57.78 | $49.90 |
| 3 | $67.50 | $59.89 | $53.85 |
| 4 | $68.29 | $62.78 | $59.10 |
| 5 | $69.08 | $65.66 | $61.73 |

### License Exempt Weekly Rates (Effective January 1, 2022)

**Source**: https://dhs.ri.gov/media/3556/download?language=en

**Note**: License Exempt providers use 4 "Step" ratings (not 5 Star ratings).

#### Full Time (30+ hours/week)

| Step Rating | Infant/Toddler | Preschool | School Age |
|---|---|---|---|
| 1 | $100.96 | $59.91 | $58.80 |
| 2 | $101.95 | $60.49 | $59.38 |
| 3 | $102.94 | $61.09 | $59.97 |
| 4 | $103.96 | $61.68 | $60.53 |

#### Three Quarter Time (20-29 hours/week)

| Step Rating | Infant/Toddler | Preschool | School Age |
|---|---|---|---|
| 1 | $75.72 | $44.93 | $44.10 |
| 2 | $76.46 | $45.37 | $44.53 |
| 3 | $77.21 | $45.83 | $44.97 |
| 4 | $77.96 | $46.26 | $45.40 |

#### Half Time (10-19 hours/week)

| Step Rating | Infant/Toddler | Preschool | School Age |
|---|---|---|---|
| 1 | $50.48 | $29.95 | $29.40 |
| 2 | $50.98 | $30.26 | $29.69 |
| 3 | $51.48 | $30.54 | $29.98 |
| 4 | $51.98 | $30.84 | $30.28 |

#### Quarter Time (0-9 hours/week)

| Step Rating | Infant/Toddler | Preschool | School Age |
|---|---|---|---|
| 1 | $25.24 | $14.71 | $14.70 |
| 2 | $25.49 | $15.11 | $14.85 |
| 3 | $25.74 | $15.28 | $14.99 |
| 4 | $25.98 | $15.42 | $15.13 |

### Tiered Reimbursement Basis

**Legal Citation**: R.I. Gen. Laws 40-6.2-1.1

Per statute, the base reimbursement rates are determined by the 75th percentile of market rates from triennial surveys (conducted by RI Dept of Labor and Training). Rates are tiered by QRIS BrightStars quality rating, with higher-rated providers receiving higher reimbursement. The specific tier percentages above the base rate are defined in statute for infant/toddler and preschool care.

---

## Benefit Calculation

### How the Subsidy Works

The CCAP benefit is calculated as:

```
CCAP Allowable Child Care Expense = Provider Rate - Family Share (Co-Payment)
```

Per 218-RICR-20-00-4.2(A)(1):
**Quote**: "Allowable child care expense means the total cost of the CCAP authorized child care services paid by the DHS to an approved provider, after deducting the amount the family is required to pay the provider as its share of the cost (or family share) for authorized services."

### Step-by-Step Benefit Calculation

1. **Determine eligibility**: Income at or below 261% FPL (or 300% FPL for transitional), meets activity requirements, child meets age requirements, meets residency/citizenship, cooperating with child support
2. **Determine family share level**: Based on gross countable income as % of FPL:
   - Level 0 (at or below 100% FPL): 0%
   - Level 1 (>100% to 125% FPL): 2%
   - Level 2 (>125% to 150% FPL): 5%
   - Level 3 (>150% to 261% FPL): 7%
   - Level 4 (>261% to 300% FPL, transitional only): 7%
3. **Calculate family share amount**: Family Share = Co-Payment Rate x Gross Countable Monthly Income
4. **One co-payment per family**: Regardless of number of children
5. **Assign to youngest child**: Family share assigned to youngest eligible child's provider
6. **DHS pays**: Provider rate minus the family share for each child

### Key Implementation Notes for Benefit Calculation

- The benefit is a **provider-facing subsidy** (DHS pays provider, not family)
- Family share is a **single monthly amount** per family, not per child
- The family share is based on **monthly** gross countable income
- For modeling purposes, the subsidy per family = sum of (provider weekly rates x time authorization) across all eligible children - family share
- Provider rates are **weekly**, so monthly calculation = weekly rate x 4.3333 (or as applicable)

---

## Priority Groups

**Legal Citation**: 218-RICR-20-00-4.3.1(C)

Per the CCDF State Plan, Rhode Island prioritizes:
1. Children receiving protective services
2. Children experiencing homelessness
3. Children in families receiving RI Works cash assistance
4. Children of families with very low income (below poverty level)

---

## Limitations and Exclusions

### School-Age Limitations

**Legal Citation**: 218-RICR-20-00-4.7.2
- School-age children cannot receive CCAP during school hours (approximately 9 AM - 2 PM)
- CCAP authorized for before/after school and school vacation periods

### Absence Limits

- Maximum 2 consecutive weeks of paid absence per year (licensed providers only)
- License-exempt providers receive payment only for services actually rendered

### Self-Employed Child Care Providers

A parent who is self-employed as a child care provider cannot receive CCAP payment for care of their own child or another child in the same household (Section 4.6.3(A)(1)).

---

## CCAP for Child Care Staff Pilot

**Source**: https://dhs.ri.gov/programs-and-services/child-care/child-care-providers/CCAP-for-Child-Care-Staff

A separate pilot program (218-RICR-20-00-13) makes child care free for child care educators and staff earning up to 300% FPL. This is governed by separate regulations and is NOT the same as the standard CCAP.

---

## Income Eligibility History

| Effective Date | Initial Entry Limit | Transitional Exit Limit | Source |
|---|---|---|---|
| Pre-2022 | 180% FPL | 225% FPL | 218-RICR-20-00-4 (prior version) |
| 2022-07-01 | 200% FPL | 300% FPL | FY2023 State Budget; CCDF State Plan 2025-2027, Section 2.2.4(d) |
| 2025-01-01 | 261% FPL | 300% FPL | FY25 State Budget; DHS press release; 218-RICR-20-00-4.6.1(A)(1)(a) (amended) |

### Co-Payment Level History

The co-payment structure from the regulation (pre-amendment) used different FPL ranges:
- Prior regulation had: Level 3 at 150%-180%, Level 4 at 180%-200%, Level 5 at 200%-225%
- Current regulation (post-261% amendment) consolidated to: Level 3 at 150%-261%, Level 4 (transitional) at 261%-300%

---

## Regulatory Sources

### Primary Sources

1. **218-RICR-20-00-4 - Child Care Assistance Program Rules and Regulations**
   - Full regulation text (78 pages)
   - URL: https://dhs.ri.gov/media/9236/download?language=en
   - Also at: https://rules.sos.ri.gov/Regulations/part/218-20-00-4
   - Status: Active Rule (most recent amendments effective 07/23/2025)
   - Cornell Law mirror: https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3

2. **R.I. Gen. Laws Chapter 40-6.2 - Child Care -- State Subsidies**
   - URL: https://law.justia.com/codes/rhode-island/title-40/chapter-40-6-2/
   - Section 40-6.2-1.1 (Rates established): https://law.justia.com/codes/rhode-island/title-40/chapter-40-6-2/section-40-6-2-1-1/

3. **R.I. Gen. Laws 42-12-23 - DHS Child Care Authority**
   - Designates DHS as principal agency for child care planning and coordination

4. **45 CFR Part 98 - Child Care and Development Fund (Federal)**
   - URL: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-98
   - Section 98.20 - Child eligibility: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-98/subpart-C/section-98.20
   - Federal maximum income: 85% SMI
   - Federal maximum asset limit: $1,000,000
   - Federal maximum co-payment cap: 7% of family income
   - Federal minimum age: Under 13 (up to 19 for disabled/court-supervised)

### CCDF State Plan

5. **CCDF State Plan FFY 2025-2027 (Rhode Island)**
   - URL: https://dhs.ri.gov/media/7311/download?language=en
   - Also at ACF: https://acf.gov/occ/form/approved-ccdf-plans-fy-2025-2027
   - Period: 10/01/2024 to 9/30/2027
   - OMB Control No: 0970-0114
   - Key sections: 2.2.4 (income limits), 2.2.6 (asset limit), 2.2.7 (additional eligibility), 3.1 (co-payments)
   - **Note**: Plan was written when entry limit was 200% FPL; regulation has since been amended to 261% FPL

### Co-Payment and Rate Charts

6. **CCAP 2026 Family Income Co-Pay Chart** (effective 02/15/2026)
   - URL: https://dhs.ri.gov/media/10606/download?language=en
   - Contains: Annual and monthly income thresholds by family size (2-15+), FPL percentages, co-share amounts

7. **Licensed Center Child Care Weekly Rates** (effective July 1, 2025)
   - URL: https://dhs.ri.gov/media/9356/download?language=en

8. **Licensed Family Child Care Weekly Rates** (effective July 1, 2024)
   - URL: https://dhs.ri.gov/media/7481/download?language=en

9. **License Exempt Child Care Weekly Rates** (effective January 1, 2022)
   - URL: https://dhs.ri.gov/media/3556/download?language=en

### Program Information

10. **DHS CCAP Eligibility Page**
    - URL: https://dhs.ri.gov/programs-and-services/child-care/child-care-assistance-program-ccap/ccap-family-eligibility-how

11. **DHS CCAP Provider Rates Page**
    - URL: https://dhs.ri.gov/programs-and-services/child-care/child-care-assistance-program-ccap/ccap-provider-rates-financial

12. **DHS Press Release - FY25 Budget Income Expansion**
    - URL: https://dhs.ri.gov/press-releases/more-ri-households-become-eligible-child-care-assistance-through-fy25-budget
    - Details the change from 200% FPL to 261% FPL effective January 1, 2025

13. **ACF Family Co-Payments by State (January 2025)**
    - URL: https://acf.gov/sites/default/files/documents/occ/CCDF-Family-Co-Payments-by-State.pdf

14. **ACF Family Income Eligibility Levels by State (January 2025)**
    - URL: https://acf.gov/sites/default/files/documents/occ/CCDF-Family-Income-Eligibility-Levels-by-State.pdf

15. **Economic Progress Institute CCAP Summary**
    - URL: https://economicprogressri.org/resources/child-care-assistance-program
    - Third-party summary (use for verification only, not as primary source)

### References for Parameters

```yaml
# For eligibility income limits:
reference:
  - title: 218-RICR-20-00-4.6.1(A)(1)(a)
    href: https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3
  - title: CCAP 2026 Family Income Co-Pay Chart
    href: https://dhs.ri.gov/media/10606/download?language=en

# For co-payment rates:
reference:
  - title: 218-RICR-20-00-4.6.1(C)(1)(c)
    href: https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3
  - title: CCAP 2026 Family Income Co-Pay Chart
    href: https://dhs.ri.gov/media/10606/download?language=en

# For asset limit:
reference:
  - title: 218-RICR-20-00-4.6.1(B)(1)
    href: https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3
  - title: CCDF State Plan FFY 2025-2027, Section 2.2.6
    href: https://dhs.ri.gov/media/7311/download?language=en#page=25

# For provider rates (licensed center):
reference:
  - title: R.I. Gen. Laws 40-6.2-1.1
    href: https://law.justia.com/codes/rhode-island/title-40/chapter-40-6-2/section-40-6-2-1-1/
  - title: CCAP Licensed Center Child Care Weekly Rates, July 2025
    href: https://dhs.ri.gov/media/9356/download?language=en

# For child age thresholds:
reference:
  - title: 218-RICR-20-00-4.2(A)(18)
    href: https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.2
  - title: 218-RICR-20-00-4.12(B)(2)
    href: https://dhs.ri.gov/media/9236/download?language=en#page=76
```

```python
# For variables:
reference = "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3"
# Or for multiple:
reference = (
    "https://www.law.cornell.edu/regulations/rhode-island/218-RICR-20-00-4.3",
    "https://dhs.ri.gov/media/10606/download?language=en",
)
```

---

## Implementation Considerations

### Suggested Variable Structure

```
ri/dhs/ccap/
  eligibility/
    ri_ccap_child_eligible.py          # Person-level: age, citizenship, residency
    ri_ccap_income_eligible.py          # SPMUnit-level: income vs 261% FPL
    ri_ccap_eligible.py                 # SPMUnit-level: combines all eligibility checks
  income/
    ri_ccap_countable_income.py         # SPMUnit-level: gross countable income
  ri_ccap_family_share.py              # SPMUnit-level: co-payment amount
  ri_ccap.py                           # SPMUnit-level: total subsidy amount
```

### Suggested Parameter Structure

```
ri/dhs/ccap/
  eligibility/
    income_limit/
      entry_rate.yaml                  # 2.61 (261% FPL)
      transitional_rate.yaml           # 3.00 (300% FPL)
    asset_limit.yaml                   # 1_000_000
    child_age_limit.yaml               # 13
    disabled_child_age_limit.yaml      # 19 (or 18 per regulation text "through age eighteen")
    min_work_hours.yaml                # 20
  co_payment/
    rate.yaml                          # Bracket parameter by FPL percentage
  provider_rates/
    licensed_center/...                 # By star rating, age, and time authorization
    licensed_family/...
    license_exempt/...
```

### Key Implementation Decisions

1. **Income definition**: Uses gross countable income (not net). No earned income disregards or deductions -- the full list of countable/excluded items applies.

2. **FPL-based thresholds**: Entry limit (261% FPL) and transitional exit limit (300% FPL) should be stored as rates, not dollar amounts. The FPL base values update annually.

3. **Co-payment as FPL-bracket scale**: The co-payment percentage is a step function of income as percentage of FPL. This maps naturally to a bracket parameter.

4. **Provider rates**: These are complex multi-dimensional parameters (provider type x star rating x age category x time authorization). Consider whether all dimensions need to be parameterized or if a simplified approach is appropriate for initial implementation.

5. **Transitional eligibility**: The entry vs. exit threshold distinction requires knowing whether a family is a new applicant or currently enrolled. Similar pattern to `is_tanf_enrolled` -- could use `is_ccap_enrolled` or equivalent.

6. **Family size**: Determined by the "financial unit" definition, which aligns roughly with the SPMUnit concept (dependent children + parents + legal spouses in household).

### Existing Reference Implementation

Colorado CCAP implementation in the codebase:
- Variables: `/policyengine_us/variables/gov/states/co/ccap/`
- Parameters: `/policyengine_us/parameters/gov/states/co/ccap/`
- Tests: `/policyengine_us/tests/policy/baseline/gov/states/co/ccap/`

Colorado uses a similar structure with entry/re-determination separation, FPG and SMI eligibility checks, and parent fee calculations. Rhode Island's model is simpler (FPL-only, no SMI check for entry, flat co-payment percentages rather than a dollar-amount fee schedule).

---

## PDFs Successfully Extracted

All key PDFs were downloaded and extracted:

1. **218-RICR-20-00-4 Regulations** (78 pages) - `/tmp/ri_ccap_regs.pdf` -> `/tmp/ri_ccap_regs.txt`
2. **CCAP Program Info Flyer** (1 page) - `/tmp/ri_ccap_info.pdf` -> `/tmp/ri_ccap_info.txt`
3. **CCAP 2026 Co-Pay Chart** (2 pages) - `/tmp/ri_ccap_copay_2026.pdf` -> `/tmp/ri_ccap_copay_2026.txt`
4. **CCDF State Plan FFY 2025-2027** (~180 pages) - `/tmp/ri_ccdf_plan.pdf` -> `/tmp/ri_ccdf_plan.txt`
5. **Licensed Center Rates July 2025** (1 page) - `/tmp/ri_center_rates.pdf` -> `/tmp/ri_center_rates.txt`
6. **Licensed Family Rates July 2024** (1 page) - `/tmp/ri_family_rates.pdf` -> `/tmp/ri_family_rates.txt`
7. **License Exempt Rates January 2022** (1 page) - `/tmp/ri_exempt_rates.pdf` -> `/tmp/ri_exempt_rates.txt`
8. **ACF Co-Payments by State January 2025** - `/tmp/ccdf_copay_states.pdf` -> `/tmp/ccdf_copay_states.txt`
9. **ACF Income Eligibility Levels by State January 2025** - `/tmp/ccdf_income_states.pdf` -> `/tmp/ccdf_income_states.txt`
