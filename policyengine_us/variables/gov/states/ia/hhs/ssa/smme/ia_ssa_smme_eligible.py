from policyengine_us.model_api import *


class ia_ssa_smme_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Iowa SSA SMME eligible"
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.51.pdf#page=2",
        "https://www.legis.iowa.gov/docs/code/249.3.pdf",
    )

    def formula(person, period, parameters):
        aged_or_disabled = person("is_ssi_aged_blind_disabled", period.this_year)
        has_medicaid = person("ia_ssa_has_full_medicaid", period)
        has_medicare = person("ia_ssa_has_medicare_part_b", period)
        # IAC 441—51.7(6): income must exceed 120% of the federal poverty
        # level. SMME is a $1 technical SSP pathway for people categorically
        # SSI-eligible but income-ineligible, so the FPL floor is what
        # distinguishes them from regular SSI recipients.
        p = parameters(period).gov.states.ia.hhs.ssa
        countable_monthly = (
            person("ssi_countable_income", period.this_year) / MONTHS_IN_YEAR
        )
        fpg_monthly = person.spm_unit("spm_unit_fpg", period.this_year) / MONTHS_IN_YEAR
        income_above_fpl_floor = (
            countable_monthly > p.smme.minimum_income_fpl_multiplier * fpg_monthly
        )
        return aged_or_disabled & has_medicaid & has_medicare & income_above_fpl_floor
