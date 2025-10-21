# Connecticut TFA - Eligibility Requirements

## Source
Connecticut TANF State Plan 2024-2026, Section A, Part I, Overview and A.1 (Pages 9-12)

## Demographic Eligibility

### Dependent Child Definition

A dependent child must meet ONE of the following age criteria:

1. **Under 18 years of age**, OR
2. **Age 18** and attending secondary school or its equivalent, OR
3. **Under age 24** and attending post-secondary school AND considered a dependent student through the Free Application for Federal Student Aid (FAFSA) process, OR
4. **Under age 25** and participating in a TANF job training or subsidized employment program

**Source**: TANF State Plan p. 9

### Caretaker Relative Definition

A caretaker relative is a relative who cares for and supervises the dependent child.

**Who qualifies**:
- Parent (custodial or non-custodial)
- Other person related by blood, adoption, or marriage to the child
- Another adult acting in loco parentis
- Legal guardians

**Note**: Any relative may receive assistance for a child, including legal guardians and others acting in loco parentis.

**Source**: TANF State Plan p. 9, 12

### Pregnant Women

- Pregnant women are eligible for assistance **throughout the entire pregnancy**
- This is explicitly stated eligibility from conception through delivery

**Source**: TANF State Plan p. 9, 12

## Categorical Eligibility Requirements

### Needy Family Definition

Connecticut defines a "needy family" as:
- A family with gross income less than **75% of Connecticut's median income level**

**Exception**: For TFA cash assistance program, more restrictive income limits apply (see income_limits.md)

The family must include:
- A dependent child (as defined above), AND
- A caretaker relative

**Source**: TANF State Plan p. 9

### Residence Requirement

- Applicants must **live in Connecticut**
- No specific duration of residence required (cannot have durational residence requirements under federal law)

**Source**: TANF State Plan p. 9 (inferred from eligibility criteria)

### Citizenship and Immigration Status

**Citizens**: Eligible if meeting all other criteria

**Non-Citizens**: Connecticut provides assistance to:
- Mandatory qualified aliens (as defined in Title IV of P.L. 104-193)
- Optional qualified aliens (as defined in Title IV of P.L. 104-193)

**Requirements for Non-Citizens**:
- All eligibility requirements that apply to U.S. citizens also apply to qualified aliens
- Benefits and provisions are the same
- **Must pursue citizenship** to the extent possible

**Exemptions from citizenship pursuit requirement**:
- Victims of domestic violence
- Persons with developmental disabilities or other mental impairment

**Source**: TANF State Plan p. 43, Section B Part II

### Living Arrangement Requirements

**Child must live with a related adult** or an adult who has filed for guardianship

**Absence from home**:
- Assistance denied if minor child has been, or is expected to be, **absent from home for more than 180 consecutive days**

**Good cause exception**:
- Split custody situations where child is absent up to half calendar year (183 days)

**Source**: TANF State Plan pp. 9, 49 (Section B Part VII)

## Time-Limited vs. Exempt Families

### Time-Limited Families (Non-Exempt)

Families subject to time limits must have at least one non-exempt adult.

### Exempt Families

A person is exempt from time limits and work requirements if they meet ANY of the following criteria:

1. **Incapacitated** - Cannot work due to medical condition
2. **Age 60 or older**
3. **Non-parent caretaker relative who does not receive assistance** (e.g., grandparent caring for child but not receiving benefits for themselves)
4. **Pregnant** - if a physician has certified that she is unable to work
5. **Post-partum** - for six weeks after delivery, or longer if physician certifies unable to work
6. **Unemployable** - As determined by the state
7. **Minor parent** - Attending and satisfactorily completing high school or high school equivalency program

### Connecticut State-Only Exemptions

These exemptions apply to state time limits but **NOT** to the federal 60-month limit:

1. **Caring for an incapacitated household member**
2. **Caring for a child under the age of one** (after the first six weeks post-partum)

**Note**: When exemptions extend benefits beyond 60 months due to these state-only exemptions, Connecticut uses state funds to pay for those months. If the family moves to another state, these months are reported as non-exempt months.

**Source**: TANF State Plan pp. 11-12

## Special Populations

### "Certain Exempt" Families (Solely State Funded)

Effective October 1, 2008: TFA families where **all adults are exempt** based on one of the following criteria are funded outside of TANF in a solely state-funded program:

- Incapacitated
- Age 60 or older
- Pregnant (physician-certified unable to work)
- Post-partum (physician-certified unable to work)
- Unemployable

**Source**: TANF State Plan p. 12

### Two-Parent Families

**Federal Definition Two-Parent Cases** (45 CFR 261.24):
- Funded as Solely State Funded (SSF) program
- No longer part of federal TANF program
- Not claimed as separate state program

**Other two-parent families** (not meeting federal 45 CFR 261.24 definition):
- Continue to be part of TANF program
- Subject to standard TFA eligibility and rules

**Source**: TANF State Plan p. 9

### Domestic Violence Survivors

Families that include a member who has been battered or subject to extreme cruelty:
- Considered a **hardship case** for TANF-funded benefits
- Can receive benefits **beyond the 60-month federal limit**
- State has established screening procedures for domestic violence, sexual assault, and stalking

**Source**: TANF State Plan pp. 12, 48 (Section B Part VI)

## Application Process Requirements

### Employment Services Assessment

**Before benefits are granted**:
- Applicants must attend the **initial employment services assessment intake session**
- Purpose: Further employment assessment and plan development
- Exception: Exempt individuals may not be required to attend

**Source**: TANF State Plan p. 10

### Standard of Promptness

- **45 days** from date of application for inactive cases
- **30 days** for extension applications (if applying before end of Jobs First time limit or current extension)

**Source**: TANF State Plan p. 44 (Section B Part III)

## Periodic Reviews

**Continuing eligibility reviews**:
1. After **12 months** of continuous assistance
2. In the **20th month** of the time limit (through March 31, 2024)
3. In the **35th month** of the time limit (effective April 1, 2024, when Jobs First limit increases to 36 months)

**Source**: TANF State Plan p. 44

## Implementation Notes

### Federal Baseline Alignment

**Connecticut's eligibility requirements align with federal TANF baseline for**:
- ✓ Age thresholds (under 18, or 18 and in school)
- ✓ Pregnant women eligibility
- ✓ Immigration/citizenship (qualified aliens)
- ✓ Caretaker relative definitions

**State-specific additions**:
- Age 24 exception for post-secondary students (dependent through FAFSA)
- Age 25 exception for job training/subsidized employment participants
- 180-day absence rule (more generous than federal minimum 45 days)
- State-only exemptions for caring for incapacitated member or child under one

### PolicyEngine Implementation

For a **simple TANF implementation**, can use:
- `is_demographic_tanf_eligible` (federal baseline) - covers age thresholds and pregnant women
- `is_citizen_or_legal_immigrant` (federal baseline) - covers citizenship requirements

**Custom state implementation needed for**:
- Income limits (see income_limits.md)
- Time limit tracking (see time_limits.md)
- Work requirement exemptions (if modeling work requirements)
