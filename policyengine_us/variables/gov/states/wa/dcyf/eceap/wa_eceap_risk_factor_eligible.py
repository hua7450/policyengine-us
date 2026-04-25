from policyengine_us.model_api import *


class wa_eceap_risk_factor_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Risk-factor eligible for Washington ECEAP"
    definition_period = YEAR
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=43.216.512",
        "https://app.leg.wa.gov/RCW/default.aspx?cite=43.216.505",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.wa.dcyf.eceap.eligibility.income
        # The risk-factor pathway (RCW 43.216.512) expires 2030-08-01, when
        # the standard threshold rises to 50% SMI and the pathway becomes
        # redundant.
        if not p.risk_factor_pathway.in_effect:
            return False

        spm_unit = person.spm_unit
        # DCYF income verification (WAC 110-425-0080) counts market income plus
        # cash transfers (TANF, SSI, Social Security) and child support; the
        # broader ccdf_income excludes government transfers and so understates
        # ECEAP family income.
        income = spm_unit("wa_eceap_family_income", period)
        if p.risk_factor_pathway.uses_fpg:
            fpg = spm_unit("spm_unit_fpg", period)
            lower_bound = fpg * p.risk_factor_pathway.lower_fraction_of_fpg
            upper_bound = fpg * p.risk_factor_pathway.fraction_of_fpg
        else:
            smi = spm_unit("hhs_smi", period)
            lower_bound = smi * p.standard_fraction_of_smi
            upper_bound = smi * p.risk_factor_pathway.fraction_of_smi
        in_income_band = (income > lower_bound) & (income <= upper_bound)

        # Modelable risk factors from RCW 43.216.512 and DCYF priority points.
        # Unmodeled risk factors at the moment: domestic violence, incarcerated
        # parent of this child, teen parent, parent education level, substance
        # abuse, premature birth or low birth weight, chronic health condition,
        # deployed military parent, loss of caregiver, Indian Boarding School
        # family history, English-language-learner status (we track non-English-
        # speaking home at the household level, but not per-person English
        # proficiency reliably).
        esl = person.household("is_non_english_speaking_home", period)
        migrant = person("is_migratory_child", period)
        developmental_delay = person("has_developmental_delay", period)
        has_iep = person("has_individualized_education_program", period)
        # is_single_parent_household is only True on the unmarried tax-unit
        # head; project from the parent to the child via the SPM unit.
        single_parent_in_unit = person.spm_unit.any(
            person("is_single_parent_household", period)
        )
        has_risk_factor = (
            esl | migrant | developmental_delay | has_iep | single_parent_in_unit
        )

        return in_income_band & has_risk_factor
