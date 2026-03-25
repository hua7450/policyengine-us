# Delaware Purchase of Care (POC) - Child Care Assistance Program

## Working References

### Primary Regulatory Sources

1. **16 Del. Admin. Code 11000-11004 - Applying for Child Care Assistance**
   - URL: https://www.law.cornell.edu/regulations/delaware/16-Del-Admin-Code-SS-11000-11004
   - Contains: Income eligibility thresholds, copayment rules (7% cap, waiver conditions), activity requirements, income calculation rules, excluded income categories, phase-out rules, authorization periods, priority categories
   - Note: Regulation text still references 185% FPL initial threshold, but the DSS eligibility page (source 18) now shows 200% FPL initial, 300% FPL at redetermination, 85% SMI hard cap
   - Key sections: 11004.3.1 (priority categories), 11004.7 (copayment), 11004.7.1 (excessive financial burden), 11004.9.5 (12-month authorization), 11004.11 (temporary changes), 11004.13 (phase-out)

2. **16 Del. Admin. Code 11000-11003 - Determining Technical Eligibility for Child Care Assistance**
   - URL: https://www.law.cornell.edu/regulations/delaware/16-Del-Admin-Code-SS-11000-11003
   - Contains: Activity requirements (employment, education, training, protective services), child age limits (under 13, 13-18 with special needs), residency requirements, citizenship/non-citizen rules, family composition rules
   - Key sections: 11003.6.2 (DFS referral bypass), 11003.9.1 (income calculation), 11003.9.3 (family size)

3. **16 Del. Admin. Code 11000-11006 - Subsidized Child Care Provider Policy**
   - URL: https://www.law.cornell.edu/regulations/delaware/16-Del-Admin-Code-SS-11000-11006
   - Contains: Provider eligibility, payment structure, absent day policy (10 days/month), holiday reimbursement, fee collection rules
   - Key sections: 11006.1 (provider eligibility), 11006.4 (payment), 11006.4.1 (absent days), 11006.4.2 (fee collection), 11006.5.1 (direct deposit)

4. **24 DE Reg 704 (January 2021) - Final Regulation Amendment**
   - URL: https://archive.regulations.delaware.gov/register/january2021/final/24%20DE%20Reg%20704%2001-01-21.htm
   - Contains: 185% FPL eligibility cap (Section 11003.9.1(4.B)), DFS referral exemption (11003.6.2), copayment waiver conditions (70% FPL gross test, 40% FPL net test), income averaging (3-6 months), self-employment rules, 20 income exclusion categories
   - Note: The regulations.delaware.gov site renders only CSS on fetch - the Cornell LII mirror has the readable text

### Federal CCDF Sources

5. **CCDF Family Income Eligibility Levels by State (January 2025)**
   - URL: https://acf.gov/sites/default/files/documents/occ/CCDF-Family-Income-Eligibility-Levels-by-State.pdf#page=1
   - Delaware data: 46% of SMI for family of 3 ($3,833/month), 46% of SMI for family of 4 ($4,625/month)
   - Downloaded to: /tmp/de-ccdf-income-levels.pdf

6. **CCDF Provider Payment Rates by State (January 2025)**
   - URL: https://acf.gov/sites/default/files/documents/occ/CCDF-Provider-Payment-Rates-by-State.pdf#page=2
   - Delaware data: 50% of market rate across all age groups (infant center, infant family, toddler center, toddler family, preschool center, preschool family)
   - Base weekly infant rates: $325 (center), $223 (family child care) - both at 50% of providers receiving base rate
   - Downloaded to: /tmp/de-ccdf-rates.pdf

7. **Delaware FFY 2025-2027 CCDF Plan Appendix (Lead Agency Implementation Plan)**
   - URL: https://acf.gov/sites/default/files/documents/occ/DE-Accepted-ACF118-CCDF-FFY-2025-2027-Appendix.pdf
   - Plan approved: 2024-11-09
   - Key non-compliance areas: 12-month eligibility continuity, copay cap at 7% (implemented July 1, 2024), prospective/enrollment-based payment (waiver through April 30, 2026)
   - Policy reference: DSSM 11004.9.5 (12-month authorization), DSSM 11004.11 (temporary changes - 90 day job search)
   - Downloaded to: /tmp/de-ccdf-plan-appendix.pdf

### State Program Documents

8. **Purchase of Care Billing Guidance for June 2024 (My Child DE)**
   - URL: https://www.mychildde.org/purchase-of-care-billing-guidance-for-june-2024/
   - Contains: FY2025 reimbursement rate tables by age group and provider type (effective July 1, 2024)
   - Rate table:
     | Age Group | Family Home Daily | Family Home Weekly | Center Daily | Center Weekly |
     |-----------|-------------------|-------------------|--------------|---------------|
     | Infant (0) | $44.50 | $222.50 | $65.00 | $325.00 |
     | Toddler (1) | $40.00 | $200.00 | $58.00 | $290.00 |
     | Preschool (2-5) | $40.00 | $200.00 | $51.00 | $255.00 |
     | School Age Full-time (6+) | $32.00 | $160.00 | $38.00 | $190.00 |
     | School Age Part-time (6+) | $20.00 | $100.00 | $27.00 | $135.00 |
   - **Special Needs Rate table** (from DSS child care page screenshot, rates effective July 1, 2024 - June 30, 2027):
     | Age Group | Family Home Daily | Family Home Weekly | Center Daily | Center Weekly |
     |-----------|-------------------|-------------------|--------------|---------------|
     | Infant Special Need (0) | $46.73 | $233.63 | $68.25 | $341.25 |
     | Toddler Special Need (1) | $43.25 | $216.25 | $60.90 | $304.50 |
     | Preschool Special Need (2-5) | $43.25 | $216.25 | $55.69 | $278.45 |
     | School Age Special Need (6+) FT | $33.60 | $168.00 | $39.90 | $199.50 |
     | School Age Special Need (6+) PT | $21.00 | $105.00 | $28.35 | $141.75 |
   - Copay cap: 7% of income; families at/below 150% FPL: no copayment
   - Absent days: up to 10 per month reimbursed
   - Uniform reimbursement at state rate regardless of private rate

9. **Purchase of Care 101 Fact Sheet (May 2019, IPA/University of Delaware)**
   - URL: https://mychildde.org/wp-content/uploads/purchase-of-care-2019.pdf#page=1
   - Contains: 185% FPL income eligibility table by family size (2019 values)
   - Income table (185% FPL):
     | Family Size | Gross Monthly Income |
     |-------------|---------------------|
     | 1 | $1,872 |
     | 2 | $2,538 |
     | 3 | $3,204 |
     | 4 | $3,870 |
     | 5 | $4,536 |
     | 6 | $5,202 |
     | 7 | $5,868 |
     | 8 | $6,534 |
     | 9 | $7,232 |
     | 10 | $7,930 |
   - Children: birth through age 12
   - As of March 2019: 15,035 children subsidized; 65% ages birth to 5
   - Provider reimbursement (2018): ~59% of 75th percentile market rate
   - Downloaded to: /tmp/de-poc-101.pdf

10. **Purchase of Care Brochure (Revised May 2017)**
    - URL: https://laborfiles.delaware.gov/main/det/one-stop/DSS%20Brochure%20Child%20Care%205-2017.pdf
    - Contains: Program overview, eligibility summary (200% FPL), care types (POC, POC Plus, Self-Arranged Care, Relative Care), application process, DSS office locations
    - Application: Delaware ASSIST at assist.dhss.delaware.gov or local DSS offices
    - Required documents: proof of income (4 pay stubs weekly/2 bi-weekly for past 30 days), proof of employment, school/training schedule, proof of medical necessity
    - Downloaded to: /tmp/de-poc-brochure.pdf

11. **Purchase of Care Provider Handbook (January 2023)**
    - URL: https://dhss.delaware.gov/wp-content/uploads/sites/11/dss/pdf/PurchaseofCareProviderHandbook_FINAL1_25_2023.pdf
    - Downloaded to: /tmp/de-ccap-poc-handbook.pdf (119 pages), text at /tmp/de-ccap-poc-handbook.txt
    - Screenshots: /tmp/de-ccap-handbook-page-001.png through -010.png (1200 DPI)
    - **Section C - Client Eligibility** (handbook pp.14-25):
      - Children: under 13, or 13-18 if physically/mentally incapable of self-care (medical professional determination)
      - Special needs children: under 19 years of age, physically or mentally incapable of self-care
      - DFS-referred children: exempt from financial criteria AND citizenship requirements
      - TWP participants: must be financially eligible but exempt from special need documentation
      - Activity requirements: TANF E&T, TANF TWP, employment, approved education/training, DFS protective services, special need
      - Application processed within 2 business days; filing date = start date for assistance
      - Must verify last 30 days of earned/unearned income
      - Presumptive child care may open pending verifications (DSSM 11004.8)
      - 30 days to provide verifications (child care starts on filing date); 30-60 days = starts on date received; >60 days = must reapply
    - **Section D - Rates and Child Care Types** (handbook pp.24-25):
      - Authorization types: Part-time (0-4 hrs), Full-time (4-10 hrs), Time and a half (10-14 hrs), Part-time with Extended Care (school-age)
      - Rates based on: provider geographic location, ages of children, hours of care
      - Rates set from Delaware Local Child Care Market Rate Survey results
    - **Section E - Reimbursement, Copayments, POC Plus** (handbook pp.26-37):
      - Copayment is per family (not per child), based on family income and family size
      - Copayment will not increase during 12-month eligibility period
      - Copayment amount shown on authorization notice and in PSS
      - When child uses 2 providers, copayment usually assigned to youngest child
      - POC Plus (POC+): provider charges client the difference between DSS rate and private rate
        - Example: $250/wk private - $200/wk DSS rate = $50/wk POC+ fee to client
      - Absent days: paid absent days per month = number of authorized days per week, up to max 5 days/month (handbook version; updated to 10/month effective July 2024)
      - 7 standard national holidays reimbursed (New Year's, Memorial Day, Independence Day, Labor Day, Thanksgiving, Christmas, Juneteenth); provider may substitute 1+ holidays
      - Allowable fees to POC families: copayment, POC+ fees, late pick-up fees, field trip fees, returned check fees
      - Providers CANNOT charge: registration fees, key FOBs, credit card fees, additional rates for authorized hours, place-holding fees, or any other unapproved fees
    - **Legal Authority** (handbook p.10):
      - State: Title 31, Part I, Chapter 3, Subchapter VII, Delaware Code - Section 391
      - Federal: Title XX Social Security Act, 7 CFR 273.7 (SNAP E&T child care), CCDBG as amended by PRWORA 1996

12. **Explaining Purchase of Care in Delaware (Vision Coalition, December 2020)**
    - URL: https://visioncoalitionde.org/wp-content/uploads/2020/12/Purchase-of-Care-1-pager-12.9.20-update.pdf
    - Contains: Program overview, funding breakdown ($41M federal + $47M state = $85M total), 22,000+ children ages 0-12 covered
    - Downloaded to: /tmp/de-poc-one-pager.pdf

### Policy Analysis Sources

13. **Delaware Adopts Some New Federal Child Care Rules (RODE:L, 2024)**
    - URL: https://rodelde.org/new-federal-child-care-rules-for-delaware/
    - Contains: June 2024 policy changes, copayment cap (7% from 9%), absent days (10 from 5 per month), 150% FPL copayment waiver, proposed 200% FPL eligibility, rate increase commitment to 75th percentile
    - Impact: 8,000 of 12,000 children/families affected; most below 150% FPL will have no copayment

14. **2024 Delaware Local Child Care Market Rate Survey (May 2024)**
    - URL: https://www.dhss.delaware.gov/wp-content/uploads/sites/11/dss/pdf/2024DelawareChildCareMarketRateSurvey.pdf
    - Downloaded to: /tmp/de-ccap-market-rate.pdf, text at /tmp/de-ccap-market-rate.txt
    - Screenshots: /tmp/de-ccap-market-rate-page-01.png through -10.png (1200 DPI)
    - Overall 38% price increase from 2021 to 2024; center avg +39%, FCC avg +36%
    - **75th Percentile Daily Rates - Family Child Care (Table 2)**:
      | Region | Infant | Toddler | Preschool | SA <4hr | SA >=4hr |
      |--------|--------|---------|-----------|--------|---------|
      | Kent & Sussex | $50.00 | $45.00 | $40.00 | $20.00 | $37.50 |
      | New Castle | $50.00 | $50.00 | $47.00 | $24.00 | $40.00 |
      | Statewide | $50.00 | $48.75 | $45.00 | $21.50 | $40.00 |
    - **75th Percentile Daily Rates - Centers (Table 3)**:
      | Region | Infant | Toddler | Preschool | SA <4hr | SA >=4hr |
      |--------|--------|---------|-----------|--------|---------|
      | Kent & Sussex | $62.38 | $57.00 | $50.00 | $30.00 | $42.50 |
      | New Castle | $75.00 | $68.76 | $60.40 | $33.95 | $55.56 |
      | Statewide | $72.00 | $65.00 | $58.05 | $32.20 | $54.40 |
    - **Odd-hour FCC statewide**: $10/hour at 75th percentile (Table 4)
    - **Special needs**: 57% of providers serve children with special needs; 71% report no additional costs; avg additional cost when reported: 10-11%
    - Survey methodology: census of ~900 licensed providers, 436 completed; FCC median enrollment 6 children (median 4 subsidized); center avg enrollment 73 children

### Delaware Code

15. **Delaware Code Title 31 Chapter 3 Subchapter IV - Child Placement**
    - URL: https://www.delcode.delaware.gov/title31/c003/sc04/index.html
    - Contains: Kinship Care Program (Section 356) - related caregiver eligibility, 200% FPL income limit
    - Note: This is for kinship/placement care, not the POC subsidy program directly

### Application Portal

16. **Delaware ASSIST**
    - URL: https://assist.dhss.delaware.gov
    - Online application portal for DSS benefits including Purchase of Care

### Additional Resources

17. **My Child DE - Financial Assistance**
    - URL: https://mychildde.org/families/financial-assistance/
    - Contains: Program descriptions, links to POC handbook, POC 101, and economic analysis
    - Contact: 1-800-734-2388

18. **Delaware DSS - Child Care Services (Eligibility Page)**
    - URL: https://dhss.delaware.gov/dss/childcr/
    - Downloaded to: /tmp/de-ccap-childcr.html
    - **CRITICAL SOURCE**: Contains the current "CHILD CARE INCOME ELIGIBILITY LIMITS & SLIDING FEE SCALE" table
    - Note: Initial eligibility is described as 185% FPL in body text, but the table header says "Max Gross Monthly Income (200% FPL)" - this reflects the policy change where initial eligibility moved to 200% FPL
    - Income thresholds at redetermination: 300% FPL; during authorization: 85% SMI
    - **Complete Income Eligibility Table** (from page, current as of 2025):
      | Family Size | 200% FPL | 300% FPL (Redet.) | 85% SMI (Auth.) | <40% FPL (Excess Burden) | <=150% FPL (Waived Copay) | 7% Copay Range | Phase-Out Range |
      |-------------|----------|-------------------|-----------------|--------------------------|--------------------------|----------------|----------------|
      | 1 | $2,610 | $3,915 | $4,645 | $522 | $1,958 | $1,959-$3,915 | $2,611-$3,915 |
      | 2 | $3,526 | $5,289 | $6,074 | $705 | $2,556 | $2,646-$5,289 | $3,527-$5,289 |
      | 3 | $4,442 | $6,663 | $7,503 | $888 | $3,332 | $3,333-$6,663 | $4,443-$6,663 |
      | 4 | $5,360 | $8,040 | $8,932 | $1,072 | $4,020 | $4,021-$8,040 | $5,361-$8,040 |
      | 5 | $6,276 | $9,414 | $10,361 | $1,255 | $4,707 | $4,708-$9,414 | $6,277-$9,414 |
      | 6 | $7,192 | $10,788 | $11,790 | $1,438 | $5,394 | $5,395-$10,788 | $7,193-$10,788 |
      | 7 | $8,110 | $12,165 | $12,058 | $1,622 | $6,083 | $6,084-$12,165 | $8,111-$12,165 |
      | 8 | $9,026 | $13,539 | $12,326 | $1,805 | $6,770 | $6,771-$13,539 | $9,027-$13,539 |
      | 9 | $9,944 | $14,916 | $12,594 | $1,989 | $7,458 | $7,459-$14,916 | $9,945-$14,916 |
      | 10 | $10,862 | $16,293 | $12,862 | $2,172 | $8,147 | $8,148-$16,293 | $10,863-$16,293 |
      | 11 | $11,780 | $17,670 | $13,130 | $2,356 | $8,835 | $8,836-$17,670 | $11,781-$17,670 |
      | 12 | $12,698 | $19,047 | $13,398 | $2,540 | $9,524 | $9,525-$19,047 | $12,699-$19,047 |
    - **Eligibility rules from page text**:
      - Initial eligibility: gross monthly income <= 185% FPL (body text says 185%, table header shows 200%)
      - At yearly redetermination: if income between 185%-200% FPL, graduated phase-out for 12 months
      - Case closes: income exceeds 85% of SMI OR no longer has need for care
    - **Table period**: "PURCHASE OF CARE (POC) PROGRAM OCTOBER 1, 2025 - SEPTEMBER 30, 2026" (per user-provided PDF)
    - **Provider rate image**: FY2025 POC rates image at `/wp-content/uploads/sites/11/2025/10/FY2024_POC_Rates_7-1-2024-300x162-1.png`
    - **Additional links from page**:
      - Form 611 (Child Care Medical Certification): `/wp-content/uploads/sites/11/dss/pdf/Form611_ChildCareMedicalCertification_2024-05_Revised.pdf`
      - 2024 Market Rate Survey, 2021 MRS, 2024 Cost of Care Study, Center/FCC Cost Estimation Tools

19. **Delaware DSS - FPL Income Limits**
    - URL: https://dhss.delaware.gov/dss/fpl/
    - Downloaded to: /tmp/de-ccap-fpl.html
    - Title: "2023-2024 Countable Income Limits"
    - **100% FPL Table** (by family size, monthly gross income):
      | Family Size | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
      |---|---|---|---|---|---|---|---|---|---|---|
      | Income | $1,215 | $1,644 | $2,072 | $2,500 | $2,929 | $3,357 | $3,785 | $4,214 | $4,643 | $5,072 |
    - Also has 130%, 165%, 185%, 200% FPL tables (all with same format by family size)
    - Note: These are 2023-2024 values; the child care eligibility page table (source 18) appears to use 2025 FPL values

20. **DSS Child Care Page - User-Provided PDF (March 2025)**
    - URL: https://dhss.delaware.gov/dss/childcr/
    - Downloaded to: /tmp/de-ccap-user-doc-1.pdf (8 pages), text at /tmp/de-ccap-user-doc-1.txt
    - Screenshots: /tmp/de-ccap-user-doc-1-page-1.png through -8.png
    - Captured: 2026-03-25 at 1:40 PM
    - **Key new content - Complete POC Rate Table** (page 6 screenshot, "Purchase of Care Rates July 1, 2024 - June 30, 2027"):
      - Statewide rates, both regular and special needs
      - Rates period: July 1, 2024 through June 30, 2027 (3-year period)
      - Regular rates match source 8 (POC Billing Guidance)
      - Special needs rates extracted and added to source 8
    - **Eligibility table period**: "PURCHASE OF CARE (POC) PROGRAM OCTOBER 1, 2025 - SEPTEMBER 30, 2026"
    - **Income table**: Same values as HTML source 18, extends to family size 18
    - **Additional family sizes 13-18** (from text, not in HTML extraction):
      | Family Size | 200% FPL | 300% FPL (Redet.) | 85% SMI (Auth.) | <40% FPL | <=150% FPL | 7% Copay Range | Phase-Out Range |
      |-------------|----------|-------------------|-----------------|----------|------------|----------------|----------------|
      | 13 | $13,616 | $20,424 | $13,666 | $2,723 | $10,212 | $10,213-$20,424 | $13,617-$20,424 |
      | 14 | $14,534 | $21,801 | $13,934 | $2,907 | $10,901 | $10,902-$21,801 | $14,535-$21,801 |
      | 15 | $15,452 | $23,178 | $14,202 | $3,090 | $11,589 | $11,590-$23,178 | $15,453-$23,178 |
      | 16 | $16,370 | $24,555 | $14,470 | $3,274 | $12,278 | $12,279-$24,555 | $16,371-$24,555 |
      | 17 | $17,288 | $25,932 | $14,738 | $3,458 | $12,966 | $12,967-$25,932 | $17,289-$25,932 |
      | 18 | $18,206 | $27,309 | $15,006 | $3,641 | $13,655 | $13,656-$27,309 | $18,207-$27,309 |
    - Confirms body text still says "185% FPL" for initial eligibility while table uses 200% FPL
    - Confirms graduated phase-out text: "between 185% and 200% of the FPL at their yearly redetermination"
    - Confirms hard cap: "gross monthly income exceeds 85% of the SMI"
