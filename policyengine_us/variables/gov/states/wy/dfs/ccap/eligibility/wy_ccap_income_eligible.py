from policyengine_us.model_api import *


class wy_ccap_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Income eligible for Wyoming Child Care, Purchase of Service"
    definition_period = MONTH
    defined_for = StateCode.WY
    reference = (
        "https://drive.google.com/file/d/1yatL28Yylj62R2cTipV2sGa10TxZplxr/view",  # Wyo. Admin. Rules, DFS, Child Care - Purchase of Service, Ch. 1 §8(e)(i)(N) and Appendix A, eff. 05/07/2025 (PDF pp. 18, 37)
        "https://drive.google.com/file/d/1XlBkvgwQuX-rIL3eYjkPog1zZ-hi-gD7/view",  # Wyoming DFS Child Care Subsidy Policy Manual §1101.A (PDF p. 1)
        "https://drive.google.com/file/d/1VpQ4WE2xQZ_byLcfJgmtyYyBiKr3_ytS/view",  # Wyoming DFS Child Care Subsidy Policy Manual §1201 (PDF p. 1)
    )

    def formula(spm_unit, period, parameters):
        # Manual §1101.A: an initial application must fall at Sliding Fee
        # Scale Step 4 or below (175% of the federal poverty guideline).
        # Manual §1201: a unit already receiving assistance may continue
        # through Steps 5-6 (up to 225%) when gross income increased due to
        # employment with no 30-or-more-day break in aid; the wy_ccap_enrolled
        # input proxies continuing-recipient status, and the employment-driven
        # income-increase and break-in-aid conditions are not tracked. The
        # Table I bands equal the guideline times the step multiplier, so the
        # limits self-uprate; each chart takes effect April 1 while
        # spm_unit_fpg applies the calendar-year guideline, a three-month
        # timing simplification.
        p = parameters(period).gov.states.wy.dfs.ccap.income
        countable_income = spm_unit("wy_ccap_countable_income", period)
        fpg = spm_unit("spm_unit_fpg", period)
        enrolled = spm_unit("wy_ccap_enrolled", period)
        fpg_share = where(enrolled, p.fpl_limit.continued, p.fpl_limit.initial)
        income_eligible = countable_income <= fpg * fpg_share
        # Manual §502: POWER and Tribal TANF recipients are categorically
        # eligible.
        tanf_enrolled = spm_unit("is_tanf_enrolled", period)
        return income_eligible | tanf_enrolled
