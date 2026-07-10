# Oregon Employment Related Day Care (ERDC) working references

## Official Program Name

**Federal Program**: Child Care and Development Fund (CCDF)
**State's Official Name**: Employment Related Day Care (ERDC)
**Abbreviation**: ERDC
**Agency**: Oregon Department of Early Learning and Care (DELC)
**Source**: OAR 414-175-0001 and Oregon DELC ERDC program page

**Variable Prefix**: `or_erdc`

## Primary sources

1. [OAR Chapter 414, Division 175](https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=7871) — current ERDC administrative rules, including June 1, 2026 amendments.
2. [Oregon DELC ERDC program page](https://www.oregon.gov/delc/programs/pages/erdc.aspx) — public eligibility summary, current waitlist, and March 2026 income standards.
3. [Oregon DELC ERDC copays and billing](https://www.oregon.gov/delc/programs/pages/copays-billing.aspx) — copay and allowable-cost overview.
4. [Oregon DELC ERDC maximum rates](https://www.oregon.gov/delc/programs/pages/rates.aspx) — current 2026 rate tables and ZIP-code areas.
5. [Oregon Programs Eligibility Notebook (OPEN), July 2026](https://sharedsystems.dhsoha.state.or.us/DHSForms/Served/de2818.pdf#page=215) — operational guidance on categorical ERDC; PDF file pages 215-217.

## Verified rule map

- OAR 414-175-0015: ERDC filing, financial, need, and benefit groups; the PolicyEngine SPM unit is the closest available entity but is an approximation.
- OAR 414-175-0020: Oregon residency and immunization requirements. State scoping models residency; immunization verification is administrative.
- OAR 414-175-0021: child citizenship/noncitizen requirements applied only until May 1, 2024, so current ERDC does not require an immigration test.
- OAR 414-175-0022: eligible children are under age 13, or under age 18 with specified special circumstances.
- OAR 414-175-0023: every caretaker must work, attend qualifying education, or be on medical leave; exceptions cover a second caretaker unable to provide care and supervised contact. Categorically eligible families bypass the ordinary activity test and copay.
- OAR 414-175-0025: TANF and Expanded Child Welfare are categorical pathways. TANF waives child-care need; Expanded Child Welfare also excludes income. Both retain the resource ceiling and other federal requirements.
- OAR 414-175-0030: available assets are countable unless specifically excluded; gross income is used, with enumerated unavailable-income rules.
- OAR 414-175-0035: income-source treatment. Relevant modeled sources include wages, self-employment net of permitted costs, interest, dividends, rent, pensions, Social Security, SSI, unemployment, workers compensation, spousal support, veterans benefits, and TANF. Many narrow statutory payments lack exact PolicyEngine variables.
- OAR 414-175-0040: prospective monthly budgeting; Expanded Child Welfare income is not countable.
- OAR 414-175-0050(1): resources above $1,000,000 are ineligible. Initial monthly income must be strictly below 200% FPL. Ongoing/recertification income must be strictly below the greater of 250% FPL or 85% SMI. Group size is capped at eight.
- OAR 414-175-0050(3): March 2026 monthly copays are schedules for group sizes two through eight or more; categorical and specified transition/leave circumstances can waive them.
- OAR 414-175-0050(2): allowable cost is the lesser of billed cost and the applicable provider-rate cap; the subsidy is allowable cost less copay.
- OAR 414-175-0075: 2026 provider rates vary by Area A/B/C, provider category, child age, and hourly/part-time/monthly billing. Payable hours and special circumstances add further caps.
- OAR 414-175-0076: high-needs supplements require an administratively assessed score and supporting documentation.

## 2026 standards

- Initial monthly limits at 200% FPL, sizes 2-8+: $3,607; $4,554; $5,500; $6,447; $7,394; $8,340; $9,287.
- Ongoing monthly 85% SMI values, sizes 2-8+: $5,926; $7,321; $8,715; $10,109; $11,504; $11,765; $12,026.
- Ongoing monthly 250% FPL values, sizes 2-8+: $4,509; $5,692; $6,875; $8,059; $9,242; $10,425; $11,609.
- The copay schedule is effective March 1, 2026 and ranges from $0 to $130 depending on size and countable monthly income.
- Licensed, NQC, and QEC rate tables are effective January 1, 2026; license-exempt FAM and QFM rates are effective March 1, 2026.

## Known source and modeling issues

- OAR 414-175-0050(3)(b)(A)(v) contains an apparent typo (`$34,057.99`); the contiguous schedule and next bracket show that the intended upper boundary is $4,057.99. The implementation should encode bracket starts, avoiding reliance on the typo.
- The OPEN PDF initially failed through the web fetcher but was successfully downloaded directly, text-extracted, and relevant pages rendered at 300 DPI under `/tmp/or-ccap-sources/`.
- The waitlist, provider approval, immunization verification, unpaid-copay history, certification-period protections, and administratively assessed special circumstances are not inferable from survey inputs.
- Exact self-employment gross receipts and separately permitted business costs are not both available. The closest modeled amount is net self-employment income.
- ERDC includes TANF as countable income, but the calculated `tanf` variable is commented out of the source list because adding it would create a child care/TANF circular dependency.
- Provider rate area is a direct Area A/B/C Enum input in this PR; automatic ZIP-code mapping is deferred to a follow-up PR.
