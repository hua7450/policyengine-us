# California CalWORKs - Reference URL Audit

## Summary

Audited all reference URLs in CalWORKs cash and child care parameter files. Found **1 broken URL** (typo), **multiple http URLs** that should be https, and **reference quality concerns** (county-level sources used where state-level CDSS sources exist).

---

## Critical Issues

### 1. BROKEN URL (Typo)
**File:** `resources/sources.yaml` (line 9)
```
href: http://epolicy.dpss.lacounty.gopv/epolicy/...
```
**Issue:** Domain has typo `lacounty.gopv` instead of `lacounty.gov`
**Fix:** Change `gopv` to `gov`

---

## Reference Quality Issues

### 2. HTTP URLs Should Be HTTPS
All LA County ePolicies links use `http://` instead of `https://`. The site now redirects to https. Files affected:
- `income/sources/earned.yaml`
- `income/sources/db_unearned.yaml`
- `income/sources/other_unearned.yaml`
- `exempt.yaml`
- `region1_counties.yaml`
- `income/monthly_limit/region1/main.yaml`
- `income/monthly_limit/region2/main.yaml`
- `income/monthly_limit/region1/additional.yaml`
- `income/monthly_limit/region2/additional.yaml`
- `income/disregards/applicant/flat.yaml`
- `income/disregards/recipient/flat.yaml`
- `income/disregards/recipient/percentage.yaml`
- `resources/limit/without_elderly_or_disabled_member.yaml`
- `resources/limit/with_elderly_or_disabled_member.yaml`
- `resources/limit/age_threshold.yaml`
- `resources/limit/vehicle.yaml`
- All child_care parameter files

**Recommendation:** Change all `http://epolicy.dpss.lacounty.gov` to `https://epolicy.dpss.lacounty.gov`

### 3. County ePolicies URLs Are Fragile
Most references use LA County DPSS ePolicies with long hash fragment URLs like:
```
http://epolicy.dpss.lacounty.gov/epolicy/epolicy/server/general/projects_responsive/ePolicyMaster/index.htm?&area=general&type=responsivehelp&ctxid=&project=ePolicyMaster#t=mergedProjects%2FCalWORKs%2FCalWORKs%2F44-111_23_Earned_Income_Disregards%2F44-111_23_Earned_Income_Disregards.htm%23Policybc-2&rhtocid=_3_1_6_2_1
```

**Issues:**
- These are county-level interpretive guides, not primary regulatory sources
- URL format is fragile (session-based hash fragments)
- The same DPSS ePolicies site was recently migrated to a new URL structure:
  - Old: `http://epolicy.dpss.lacounty.gov/epolicy/...`
  - New: `https://my.dpss.lacounty.gov/public/en/home/epolicy/...`

**Recommendation:** Add WIC statutory citations and CDSS ACL references as primary sources; keep county ePolicies as secondary/supplementary.

### 4. San Diego County PDF Reference May Be Outdated
**Files:** All 4 MAP payment files + max_au_size.yaml
```
href: https://hhsaprogramguides.sandiegocounty.gov/CalWORKS/44-300/CalWORKs_Payment_Standards/G_CalWORKs_Payment_Standards.pdf
```
**Issue:** County program guide PDFs are frequently updated/moved. Already supplemented with ACL 24-55 reference, which is good.

### 5. ACL 24-55 Reference Needs Verification
**Files:** All 4 MAP payment files
```
href: https://cdss.ca.gov/Portals/9/Additional-Resources/Letters-and-Notices/ACLs/2024/24-55.pdf?ver=2024-08-19-162608-673#page=7
```
**Concern:** Earlier search suggested ACL 24-55 may actually be about CalFresh/SNAP changes, not CalWORKs MAP. The CalWORKs MAP increase ACL may be a different number. Need to verify this is the correct ACL with payment standard tables on page 7.

---

## Recommended Reference Additions

For CalWORKs cash parameters, add these primary regulatory sources:

### Statutes (permanent):
- WIC 11450 (MAP base amounts): `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=11450.&lawCode=WIC`
- WIC 11450.025 (COLA trigger): `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=11450.025.&lawCode=WIC`
- WIC 11450.12 (Applicant EID): `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=11450.12.&lawCode=WIC`
- WIC 11451.5 (Recipient EID): `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=11451.5.&lawCode=WIC`
- WIC 11452 (MBSAC): `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=11452.&lawCode=WIC`
- WIC 11453 (COLA mechanism): `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=11453.&lawCode=WIC`

### CDSS ACLs (for specific date entries):
- ACL 24-37 (MBSAC COLA 07/01/2024): `https://www.cdss.ca.gov/Portals/9/Additional-Resources/Letters-and-Notices/ACLs/2024/24-37.pdf`
- ACL 24-54 (Resource limits): `https://cdss.ca.gov/Portals/9/Additional-Resources/Letters-and-Notices/ACLs/2024/24-54.pdf`
- ACL 24-36 (Vehicle limit): Already referenced correctly
- ACL 25-65 (Resource limits 2026): `https://www.cdss.ca.gov/Portals/9/Additional-Resources/Letters-and-Notices/ACLs/2025/25-65.pdf`

---

## Files with NO Issues
The following reference URLs appear correct and well-formed:
- `resources/limit/vehicle.yaml` - Multiple good references including ACL 24-36
- `resources/limit/without_elderly_or_disabled_member.yaml` - ACL 24-54 reference with page number
- `resources/limit/with_elderly_or_disabled_member.yaml` - ACL 24-54 reference with page number
- All MAP payment files - ACL reference with page number (pending ACL 24-55 verification)
