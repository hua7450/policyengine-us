# Virginia Child Care Subsidy Program (CCSP) - Working References

## Program Overview

Virginia's Child Care Subsidy Program (CCSP) assists eligible low-income families with
child care costs for children under age 13 (or under 18 for special needs/court supervision).
The program is administered by the Virginia Department of Education (VDOE) and the
Virginia Department of Social Services (VDSS) through local departments of social services (LDSS).

**Official program name**: Child Care Subsidy Program (CCSP)
**Administering agencies**: VDOE (oversight) + VDSS/LDSS (administration)
**Federal authority**: Child Care and Development Block Grant (CCDBG) Act of 2014
**State regulations**: 8VAC20-790 (Child Care Program)
**Guidance manual**: Child Care Subsidy Program Guidance Manual (effective August 3, 2023)

## Primary Sources

### 1. Child Care Subsidy Program Guidance Manual (RIS copy)
- **URL**: https://ris.dls.virginia.gov/uploads/22VAC40/dibr/VDOE%20Child%20Care%20Program%20Guidance%20Manual%205.3.2023-20240822104447.pdf
- **Title**: Child Care Subsidy Program Guidance Manual (Revised, Effective August 3, 2023)
- **Pages**: 199
- **Downloaded to**: /tmp/va-ccsp-guidance-ris.pdf (text: /tmp/va-ccsp-guidance-ris.txt)
- **Key sections**:
  - Section 2: Program Categories (TANF, SNAP E&T, Transitional, Head Start Wrap-Around, Fee) — pp. 22-36 (#page=22)
  - Section 3.3: Non-Financial Eligibility Requirements — pp. 48-54 (#page=48)
  - Section 3.4: Income and Assets Eligibility Requirements — pp. 56-62 (#page=56)
  - Section 3.5: Copayments — pp. 63-64 (#page=63)
  - Section 3.13: Authorization (age ranges, rates) — pp. 80-86 (#page=80)
  - Section 3.14: Payments (MRR) — pp. 86-90 (#page=86)
  - Appendix A: State Income Eligibility Scale — p. 136 (#page=136)
  - Appendix B: Per-Child Copayment Scale — pp. 137-138 (#page=137)
  - Appendix Z: Metropolitan Statistical Area Groupings — p. 197 (#page=197)
- **Status**: SUCCESSFULLY DOWNLOADED AND EXTRACTED

### 2. Virginia Administrative Code 8VAC20-790 (Current Regulations)
- **URL**: https://law.lis.virginia.gov/admincode/title8/agency20/chapter790/
- **Key sections**:
  - 8VAC20-790-10: Definitions — https://law.lis.virginia.gov/admincode/title8/agency20/chapter790/section10/
  - 8VAC20-790-20: Families and children to be served — https://law.lis.virginia.gov/admincode/title8/agency20/chapter790/section20/
  - 8VAC20-790-30: Program categories — https://law.lis.virginia.gov/admincode/title8/agency20/chapter790/section30/
  - 8VAC20-790-40: Case management (eligibility, income, copay) — https://law.lis.virginia.gov/admincode/title8/agency20/chapter790/section40/
- **Status**: SUCCESSFULLY FETCHED (all sections)
- **Note**: Regulations were amended effective November 19, 2025 (Vol. 42 Iss. 5) to implement new copayment structure

### 3. VECF Budget Language Summary (Copayments, Work Requirements, Attendance)
- **URL**: https://vecf.org/wp-content/uploads/2024/09/Budget-Language-Referral-Summary-for-ECCE-Commission.pdf
- **Pages**: 6
- **Downloaded to**: /tmp/va-vecf-budget.txt
- **Key data**:
  - Current copayment scale (in effect as of Jan 1, 2023):
    - 0-100% FPG: $0/month per child
    - 101-200% FPG: $60/month per child
    - 201-300% FPG: $120/month per child
    - 301% FPG - 85% SMI: $180/month per child
  - Max 3 children assessed copayments (max family copay: $540/month)
  - Family copayments capped at 7% of gross countable income
  - Copayments generate ~$14.4M (2.5% of $582M total CCSP cost for birth-5)
- **Status**: SUCCESSFULLY DOWNLOADED AND EXTRACTED

### 4. Budget Amendment HB30 Item 126 #2h (FY2026 enacted provisions)
- **URL**: https://budget.lis.virginia.gov/amendment/2026/1/HB30/Introduced/CA/126/2h
- **Key data** (NEW copayment structure, effective ~July/August 2025):
  - Below 100% FPL: $5/month per child
  - All other families: up to 5% of annual income
  - No family pays more than 5% of income
  - Job search limited to 90 days with one extension for extraordinary circumstances
- **Status**: SUCCESSFULLY FETCHED

### 5. Regulatory Update: Vol. 42 Iss. 5 — 8VAC20-790 Final Regulation
- **URL**: https://register.dls.virginia.gov/details.aspx?id=11939
- **Effective date**: November 19, 2025
- **Changes**: Implements new 5% copayment cap, $5/child minimum, 90-day job search limit
- **Authority**: Item 125.10 of Chapter 725 of the 2025 Acts of Assembly; §§ 22.1-16 and 22.1-289.046
- **Status**: SUCCESSFULLY FETCHED

### 6. WHRO News: Virginia Families Set to Pay More for CCSP
- **URL**: https://www.whro.org/virginia-government/2025-02-10/virginia-families-set-to-pay-more-for-child-care-subsidy-program
- **Key context**: Senate proposed 7%, House proposed 5%, final enacted = 5%
- **Status**: SUCCESSFULLY FETCHED

## Failed Fetches

### childcare.virginia.gov (ALL pages blocked - 403)
The official childcare.virginia.gov site blocks all automated access (returns 403 or redirects to HTML block page). The following documents could NOT be retrieved:
1. **Family Eligibility Document (Oct 2024)**: https://www.childcare.virginia.gov/home/showpublisheddocument/57736/638633886494370000
   - Likely contains: updated income eligibility tables, FPL/SMI thresholds for 2024
2. **Copayment Scale (Effective July 1, 2025)**: https://www.childcare.virginia.gov/home/showpublisheddocument/62604/638864381965000000
   - Likely contains: the NEW copayment schedule with 5% structure
3. **Updated Copayment Scale (newer URL)**: https://www.childcare.virginia.gov/home/showpublisheddocument/65775/638937831784030000
   - Likely contains: final copayment scale after full implementation
4. **Subsidy Program Guidance Manual page**: https://www.childcare.virginia.gov/reports-resources/administrative-program-manuals-reports-and-data/subsidy-program-guidance-manual
   - Likely contains: links to updated manual chapters
5. **Paying for Child Care page**: https://www.childcare.virginia.gov/families/paying-for-child-care
   - Likely contains: current copay info, rate sheets, income guidelines

### dss.virginia.gov (SSL certificate error)
- **URL**: https://www.dss.virginia.gov/family/cc/assistance.cgi/1000
- **Error**: unable to verify the first certificate
- **URL**: https://www.dss.virginia.gov/files/division/cc/approved_subsidy_vendors/forms/Child_Care_Subsidy_Guidance_Manuel.pdf
- **Error**: unable to verify the first certificate

### ACF Federal Income Eligibility PDF (403)
- **URL**: https://acf.gov/sites/default/files/documents/occ/CCDF-Family-Income-Eligibility-Levels-by-State.pdf
- Likely contains: Virginia's CCDF income eligibility levels by family size

## Program Details Extracted

### Eligibility Requirements

#### Non-Financial Requirements
1. **Child age**: Under 13, or under 18 if physically/mentally incapable of self-care or under court supervision
2. **Citizenship**: Child must be US citizen or qualified immigrant (parent citizenship not verified)
3. **Immunization**: Per State Board of Health requirements (exemptions available)
4. **Residency**: Family must reside in the locality where application is made
5. **Parent age**: Applicant must be at least 18 (emancipated minors excepted)
6. **School attendance**: No subsidy during hours public education is available
7. **Activity test**: Must have need for child care to support:
   - Full-time or part-time employment (including work from home)
   - Education or training leading to employment (up to bachelor's degree)
   - Job search (limited to 90 days with one extension)
   - Assigned VIEW or SNAP E&T activity
   - Child protective services
8. **Two-parent household**: Must document good cause why one parent cannot provide care
9. **Family day home exclusion**: Owner/operator cannot receive subsidy for own child cared for at home
10. **Asset limit**: Family assets cannot exceed $1 million (self-certified, no verification required)

#### Income Eligibility
- **Initial eligibility**: Income must not exceed the percentage of FPG for the locality group (Group I: 150% FPG, Group II: 160% FPG, Group III: 185% FPG)
- **Families with child age 5 or younger (not in kindergarten)**: Income must not exceed 85% of State Median Income (regardless of locality group)
- **Non-financially-responsible applicants**: Income limit is 250% FPG or 85% SMI (with child 5 or under)
- **Exit limit (at redetermination)**: 85% of State Median Income
- **TANF recipients**: Automatically income-eligible (no income determination)
- **Medicaid/WIC recipients**: Automatically satisfy income requirements
- **Eligibility period**: 12 months minimum

#### Countable Income
- All gross earned and unearned income of the family unit
- Self-employment: net income (gross minus verified business expenses)
- Child support: counted as unearned income of the child
- Contract income: prorated over contract period

#### Disregarded Income (30 categories)
1. Supplemental Security Income (SSI)
2. TANF benefits
3. Transitional payments ($50/month to former VIEW participants)
4. Diversionary Assistance payments
5. General Relief benefits
6. SNAP benefits
7. USDA donated food
8. Title VII Nutrition Program for the Elderly
9. Child Nutrition Act / National School Lunch Act benefits
10. Earnings of a child under age 18
11. Earned Income Tax Credit (EITC)
12. All lump sum payments
13. Scholarships/loans/grants for education (except child care portion)
14. AmeriCorps volunteer payments
15. Tax refunds
16. Monetary gifts for one-time/annual occasions
17. Vendor payments by non-financially responsible persons (unless in lieu of wages)
18. Loans and borrowed money
19. Proceeds from sale of property (unless business)
20. Earnings under $25/month
21. Capital gains
22. Withdrawals of bank deposits
23. GI Bill benefits
24. Reimbursements (e.g., mileage)
25. Foreign government restitution to Holocaust survivors
26. Agent Orange Settlement payments
27. Vietnam Veterans children monetary benefits (38 USC 1823(c))
28. Temporary census taker earnings

#### Disregarded Deductions
1. Garnished wages
2. Basic Allowance for Housing (BAH) for military on base
3. Clothing Maintenance Allowance for military
4. Child support paid to another household

#### Family Unit Definition
Includes:
- Parents (biological, adoptive, step, legal guardians, in loco parentis, cohabitants)
- All parents' children under 18
- Spouses of adults standing in loco parentis
- Temporarily absent members (unless >60 days, except active-duty military)

### Copayment Structure

#### Current Scale (effective January 1, 2023 per guidance manual Appendix B)
| Income Threshold | Monthly Fee per Child |
|---|---|
| 0-100% FPG | $0 |
| 101-200% FPG | $60 |
| 201-300% FPG | $120 |
| 301% FPG - 85% SMI | $180 |

- Maximum 3 children assessed copayments
- Total family copayment capped at 7% of gross countable income
- TANF recipients exempt from copayments

#### NEW Scale (effective July 1, 2025 per budget/regulations)
| Income Threshold | Monthly Copayment |
|---|---|
| Below 100% FPL | $5/month per child |
| All other eligible families | Up to 5% of annual income |

- No family pays more than 5% of income
- Regulation effective November 19, 2025 (8VAC20-790 amendment)

### Income Eligibility Scale (Appendix A, based on 2023 FPG and SMI)

| Family Size | Annual FPG | 100% FPG (monthly) | Group I 150% | Group II 160% | Group III 185% | 250% FPG | Exit Limit 85% SMI (monthly) | Exit Limit 85% SMI (annual) |
|---|---|---|---|---|---|---|---|---|
| 1 | $13,590 | $1,133 | $1,700 | $1,813 | $2,097 | $2,833 | $4,201 | $50,424 |
| 2 | $18,310 | $1,526 | $2,289 | $2,442 | $2,824 | $3,815 | $5,494 | $65,939 |
| 3 | $23,030 | $1,919 | $2,879 | $3,071 | $3,551 | $4,798 | $6,787 | $81,454 |
| 4 | $27,750 | $2,313 | $3,470 | $3,701 | $4,280 | $5,783 | $8,080 | $96,969 |
| 5 | $32,470 | $2,706 | $4,059 | $4,330 | $5,007 | $6,765 | $9,372 | $112,483 |
| 6 | $37,190 | $3,099 | $4,649 | $4,959 | $5,734 | $7,748 | $10,665 | $127,998 |
| 7 | $41,910 | $3,493 | $5,240 | $5,589 | $6,463 | $8,733 | $10,908 | $130,908 |
| 8 | $46,630 | $3,886 | $5,829 | $6,218 | $7,190 | $9,715 | $11,151 | $133,816 |

NOTE: For family sizes 7+, some 85% SMI amounts are LOWER than 250% FPG. The highlighted cells in Appendix A indicate where 85% SMI caps the eligibility even at the 250% FPG level.

### Program Categories

1. **TANF Child Care** — TANF recipients (VIEW and non-VIEW); income-eligible by default
2. **SNAP E&T Child Care** — Parents in SNAP Employment & Training; income test required
3. **TANF Transitional Child Care** — Former TANF recipients; up to 12 months post-closure
4. **Head Start Wrap-Around** — Extended day/year care for Head Start-enrolled children
5. **Fee Child Care Program** — General low-income families; income test required

### Metropolitan Statistical Area Groups (Locality-Based Income Limits)
- **Group I**: 150% FPG (lowest cost-of-living localities)
- **Group II**: 160% FPG
- **Group III**: 185% FPG (highest cost-of-living localities)
- Localities are grouped by local median income with adjustments for cost of care
- Full mapping in Appendix Z of the guidance manual

### Maximum Reimbursable Rates (MRR)
- Rates vary by: provider type, child age, locality
- Set using a cost-of-quality estimation model (not market rate survey since 2023)
- Level 1 and Level 2 rates exist (Level 2 for higher-quality providers)
- Rates available as dataset: https://data.virginia.gov/dataset/general-child-care-subsidy-program-maximum-reimbursement-rates
- Effective date of current rates: August 3, 2023
- Providers may charge above MRR; families responsible for the difference

### Income Conversion
- Weekly income x 4.3
- Bi-weekly income x 2.15
- Semi-monthly income x 2

---

## FY26 Copayment One Pager (User-Provided PDF)

Source: https://www.childcare.virginia.gov/home/showpublisheddocument/65775/638937831784030000

### Table 1: Current and New Copayment Scales

| Income Threshold | Current Copayment Scale | Copayment Scale effective July 1, 2025 |
|---|---|---|
| Income = $0 | $0 | $0 |
| >0-100% FPG | $0 | $5 |
| 101-150% FPG | $60 | $125 |
| 151-200% FPG | $60 | $175 |
| 201-250% FPG | $120 | $225 |
| 251-300% FPG | $120 | $275 |
| 301-350% FPG | $180 | $325 |
| 351% FPG - 85% SMI | $180 | $375 |
| Maximum total copayment | 7% of family income | 5% of family income |

### Table 2: Effective Dates for the New Copayment Scale

| Redetermination due by | Copayment changes effective |
|---|---|
| June 30, 2025 | September 1, 2025 |
| July 30, 2025 | August 1, 2025 |
| August 30, 2025 or later | September 1, 2025 |

New copayment scale fully implemented for all families by September 1, 2025.

### Table 3: Copayment Family Scenarios

| Family | Size | Annual/Monthly Income | % FPG | 5% of Income | Per-Child Copay (Scale) | # Children | Total Copay (Scale) | Actual Total |
|---|---|---|---|---|---|---|---|---|
| A | 4 | $36,000/$3,000 | 100-150% | $150 | $125 | 2 | $250 | $150 or $75/child |
| B | 3 | $64,800/$5,400 | 250-300% | $270 | $275 | 1 | $275 | $270 |
| C | 5 | $114,000/$9,500 | 350% FPG - 85% SMI | $475 | $375 | 2 | $750 | $475 |

Note: Actual total copayment = min(total copayment from scale, 5% of family income)
