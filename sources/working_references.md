# Indiana TANF Historical Sources — Working References

## Summary of Key Historical Finding

**Indiana's TANF benefit amounts (standard of need) were frozen at 1988 AFDC levels from program inception (1997) until July 1, 2023**, when SEA 265 took effect. This means the standard of need schedule was unchanged for ~35 years. The 1997 Green Book confirms the 1997 values match the pre-2023 values exactly.

---

## 1. Standard of Need (Benefit Amounts by Family Size)

### Era 1: 1988–2023-06-30 (AFDC-era frozen values)

These values were set in 1988 under AFDC and carried forward unchanged into TANF (1997) through June 30, 2023.

**Assistance Groups with Adults and Children:**

| Family Size | Monthly Amount |
|-------------|---------------|
| 1 | $139 |
| 2 | $229 |
| 3 | $288 |
| 4 | $346 |
| 5 | $405 |
| 6 | $463 |
| 7 | $522 |
| 8 | $580 |
| 9 | $637 |
| 10 | $695 |

**Sources:**
- 1997 Green Book (GPO-CPRT-105WPRT37945): Confirms $139/$229/$288/$346/$405/$463 for family sizes 1-6 as of January 1997
  - https://www.govinfo.gov/content/pkg/GPO-CPRT-105WPRT37945/html/GPO-CPRT-105WPRT37945-2-7.htm
- Issue #6665 references: 2001 Indiana Program Budget Book confirms "$288 for family of three"
  - https://www.in.gov/sba/files/2001_Indiana_Program_Budget_Book_Narratives.pdf#page=64
- Indiana DCS "Assistance for Unlicensed Relative Placements" (2016 version)
  - https://www.in.gov/dcs/files/16.2%20Assistance%20for%20Unlicensed%20Relative%20Placements.pdf#page=7
- Indiana DCS "Assistance for Unlicensed Relative Placements" (2019 archived version)
  - https://www.in.gov/dcs/files/16.02-Assistance-for-Unlicensed-Relative-Placements.docx-ARCHIVED-8-28-2020-v5.pdf#page=7
- WIOA State Plan Portal (PY 2020-2023) confirms $139.50/$229.50/$288/$346/$405.50/$463/$522.50/$580 per month
  - https://wioaplans.dol.gov/node/67731
- Multiple news sources confirm benefits "unchanged since 1988" / "first increase since TANF's creation"

**RESOLVED — DCS PDF Verification (page 7 of both PDFs):**
Both DCS PDFs (2016 current and 2019 archived) show identical round-number values. The WIOA State Plan half-dollar amounts ($139.50, $229.50, etc.) are incorrect/approximate — the authoritative DCS documents show $139.00, $229.00, etc.

**Sizes 9-10:** Not shown in DCS PDFs (table goes to size 8 only). Pattern analysis: increments are +$90, +$59, then +$58 per additional member (sizes 3-8). Extrapolating: size 9 = $638, size 10 = $696. However, the 1997 Green Book only covers sizes 1-6, and the DCS table covers sizes 1-8. Sizes 9-10 remain unverified for the pre-2023 era — may not have been defined (max unit size may have been 8).

**DCS PDF also shows Gross Income Limits (pre-2023):**

| Family Size | Gross Income Limit |
|-------------|-------------------|
| 1 | $286.75 |
| 2 | $471.75 |
| 3 | $592.00 |
| 4 | $712.25 |
| 5 | $832.50 |
| 6 | $952.75 |
| 7 | $1,073.00 |
| 8 | $1,193.25 |

**DCS PDF also shows Children-Only amounts:**

| Family Size | Children Only |
|-------------|--------------|
| 1 | $139.00 |
| 2 | $198.00 |
| 3 | $256.00 |
| 4 | $315.00 |
| 5 | $373.00 |
| 6 | $432.00 |
| 7 | $490.00 |
| 8 | $549.00 |

### Era 2: 2023-07-01–present (SEA 265 values)

These values took effect July 1, 2023, per SEA 265 (Senate Enrolled Act 265, signed May 22, 2023).

| Family Size | Monthly Amount |
|-------------|---------------|
| 1 | $155 |
| 2 | $255 |
| 3 | $320 |
| 4 | $385 |
| 5 | $450 |
| 6 | $515 |
| 7 | $580 |
| 8 | $645 |
| 9 | $710 |
| 10 | $775 |

**Sources:**
- Indiana FSSA DFR "About TANF" page (current): Shows Gross Income / Net Income tables
  - https://www.in.gov/fssa/dfr/tanf-cash-assistance/about-tanf/
- 470 IAC 10.3-4-3(a)(1): Standard of need schedule
  - https://iar.iga.in.gov/code/2026/470/10.3#470-10.3-4-3
- IC 12-14-2-5: Statutory authority for standard of need
  - https://iga.in.gov/laws/2025/ic/titles/12/#12-14-2-5
- SEA 265 bill page:
  - https://iga.in.gov/legislative/2023/bills/senate/265/details

**Pattern:** $155, +$100, then +$65 per additional member (sizes 3-10).

---

## 2. Earned Income Disregards

### For Eligibility Determination

**Current (2023-07-01–present):**
- Work expense deduction: $90 (from gross earnings)
- Flat disregard: $30
- Earned income disregard rate: 33% (one-third of remaining after $30 deduction)

**Source:** 470 IAC 10.3-4-4(c)(1) and (c)(2)
- https://iar.iga.in.gov/code/2026/470/10.3#470-10.3-4-4

**Historical context:** The "$30 and 1/3" disregard is an inherited AFDC-era policy. Per the WIOA State Plan (PY 2020-2023):
- $90 work expense disregard
- $30 and 1/3 disregard for four consecutive months following work expense deduction
- $30 disregard for eight-month period thereafter
- Source: https://wioaplans.dol.gov/node/67731

**NOTE:** The current codebase has a flat $30 disregard and 33% rate without the time-limited phaseout. This may be an intentional simplification or may need review.

### For Benefit Calculation

**Current (2023-07-01–present):**
- Earned income disregard rate: 75% (i.e., only 25% of gross earnings counted)

**Source:** 470 IAC 10.3-4-4(d)(1)
- https://iar.iga.in.gov/code/2026/470/10.3#470-10.3-4-4
- WIOA State Plan confirms: "75% of earned income is disregarded; 25% of gross earnings and 100% of non-exempt unearned income applied to benefit calculation"

**Historical:** This 75% disregard for benefit calculation appears to be longstanding. Need to verify if it changed with SEA 265.

---

## 3. Resource Limits

### At Application
- **Amount:** $1,000
- **Source:** 470 IAC 10.3-4-2 (references IC 12-14-1-1(a) implicitly)
  - https://iar.iga.in.gov/code/2026/470/10.3#470-10.3-4-2
  - Cornell LII: https://www.law.cornell.edu/regulations/indiana/470-IAC-10.3-4-2

### While Receiving
- **Amount:** $10,000
- **Source:** IC 12-14-1-1(b) — "does not cease to qualify...so long as the resources...are valued at not more than ten thousand dollars ($10,000)"
  - https://iga.in.gov/laws/2025/ic/titles/12/#12-14-1-1
  - LawServer: https://www.lawserver.com/law/state/indiana/in-code/indiana_code_12-14-1-1
  - Last amended by P.L.103-2023 (SEA 265)

**Historical:** The $1,000 at-application limit appears to be longstanding (AFDC-era). The $10,000 while-receiving limit was enacted or modified by SEA 265 (P.L.103-2023). The WIOA State Plan (PY 2020-2023) mentions $1,000 initial and $1,500 ongoing — suggesting the while-receiving limit was $1,500 before SEA 265 changed it to $10,000.

---

## 4. Vehicle Exemption

- **Amount:** $20,000 total equity value for all motor vehicles
- **Source:** IC 12-14-2-1(b)(2) — referenced in 470 IAC 10.3-4-2
  - https://iga.in.gov/laws/2025/ic/titles/12/#12-14-2-1
  - Cornell LII confirms: "Each applicant group will be allowed an exclusion of $20,000 of total equity value in motor vehicles"

**Historical:** Need to verify when $20,000 amount was set. May have been changed by SEA 265 or earlier legislation.

---

## 5. Continuing Eligibility FPG Rate

- **Current rate:** 100% of Federal Poverty Guidelines (for continuing eligibility)
- **Source:** 470 IAC 10.3-4-1
  - https://iar.iga.in.gov/code/2026/470/10.3#470-10.3-4-1

**Historical:** Per SEA 265, the income eligibility threshold is being phased in:
- Pre-SEA 265: ~16-17% FPL (grossly restricted)
- SEA 265 phase-in to 35% FPL, then to 50% FPL by end of 2027
- First eligibility increase: July 2025
- Full increase: ~2027-2028
- The FSSA "About TANF" page shows gross income limit of 35% FPL currently
- Continuing eligibility: 100% FPG (for those already receiving)

**NOTE:** The codebase currently has `fpg_rate` = 1 (100%) for continuing eligibility starting 2023-07-01. This represents the continuing eligibility threshold, not the initial eligibility gross income test.

---

## 6. Gross Income Test

**Current (from FSSA About TANF page):**

| Family Size | Gross Income Limit | Net Income Limit |
|-------------|-------------------|-----------------|
| 1 | $457 | $248 |
| 2 | $618 | $409 |
| 3 | $778 | $513 |
| 4 | $938 | $617 |
| 5 | $1,099 | $721 |
| 6 | $1,259 | $825 |
| 7 | $1,420 | $929 |
| 8 | $1,580 | $1,033 |
| 9 | $1,740 | $1,137 |
| 10 | $1,901 | $1,241 |
| Each Additional | +$161 | +$104 |

**Source:** https://www.in.gov/fssa/dfr/tanf-cash-assistance/about-tanf/

**Analysis:** The gross income limit appears to be approximately 35% of FPL (consistent with the current phase of SEA 265). The net income limits appear to be approximately 160% of the standard of need amounts (e.g., $513 / $320 = 1.603 for family of 3).

---

## 7. Major Legislative History

| Date | Event | Source |
|------|-------|--------|
| 1988 | Indiana sets AFDC benefit schedule (standard of need) in statute | Multiple news sources |
| 1997-10-01 | Indiana TANF program begins, carrying forward AFDC benefit levels | Federal welfare reform (PRWORA 1996) |
| 1997-2023 | Benefit levels frozen at 1988 AFDC amounts | CBPP, news articles |
| 2023-05-22 | SEA 265 signed by Governor | https://www.indianasenaterepublicans.com/ford-bill-expanding-tanf-eligibility-in-indiana-signed-by-governor |
| 2023-07-01 | SEA 265 benefit increases take effect (standard of need raised) | 470 IAC 10.3-4-3, FSSA About TANF page |
| 2023-07-01 | Resource limit while receiving raised to $10,000 | IC 12-14-1-1(b), P.L.103-2023 |
| 2023-07-01 | Family benefit cap repealed | SEA 265 |
| 2025-07-01 | First eligibility threshold increase (to 35% FPL) | SEA 265 phase-in |
| ~2027 | Full eligibility threshold increase (to 50% FPL) | SEA 265 phase-in |

---

## 8. Regulatory Authority Sources

### Indiana Code (IC)
- **IC 12-14-1-1**: TANF eligibility, resource limits
  - https://iga.in.gov/laws/2025/ic/titles/12/#12-14-1-1
- **IC 12-14-2-1**: Property/vehicle exemptions
  - https://iga.in.gov/laws/2025/ic/titles/12/#12-14-2-1
- **IC 12-14-2-5**: Standard of need schedule
  - https://iga.in.gov/laws/2025/ic/titles/12/#12-14-2-5

### Indiana Administrative Code (470 IAC)
- **470 IAC 10.3**: TANF Assistance Program (full article)
  - https://iar.iga.in.gov/latestArticle/470/10.3
  - Justia: https://regulations.justia.com/states/indiana/title-470/article-10-3/
- **470 IAC 10.3-4-1**: Continuing eligibility FPG rate
- **470 IAC 10.3-4-2**: Real and personal property (resource limits)
  - Cornell LII: https://www.law.cornell.edu/regulations/indiana/470-IAC-10.3-4-2
- **470 IAC 10.3-4-3**: Standard of need amounts
- **470 IAC 10.3-4-4**: Income deductions/disregards

### Legislation
- **SEA 265 (2023)**: First TANF increase in 30+ years
  - Bill page: https://iga.in.gov/legislative/2023/bills/senate/265/details

### State Plan Documents
- **Indiana TANF State Plan Amendment**
  - https://www.in.gov/fssa/dfr/files/TANF_Indiana_State_Plan_amendment.pdf
- **Indiana TANF State Plan Renewal** (effective 1/1/2023)
  - https://www.in.gov/fssa/dfr/files/Indiana-TANF-State-Plan_Renewal.pdf

### Policy Manuals
- **FSSA DFR Policy Manual** (main page)
  - https://www.in.gov/fssa/dfr/forms-documents-and-tools/policy-manual/
- **Chapter 3400**: Financial eligibility criteria
  - https://www.in.gov/fssa/dfr/files/3400.pdf
- **Chapter 2800**: Income
  - https://www.in.gov/fssa/dfr/files/2800.pdf
- **Policy Manual Transmittals** (2023, 2024)
  - https://www.in.gov/fssa/dfr/forms-documents-and-tools/policy-manual/program-policy-manual-transmittals/

### Cross-Reference/Verification Sources
- **1997 Green Book** (GPO): AFDC/TANF benefit tables by state (January 1997)
  - https://www.govinfo.gov/content/pkg/GPO-CPRT-105WPRT37945/html/GPO-CPRT-105WPRT37945-2-7.htm
- **2004 Green Book** (GPO): TANF benefit tables
  - https://www.govinfo.gov/content/pkg/GPO-CPRT-108WPRT108-6/html/GPO-CPRT-108WPRT108-6-2-7.htm
- **Urban Institute Welfare Rules Database**: Historical TANF policies 1996-2023
  - https://wrd.urban.org/
  - Databook (2013): https://wrd.urban.org/sites/default/files/documents/2023-09/Welfare%20Rules%20Databook%202013.pdf
  - Databook (2021): https://www.urban.org/sites/default/files/2023-08/Welfare%20Rules%20Databook%20State%20TANF%20Policies%20as%20of%20July%202021.pdf
  - Graphical Overview (2023): https://www.urban.org/sites/default/files/2025-05/Graphical-Overview-of-State-and-Territory-TANF-Policies-as-of-July-2023.pdf
- **WIOA State Plan Portal (PY 2020-2023)**: Indiana TANF details
  - https://wioaplans.dol.gov/node/67731
- **NCCP TANF Profile (Indiana)**: 2024 benefit comparison
  - https://www.nccp.org/wp-content/uploads/2024/08/TANF-profile-Indiana.pdf
- **NCCP 50-State Comparison**: 2024 TANF benefit amounts
  - https://www.nccp.org/wp-content/uploads/2024/11/TANF-Benefit-Amounts-2024-FINAL.pdf
- **CBPP**: TANF benefit level analysis
  - https://www.cbpp.org/research/income-security/continued-increases-in-tanf-benefit-levels-are-critical-to-helping
- **INCAP Report**: Indiana TANF history and analysis
  - https://institute.incap.org/assets/docs/Reports/TANF%20Report_Final.pdf
- **INCAP Fact Sheet (2021)**: TANF and SB 233
  - https://institute.incap.org/assets/docs/Fact-Sheets/FactSheet-2021-TANFandSB233.pdf
- **2001 Indiana Budget Book**: Confirms $288 for family of 3
  - https://www.in.gov/sba/files/2001_Indiana_Program_Budget_Book_Narratives.pdf#page=64
- **Indiana DCS Documents** (issue #6665 references):
  - 2016 version: https://www.in.gov/dcs/files/16.2%20Assistance%20for%20Unlicensed%20Relative%20Placements.pdf#page=7
  - 2019 archived: https://www.in.gov/dcs/files/16.02-Assistance-for-Unlicensed-Relative-Placements.docx-ARCHIVED-8-28-2020-v5.pdf#page=7
  - 2016 archived (v3): https://www.in.gov/dcs/files/16.2-Assistance-for-Unlicensed-Relative-Placements-Archive-10-31-2016-v3.pdf
- **2010 FSSA Fact Sheet**: Statewide TANF data
  - https://www.in.gov/fssa/dfr/files/INFact_Sheet_Statewide_2010-01.pdf

### News Coverage (for timeline verification)
- Indiana Capital Chronicle (Jan 2023): "Senate committee passes first TANF increase in over 30 years"
  - https://indianacapitalchronicle.com/2023/01/24/senator-committee-passes-first-tanf-increase-in-over-30-years/
- WFYI (Jan 2023): "Indiana Senate passes bill with 'modest' increases to TANF eligibility limit, payments"
  - https://www.wfyi.org/news/articles/indiana-senate-passes-bill-with-modest-increases-to-tanf-eligibility-limit-payments
- WFYI (Apr 2023): "Indiana set to expand access to temporary government help"
  - https://www.wfyi.org/news/articles/indiana-set-to-expand-access-to-temporary-government-help-for-low-income-people--eventually
- Indiana Public Radio (Jun 2023): "Congress' debt deal may hinder new Indiana law"
  - https://indianapublicradio.org/news/2023/06/congress-debt-deal-may-hinder-a-new-indiana-law-to-extend-tanf-benefits-to-thousands-of-families/

---

## 9. Implementation Plan for Backdating

### Parameters That Need Historical Entries

Given that benefits were frozen from 1988 through June 30, 2023, each parameter needs ONE historical entry backdated to program inception:

1. **standard_of_need/amount.yaml**: Add 1997-10-01 entries with the AFDC-era values (sizes 1-10)
2. **income/deductions/benefit/earned_income_disregard/rate.yaml**: Add 1997-10-01 entry (verify if 75% is unchanged)
3. **income/deductions/eligibility/earned_income_disregard/rate.yaml**: Add 1997-10-01 entry (verify if 33% is unchanged)
4. **income/deductions/eligibility/flat_disregard/amount.yaml**: Add 1997-10-01 entry (verify if $30 is unchanged)
5. **income/deductions/work_expense/amount.yaml**: Add 1997-10-01 entry (verify if $90 is unchanged)
6. **resources/limit/at_application/amount.yaml**: Add 1997-10-01 entry ($1,000 — longstanding)
7. **resources/limit/while_receiving/amount.yaml**: Add 1997-10-01 entry with OLD value (likely $1,500 per WIOA State Plan) — then 2023-07-01 = $10,000
8. **resources/vehicle_exemption/amount.yaml**: Need to verify if $20,000 was always the amount or changed
9. **eligibility/continuing/fpg_rate.yaml**: Need to verify historical value

### Open Questions (Need Verification from Prep Agent PDF Renders)

1. **Exact pre-2023 standard of need for sizes 7-10**: Green Book only goes to size 6. DCS PDFs may have full table.
2. **Half-dollar amounts**: WIOA shows $139.50, $229.50, etc. vs Green Book showing $139, $229. Which is correct?
3. **While-receiving resource limit history**: Was it $1,500 before SEA 265 changed it to $10,000?
4. **Vehicle exemption history**: Was $20,000 always the amount?
5. **Earned income disregard history**: Were the rates (75% benefit, 33% eligibility, $30 flat, $90 work expense) unchanged since program inception?
6. **FPG rate history**: The current 100% FPG for continuing eligibility — was this always the case?
7. **Children-only groups**: Different benefit schedule exists (see WIOA data). Not currently modeled in codebase — may not need backdating but should document.

---

## 10. Children-Only Assistance Groups (Reference Only)

Per WIOA State Plan (PY 2020-2023), Indiana has a separate benefit schedule for children-only groups:

| Children | Monthly Amount |
|----------|---------------|
| 1 | $139.50 |
| 2 | $198.00 |
| 3 | $256.50 |
| 4 | $315.00 |
| 5 | $373.50 |
| 6 | $432.00 |
| 7 | $490.50 |
| 8 | $549.00 |

This is NOT currently implemented in the codebase. Documenting for completeness.

---

*Last updated: 2026-02-26*
*Status: Research complete, pending prep agent PDF verification*
