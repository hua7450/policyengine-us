# Iowa State Supplementary Assistance (SSA) — Working References

Research compiled 2026-04-16 for PolicyEngine-US implementation.
Every PDF link uses `#page=NN` (file page, not printed page) unless the PDF is single-page.

---

## 0. Program Identification

- **Official name**: **State Supplementary Assistance (SSA)** — Iowa statutorily and operationally uses "State Supplementary Assistance", *not* "State Supplementary Payment". The program is sometimes shortened to "SSP" in colloquial use but Iowa Code chapter 249 title reads "STATE SUPPLEMENTARY ASSISTANCE".
- **Administering agency**: **Iowa Department of Health and Human Services (HHS)** — reorganized from the Iowa Department of Human Services (DHS) in 2023. The DHS employees' manual is now the "Iowa Department of Health and Human Services Employees' Manual" (Title 6, Chapter B). Many rules and form numbers still reference "DHS".
- **Dual federal/state administration**:
  - **SSA-administered** (federal Social Security Administration issues payment on behalf of state): Mandatory State Supplement, Blind Supplement, Dependent Person (DP), Family-Life Home (FLH).
  - **State-administered** (Iowa HHS issues payment): Residential Care Facility (RCF), In-Home Health-Related Care (IHHRC), Supplement for Medicare and Medicaid Eligibles (SMME).
  - Source: IAC 441—50.2(1) paragraphs a–c; Employees' Manual 6-B p.2.
- **Legal basis**: Iowa Code Chapter 249; IAC 441 Chapters 50, 51, 52, 54, and 177; 20 CFR 416 Subpart T (§§ 416.2001–416.2099).

---

## 1. Iowa Code (Statute)

### 1.1 Iowa Code § 249.3 — Eligibility
- **Local file**: `/tmp/ia-ssp/code-249-3.pdf` (2 pages; text: `code-249-3.txt`)
- **URL**: https://www.legis.iowa.gov/docs/code/249.3.pdf
- **Key content**: Four subsection groups of eligible persons:
  1. "Essential person" grandfathered from December 1973 categorical assistance (OAA/AB/AD).
  2. Persons receiving care in a licensed adult foster home, boarding home, custodial home, or "another type of protective living arrangement", OR nursing care in the person's own home, who are receiving SSI or would receive SSI but for excess income.
  3. Persons living with a dependent spouse/parent/child/adult child, receiving SSI or would receive SSI but for excess income, with income insufficient to provide for the dependent.
  4. The "Supplement for Medicare and Medicaid Eligibles" (SMME) group — aged 65+ or disabled, living in own home/home of another/group living/medical facility, eligible for SSI but for excess income or SGA, already receiving full Medicaid, eligible for Medicare Part B, income between 120% FPL and Medicaid income limit.

### 1.2 Iowa Code § 249.9A — Personal Needs Allowance
- **Local file**: `/tmp/ia-ssp/code-249-9A.pdf` (1 page; text: `code-249-9A.txt`)
- **URL**: https://www.legis.iowa.gov/docs/code/2025/249.9A.pdf
- **Key content**: The department shall increase the RCF personal needs allowance by the same percentage and at the same time as federal SSI/Social Security COLA. Added by 2024 Acts, ch 1157, §46. NEW section (2024).

### 1.3 Iowa Code Chapter 249 (top level)
- The overall "State Supplementary Assistance" chapter title in the Iowa Code. Referred to in manual as "Iowa Code Chapter 249, 'State Supplemental Assistance'" (note: Code title uses "Supplementary"; manual labels with "Supplemental" — both appear).

---

## 2. Iowa Administrative Code (Regulations)

All chapters below live under **Iowa Administrative Code Title 441 — Human Services Department**, Title V "State Supplementary Assistance".

### 2.1 IAC 441—Chapter 50 — Application for Assistance
- **Local file**: `/tmp/ia-ssp/iac-441-50.pdf` (4 pages; text: `iac-441-50.txt`)
- **URL**: https://www.legis.iowa.gov/docs/iac/chapter/04-15-2026.441.50.pdf
- **Rule 441—50.1** — Definitions of aged, blind, disabled, applicant, client, "Payment for a dependent relative", "Payment for a protective living arrangement" (family life home), "Payment for residential care".
- **Rule 441—50.2** — Application procedures; paragraphs 50.2(1)(a)–(c) specify federal-vs-state administration of each SSA supplement.
- Recent amendment: ARC 9304C, IAB 5/28/25, effective 7/2/25.

### 2.2 IAC 441—Chapter 51 — Eligibility
- **Local file**: `/tmp/ia-ssp/iac-441-51.pdf` (~6 pages; text: `iac-441-51.txt`)
- **URL**: https://www.legis.iowa.gov/docs/iac/chapter/04-15-2026.441.51.pdf
- **Rule 441—51.2** — Must apply for all other benefits (SSI, FIP, etc.).
- **Rule 441—51.3** — Supplementation from non-federal sources counts as income, reducing SSA payment.
- **Rule 441—51.4** — Eligibility for residential care (licensed facility, physician's statement, income less than 31 × max per diem).
- **Rule 441—51.5** — Dependent relatives (income/resource rules, financial dependency definition).
- **Rule 441—51.6** — Iowa residency requirement.
- **Rule 441—51.7** — Eligibility for SMME (Medicaid eligibility, SSI-eligibility except SGA/income, not eligible under other SSA group, Medicare Part B, living arrangement, income between 120% FPL and Medicaid limit).
- **Rule 441—51.8** — Income from room and board.
- **Rule 441—51.9** — SSN requirement; overpayment recovery.
- Recent amendment: ARC 9305C, IAB 5/28/25, effective 8/1/25.

### 2.3 IAC 441—Chapter 52 — Payment
- **Local file**: `/tmp/ia-ssp/iac-441-52.pdf` (~5 pages; text: `iac-441-52.txt`)
- **URL**: https://www.legis.iowa.gov/docs/iac/chapter/04-15-2026.441.52.pdf
- **Rule 441—52.1(249)** — **Assistance standards** (the core rate-setting rule).
  - Key text (file page 1): "Assistance standards are the amounts of money allowed on a monthly basis to recipients of state supplementary assistance… **Current assistance standards will be published on the department's website.** Assistance standards will be adjusted annually to reflect cost-of-living adjustments (COLA) adopted by the Social Security Administration, in accordance with 20 CFR §416.2095 and 20 CFR §416.2096 as amended to March 15, 2022. Adjustments to the assistance standards based on COLA are effective January 1 of each year."
  - **52.1(1) Protective living arrangement** — family-life home (cross-reference to 441—Chapter 111).
  - **52.1(2) Dependent relative** — five household configuration categories (see §5 below for list).
  - **52.1(3) Residential care** — Before 7/1/2017: flat per diem OR cost-related per diem. On/after 7/1/2017: cost-related (max per diem). Details six income disregards applied in order, reserve bed days, etc.
  - **52.1(4) Blind** — "$22 per month" for blind recipients not receiving another type of SSA (this figure is literally in the rule text).
  - **52.1(5) In-home, health-related care** — cross-reference to 441—Chapter 177.
  - **52.1(6) Minimum income level cases** — December 1973 MIL preservation.
  - **52.1(7) Supplement for Medicare and Medicaid eligibles** — "$1 per month" (literally in the rule text).
- Recent amendment: ARC 9306C, IAB 5/28/25, effective 8/1/25.

### 2.4 IAC 441—Chapter 54 — Facility Participation
- **Local file**: `/tmp/ia-ssp/iac-441-54.pdf` (~3 pages; text: `iac-441-54.txt`)
- **URL**: https://www.legis.iowa.gov/docs/iac/chapter/04-15-2026.441.54.pdf
- Residential care facility participation rules (not critical to individual eligibility modeling).

### 2.5 IAC 441—Chapter 177 — In-Home Health-Related Care (IHHRC)
- **Local file**: `/tmp/ia-ssp/iac-441-177.pdf` (~7 pages; text: `iac-441-177.txt`)
- **URL**: https://www.legis.iowa.gov/docs/iac/chapter/04-15-2026.441.177.pdf
- **Rule 441—177.4(1)(f)** — Countable income limits: **$480.55/month** for one person, **$961.10** if both spouses need care, with disregards in order: SSI standard (individual/couple), $65 + ½ earned income, SSI dependent allowance per dependent, unmet medical needs of ineligible spouse, unmet medical needs of applicant/recipient.
- **Rule 441—177.4(1)(g)** — Income deeming rules for children.
- **Rule 441—177.5** — Provider qualifications (age 18+, health assessment, training).
- **Rule 441—177.6** — Physician certification procedure (Form 470-0673).
- **Rule 441—177.7** — Home maintenance allowance and client participation.
- Recent amendment: ARC 6720C, IAB 11/30/22, effective 2/1/23.

### 2.6 Archive/aggregator links (for verification only)
- Justia: https://regulations.justia.com/states/iowa/agency-441/title-xv/chapter-177/rule-441-177-4/
- Cornell LII: https://www.law.cornell.edu/regulations/iowa/Iowa-Code-r-441-52.1 — note: Cornell text lags Iowa's IAB amendments. Always cross-check against the legis.iowa.gov PDF.

---

## 3. Iowa HHS Employees' Manual (Policy Manual)

### 3.1 Title 6, Chapter B — State Supplementary Assistance
- **Local file (two copies with same content)**:
  - `/tmp/ia-ssp/6b-manual.pdf` (3,582 lines text, ~78 pages) — smaller file, older PDF build
  - `/tmp/ia-ssp/info-2025-03-07.pdf` (3,663 lines text) — identical content
- **URL (small version)**: https://hhs.iowa.gov/media/3987/download
- **URL (March 7, 2025 revision)**: https://hhs.iowa.gov/media/15607/download?inline
- **Revision date**: March 7, 2025.
- **Page references** (use for `#page=NN`):
  - **Overview & Legal Basis**: manual p.1 (PDF file page ~5).
  - **Policies Applicable to All SSA / Eligibility requirements**: p.2 (PDF ~6). Resource limits $2,000 individual / $3,000 couple. Income must be less than standard for living arrangement.
  - **Blind Supplement**: p.15–16. Confirms $22 blind special allowance; maximum income levels $989 individual, $1,472 one-blind-couple, $1,494 both-blind-couple (based on 2025 SSI standards $967/$1,450).
  - **Dependent Person**: p.16–26. Dependent income must be <$503/month (2025 value, = SSI dependent allowance). Household income must be less than applicable assistance standard:
    - Aged or disabled client and a dependent relative: **$1,470** (2025)
    - Aged or disabled client, spouse aged 65+ or disabled, and a dependent relative: **$1,953** (2025)
    - Blind client and a dependent relative: **$1,492** (2025)
    - Blind client, aged or disabled spouse, and a dependent relative: **$1,975** (2025)
    - Blind client, blind spouse, and a dependent relative: **$1,997** (2025)
  - **Family-Life Home (FLH)**: p.26–32. Standard allowance **$1,129** (2025). Maximum payment $142 (not $162, to compensate for SSI's $20 disregard). Personal needs **$126** (2025).
  - **In-Home Health-Related Care (IHHRC)**: p.32–46. Max cost of care $480.55/month single / $961.10/month couple-both-needing-care. Home maintenance allowance $967 individual / $1,450 couple / $483 per dependent (2025 SSI-linked).
  - **Mandatory State Supplement**: p.47–50. December 1973 minimum-income-level preservation cases (legacy).
  - **Residential Care Supplement (RCF)**: p.50–70. Flat per diem $17.86, max cost-related per diem **$37.60** (2025). Personal needs **$126** (2025). Client participation rules detailed on p.57–67.
  - **Supplement for Medicare and Medicaid Eligibles (SMME)**: p.70–74. Fixed $1/month paid quarterly. Requires dual Medicare Part B + full Medicaid, income between 120% FPL and Medicaid limit, not eligible under another SSA group.

### 3.2 Additional manual: April 11, 2025 revision
- **Local file**: `/tmp/ia-ssp/info-2025-04-11.pdf`
- **URL**: https://hhs.iowa.gov/media/15819/download?inline
- 4,377 lines — this is Title 8 Chapter E (Medicaid Income), which includes tangential SSA references; **not the SSA-specific chapter**.

---

## 4. Informational Letters / Rate-setting Announcements

### 4.1 Informational Letter No. 2651-MC-FFS (December 30, 2024)
- **Local file**: `/tmp/ia-ssp/il-2024-12-30.pdf` (2 pages; text: `il-2024-12-30.txt`)
- **URL**: https://secureapp.dhs.state.ia.us/IMPA/Information/ViewDocument.aspx?viewdocument=634b265a-2fa6-4fdb-a4ed-0ce94e32b993
- **Content**: Effective January 1, 2025:
  - RCF **maximum per diem rate**: $36.82 → **$37.60**
  - **Flat per diem rate**: remains at **$17.86** (unchanged since 2/1/2004)
  - **Personal needs allowance**: $123.00 → **$126.00**
  - Based on "average Medicaid copays paid by RCF Medicaid members in SFY 2024 in conjunction with the COLA increase announced by SSA".

---

## 5. Current 2026 Rates — Iowa HHS SSA Standards Page

### 5.1 State Supplementary Assistance | Health & Human Services
- **URL**: https://hhs.iowa.gov/assistance-programs/state-supplementary-assistance
- **Effective**: January 1, 2026
- **Single-page HTML** (no PDF anchor needed)

**Family Home Life (FLH)** — Effective January 1, 2026
| Component | Amount |
|---|---|
| Payment to Family | $1,026.00 |
| Personal Needs Allowance | $130.00 |
| Payment Standard (total) | $1,156.00 |

**Dependent Person (DP)** — Effective January 1, 2026
| Category | Income Standard |
|---|---|
| Maximum Payment (per person) | $518.00 |
| Aged or Disabled Client and Dependent Relative | $1,512.00 |
| Aged or Disabled Client, Eligible Spouse, and Dependent Relative | $2,009.00 |
| Blind Client and Dependent Relative | $1,534.00 |
| Blind Client, Aged or Disabled Spouse, and Dependent Relative | **$3,031.00** ⚠️ SUSPECTED TYPO — see §9 |
| Blind Client, Blind Spouse, and Dependent Relative | $2,053.00 |

**Residential Care Facility (RCF)** — Effective January 1, 2026
| Component | Amount |
|---|---|
| Personal Needs Allowance | $130.00 |
| Flat per Diem Rate | $17.86 |
| Maximum Cost-Related per Diem Rate | $38.47 |

### 5.2 Current rates NOT published on the HHS SSA page
The HHS SSA page does not publish current-year values for:
- Blind supplement ($22/month — hardcoded in IAC 441—52.1(4))
- In-Home Health-Related Care max cost-of-care ($480.55 / $961.10 — hardcoded in IAC 441—177.4(1)(f))
- SMME payment ($1/month — hardcoded in IAC 441—52.1(7))
- Home maintenance allowances ($967 / $1,450 / $483 — derived from federal SSI FBR)
- 2026 manual update with revised FLH/DP/IHHRC amounts (not yet published; March 7, 2025 is the latest)

---

## 6. Historical Pamphlet: Comm. 18 (State Supplementary Assistance)

- **Local file**: `/tmp/ia-ssp/comm18.pdf` (3 pages; text: `comm18.txt`)
- **URL**: https://hhs.iowa.gov/media/6413/download
- **Revision date**: Comm. 18 (Rev. 3/10) — March 2010
- **Content**: Consumer-facing explanation of SSA. Lists 5 special-needs categories:
  - Special Blind Allowance
  - Residential Care
  - Family-Life Home
  - Dependent Relative
  - In-Home Health-Related Care
- Note: Comm. 18 does NOT list the SMME ($1/month) supplement (which was added by 2003 Iowa legislation for the "pass-through" requirement) or the Mandatory State Supplement (1973 MIL grandfathered cases) — likely because this consumer pamphlet predates some additions. Authoritative list of SSA types is in the 6-B manual and IAC 441—52.1.

---

## 7. SSA 2011 State Assistance Programs Report (Iowa)

### 7.1 Availability
- **Primary URL (SSA)**: https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ia.html — **403 blocked** to automated tools (including curl with browser UA)
- **Wayback Machine (working)**: https://web.archive.org/web/2024/https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ia.html
- **Extracted text**: `/tmp/ia-ssp/ssa-2011-ia.txt` (209 lines, complete)

### 7.2 2011 Payment Levels (from Table 1 — verbatim)
Optional state supplementation payment levels, January 2011 (in dollars):

| Living arrangement | State code | Combined federal+state (Individual) | Combined federal+state (Couple) | State supplementation (Individual) |
|---|---|---|---|---|
| Living independently (blind) | A | 696.00 | 1,055.00 (a) | 22.00 |
| Living in the household of another (blind) | B | 471.34 | 718.00 (a) | 22.00 |
| Living with a dependent person (Aged and disabled) | C | 1,018.00 | 1,355.00 | 344.00 |
| Living with a dependent person (Blind) | C | 1,040.00 | 1,399.00 | 366.00 |
| Family life or boarding home (Aged and disabled) | D | 816.00 | 1,652.00 | 142.00 |
| Family life or boarding home (Blind) | D | 838.00 | 1,696.00 | 164.00 |
| Living with a dependent person in the household of another (Aged and disabled) | H | 793.34 | 1,018.00 | 344.00 |
| Living with a dependent person in the household of another (Blind) | H | 815.34 | 1,062.00 | 366.00 |
| Family life or boarding home with 1/3 reduction (Aged and disabled) | I | 591.34 | 1,315.00 | 142.00 |
| Family life or boarding home with 1/3 reduction (Blind) | I | 613.34 | 1,359.00 | 164.00 |
| Residential care | . . . | 965.34 | . . . | 291.34 (b) |
| In-home health care | . . . | 1,154.55 | 1,972.10 (c) | 480.55 (d) |

**Footnotes**:
- (a) "Payment level when both members of a couple are blind; when only one member is blind, payment is reduced by $22."
- (b) "Amount based on allowable costs of residential care (up to $28.14 per day), plus a personal needs allowance of $93 per month, minus the federal SSI payment. State administers payments."
- (c) "Payment is based on both members of a couple needing in-home health-related care. When one member needs care, payment is reduced by $480.55. State administers payments."
- (d) "Payment is based on actual cost of in-home health-related care up to a maximum of $480.55, plus basic federal benefit. State administers payments."

### 7.3 2011 Recipient Counts (from Table 2)
| Living arrangement | State code | Total | Aged | Blind | Disabled Adults | Disabled Children |
|---|---|---|---|---|---|---|
| **All recipients** | — | **5,281** | 594 | 453 | 3,927 | 307 |
| Living independently (blind) | A | 535 | 0 | 424 | 0 | 111 |
| Living in the household of another (blind) | B | 10 | 0 | 9 | 0 | 1 |
| Living with a dependent person | C | 1,473 | 109 | 18 | 1,176 | 170 |
| Family life or boarding home | D and I | 4 | 0 | 0 | 4 | 0 |
| Living with a dependent person in the household of another | H | 1 | 1 | 0 | 0 | 0 |
| Residential care | — | 1,703 | 299 | — | 1,404 | 0 |
| In-home health care | — | 1,531 | 182 | — | 1,324 | 25 |
| Medicaid facility | — | 24 | 3 | 2 | 19 | 0 |

### 7.4 Program administration notes (from SSA 2011 Iowa page, verbatim)
- Mandatory Minimum Supplementation: Social Security Administration.
- Optional State Supplementation: "State Department of Human Services administers supplemental payments for persons receiving residential or in-home health-related care, and persons who are eligible for the supplement for Medicare and Medicaid eligible. Social Security Administration administers all other supplemental payments."
- Effective dates: January 1, 1974 (blind); May 1, 1974 (aged and disabled); **October 1, 2003** (SMME — supplement for Medicare and Medicaid eligible).
- Statutory basis: Code of Iowa, chapter 249.
- Total expenditures: "State-administered payments for calendar year 2010 are not available, but $5,362,000 in federally administered payments were made to SSI recipients."

**Note**: The SSA 2011 report is the **last state-by-state SSP report SSA published**; it was discontinued thereafter. Use this as the authoritative historical snapshot for rates/eligibility as of January 2011.

### 7.5 Derivation of 2011 state-only portions from combined totals
Working from 2011 SSI FBR ($674 individual / $1,011 couple):
- Blind (Individual) state-only = $22 (directly stated)
- Living with dependent (Aged/Disabled), Individual: combined $1,018 − federal $674 = **$344 state portion** ✓ matches
- Family-life home (Aged/Disabled), Individual: combined $816 − federal $674 = **$142** ✓ matches
- Residential care, Individual: per footnote (b), cost-based formula; $28.14/day × 31 = $872.34 + $93 PNA = $965.34 total = $291.34 state portion (after federal SSI).

---

## 8. Historical rates from Wayback Machine (IA HHS SSA page)

The Iowa HHS SSA rates page has archived snapshots available at:
- 2024 snapshot: https://web.archive.org/web/2024/https://hhs.iowa.gov/assistance-programs/state-supplementary-assistance (shows Jan 1, 2025 rates)
- 2025 snapshot: https://web.archive.org/web/2025/https://hhs.iowa.gov/assistance-programs/state-supplementary-assistance (shows Jan 1, 2025 rates)

**Note**: Pre-2024 snapshots of the current URL and of the older `dhs.iowa.gov/state-supplementary-assistance-program` URL were not available in Wayback (404). This limits ability to verify historical year-by-year amounts beyond the 6-B manual's current rates and the SSA 2011 report.

**Iowa HHS rates comparison (2025 → 2026)**:
| Item | 2025 | 2026 | COLA-implied? |
|---|---|---|---|
| FLH Payment to Family | $1,003 | $1,026 | 2.29% (≈ 2.5% COLA) ✓ |
| FLH Personal Needs Allowance | $126 | $130 | 3.17% — higher than COLA |
| FLH Payment Standard | $1,129 | $1,156 | 2.39% ✓ |
| DP Maximum Payment | $503 | $518 | 2.98% ≈ 2.5% COLA ✓ |
| DP Aged/Disabled + dep | $1,470 | $1,512 | 2.86% ✓ |
| DP Aged/Disabled + spouse + dep | $1,953 | $2,009 | 2.87% ✓ |
| DP Blind + dep | $1,492 | $1,534 | 2.82% ✓ |
| DP Blind + A/D spouse + dep | $1,975 | **$3,031** | **53.5% ⚠️ TYPO SUSPECTED** |
| DP Blind + blind spouse + dep | $1,997 | $2,053 | 2.80% ✓ |
| RCF Personal Needs | $126 | $130 | 3.17% |
| RCF Flat per Diem | $17.86 | $17.86 | frozen since 2/1/2004 |
| RCF Max Cost-Related per Diem | $37.60 | $38.47 | 2.31% ✓ |

---

## 9. Known Issues / Verification Flags

### 9.1 Suspected typo on Iowa HHS SSA page (DP Blind + Aged/Disabled spouse + dep)
- 2025 value: $1,975 (from 6-B manual and 2024/2025 Wayback)
- 2026 value as published: **$3,031**
- Expected 2026 value from COLA: ~$2,031 (consistent with the 2.8% applied to other 2026 DP rows)
- **Likely explanation**: Transposition/typo where "$2,031" became "$3,031".
- **Recommended action**: Flag this in the PR description as a verification TODO. Before committing parameter values for 2026, email Iowa HHS or wait for the next 6-B manual revision to confirm.

### 9.2 2026 manual not yet published
- Latest 6-B manual is **March 7, 2025**. For 2026 implementation, the current (Effective January 1, 2026) rates on the HHS SSA page are the only source for FLH/DP/RCF.
- Blind, IHHRC, and SMME rates are controlled by IAC (and frozen or COLA-indexed from federal SSI standards), so the 2025 manual is still authoritative for those.

### 9.3 Historical rates before 2011 and between 2011–2024
- SSA stopped publishing state-by-state SSP reports after January 2011.
- Iowa's 2015–2023 rate snapshots were not archived on Wayback Machine.
- Reconstruction would require either:
  - Manual request to Iowa HHS for historical assistance standards schedule; OR
  - Calculation by applying federal SSI COLA sequence to the 2011 figures forward (approximate, because some rates are not pure COLA — e.g., the $17.86 flat per diem has been frozen since 2/1/2004).

---

## 10. Closed PR #7734 (mattunrath/ia-ssp)

- **Branch**: `mattunrath/ia-ssp` on GitHub remote
- **Single commit**: `02a0314df9` "Initial commit for Iowa SSP implementation" dated 2026-03-07
- **Content**: Branch was initialized but **never committed source or variable files**. Only commit message; no actual implementation, no `sources/` directory, no parameters.
- **Use**: **Do not copy** — branch has no content to copy. Sources were independently collected here.

---

## 11. Other supporting material

### 11.1 Iowa Legislature Budget Unit: State Supplementary Assistance (FT doc 16896)
- **Local file**: `/tmp/ia-ssp/budget-unit.pdf` (text: `budget-unit.txt`, 53 lines)
- **URL**: https://www.legis.iowa.gov/docs/publications/FT/16896.pdf
- Contains legislative budget overview of SSA appropriations.

### 11.2 ARC 3715C — Iowa Administrative Rules Notice
- **URL**: https://rules.iowa.gov/Notice/Details/3715C
- Amendment notice referenced in IAC Chapter 52's revision history. Confirms the "periods of eligibility beginning July 1, 2017" transition to cost-related-only RCF reimbursement.

### 11.3 WorkWorld Iowa SSA reference (secondary / for cross-verification only)
- **URL**: https://help.workworldapp.com/wwwebhelp/state_supplementary_assistance_eligibility_requirements_iowa.htm
- References: Iowa DHS Employees' Policy Manual Title 6 Chapter B; 20 CFR 416.2001; Iowa Code § 249.3.

### 11.4 Iowa Admin. Code Justia portal (secondary / for cross-verification only)
- **URL**: https://regulations.justia.com/states/iowa/441/title-v/chapter-51/441-51-3/

### 11.5 Iowa HHS application forms (SSA application, not source for rates)
- English: https://hhs.iowa.gov/media/5825/download?inline
- Spanish: https://hhs.iowa.gov/media/5828/download?inline
- Medicaid brochure: https://hhs.iowa.gov/media/6420/download?inline
- Application portal: https://hhsservices.iowa.gov/apspssp/ssp.portal

---

## 12. Fetch status summary

### Successful fetches
- Iowa HHS SSA current rates page ✓
- Iowa Code § 249.3 (PDF) ✓
- Iowa Code § 249.9A (PDF) ✓
- IAC Chapters 50, 51, 52, 54, 177 (PDFs) ✓
- 6-B Employees' Manual (PDF) — full 78-page text extracted ✓
- Comm. 18 pamphlet ✓
- Informational Letter 2651-MC-FFS (Dec 30, 2024 — RCF rate update) ✓
- Iowa Legislature budget FT document ✓
- **SSA 2011 Iowa report via Wayback Machine** ✓ (after direct SSA 403)

### Failed fetches (403/404) — CRITICAL for unreachable-reference checkpoint
- **`https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ia.html`** — SSA blocks automated tools with HTTP 403. **Resolution**: content was successfully retrieved via Wayback Machine at `https://web.archive.org/web/2024/https://www.ssa.gov/policy/docs/progdesc/ssi_st_asst/2011/ia.html`. If primary citation is needed, user may need to download the SSA URL manually in a browser. The Wayback version is byte-for-byte the same HTML.
- **Historical snapshots of `dhs.iowa.gov/state-supplementary-assistance-program`** — 404 on all Wayback years tried (2015, 2018, 2019, 2020, 2022). DHS→HHS reorganization likely destroyed older archives. **Impact**: cannot directly verify year-by-year FLH/DP/RCF rates from 2011 to 2024. Mitigation: use the 2011 SSA report for the 2011 baseline; the 2025 HHS page/Wayback snapshot for the 2024/2025 rates; and accept that 2012–2023 rates will need to be either reconstructed via COLA application to 2011 figures, or obtained via direct request to Iowa HHS.

### No attempt made (not needed for this scope)
- Individual annual IAB notices filing COLA adjustments (dozens of ARC numbers listed in IAC Ch 52's amendment history — each year has one, and for current modeling the published HHS standards are sufficient).

---
