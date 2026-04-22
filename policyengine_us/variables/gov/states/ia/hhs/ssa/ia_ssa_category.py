from policyengine_us.model_api import *


class IASSACategory(Enum):
    RCF = "Residential care facility"
    IHHRC = "In-home health-related care"
    FLH = "Family-life home"
    DP = "Dependent person"
    BLIND = "Blind"
    SMME = "Supplement for Medicare and Medicaid eligibles"
    NONE = "Not in an Iowa SSA category"


class ia_ssa_category(Variable):
    value_type = Enum
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA category"
    possible_values = IASSACategory
    default_value = IASSACategory.NONE
    defined_for = StateCode.IA
    reference = "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.52.pdf"

    def formula(person, period, parameters):
        eligible = person("ia_ssa_eligible", period)
        p = parameters(period).gov.states.ia.hhs.ssa
        # Monthly SSI countable income and federal SSI payment; both source
        # variables are annual, so divide by 12 for use in monthly formulas.
        countable_monthly = (
            person("ssi_countable_income", period.this_year) / MONTHS_IN_YEAR
        )
        ssi_monthly = person("ssi", period.this_year) / MONTHS_IN_YEAR
        # Iowa-administered RCF client participation uses total monthly income
        # (SSI countable + federal SSI payment), not the |FBR − income| V-shape.
        total_rcf_income = countable_monthly + ssi_monthly
        in_rcf = person("ia_ssa_resides_in_residential_care_facility", period)
        client_participation = max_(
            0, total_rcf_income - p.rcf.personal_needs_allowance
        )
        rcf_income_threshold = p.rcf.days_multiplier * p.rcf.max_per_diem
        rcf_income_eligible = client_participation < rcf_income_threshold
        needs_ihhrc = person("ia_ssa_needs_in_home_health_related_care", period)
        both_need_care = person("ia_ssa_ihhrc_both_need_care", period)
        # IAC 441—177.4(1)(f): countable income of the individual and spouse
        # living in the home shall be limited to $480.55 per month if one needs
        # care or $961.10 (combined) if both need care.
        couple_countable = person.marital_unit.sum(countable_monthly)
        ihhrc_income_eligible = where(
            both_need_care,
            couple_countable <= p.ihhrc.max_cost_couple,
            countable_monthly <= p.ihhrc.max_cost_single,
        )
        in_flh = person("ia_ssa_resides_in_family_life_home", period)
        # IAC 441—177.4(1)(c): IHHRC recipients must live in their own home,
        # so exclude those residing in an RCF or family-life home.
        in_own_home = ~in_rcf & ~in_flh
        has_dependent = person("ia_ssa_dp_has_eligible_dependent", period)
        dp_configuration = person("ia_ssa_dp_configuration", period)
        in_dp = dp_configuration != dp_configuration.possible_values.NONE
        is_blind = person("is_blind", period.this_year)
        # IAC 441—52.1(4) blind standard is a federally-administered SSP;
        # supplement phases to zero when countable income reaches FBR +
        # state standard. Mirror that ceiling in the category gate so blind
        # recipients with excess income fall through to the next category.
        fbr = parameters(period).gov.ssa.ssi.amount.individual
        blind_income_eligible = countable_monthly < fbr + p.blind
        smme_eligible = person("ia_ssa_smme_eligible", period)
        return select(
            [
                eligible & in_rcf & rcf_income_eligible,
                eligible & needs_ihhrc & in_own_home & ihhrc_income_eligible,
                eligible & in_flh,
                eligible & has_dependent & in_dp,
                eligible & is_blind & blind_income_eligible,
                eligible & smme_eligible,
            ],
            [
                IASSACategory.RCF,
                IASSACategory.IHHRC,
                IASSACategory.FLH,
                IASSACategory.DP,
                IASSACategory.BLIND,
                IASSACategory.SMME,
            ],
            default=IASSACategory.NONE,
        )
