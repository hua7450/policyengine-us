from policyengine_us.model_api import *


class WAStateSupplementaryPaymentCategory(Enum):
    STANDARD = "Standard rate (aged, blind, disabled, or with ineligible spouse)"
    MEDICAL_INSTITUTION = "Resident of medical (Title XIX) institution"
    NONE = "Not in a qualifying category"


class wa_ssp_payment_category(Variable):
    value_type = Enum
    entity = Person
    label = "Washington SSP payment category"
    definition_period = MONTH
    defined_for = StateCode.WA
    possible_values = WAStateSupplementaryPaymentCategory
    default_value = WAStateSupplementaryPaymentCategory.NONE
    reference = "https://app.leg.wa.gov/wac/default.aspx?cite=388-474-0012"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.wa.dshs.ssp
        # WA SSP requires actual SSI receipt, not just categorical eligibility.
        # We don't track SSP enrollment date at the moment, so anyone meeting
        # the categorical criteria is treated as eligible — this overstates the
        # true caseload because WA closed SSP to most new enrollees in 2023
        # (DDA PVL, grandfathered/MIL, and BRS foster-child tracks not modeled).
        is_ssi_eligible = person("is_ssi_eligible", period.this_year)
        receives_ssi = person("uncapped_ssi", period.this_year) > 0
        base_eligible = is_ssi_eligible & receives_ssi

        # SDX code D (medical treatment facility) maps to MEDICAL_INSTITUTION;
        # codes A/B/C (community living) map to STANDARD via the categorical paths.
        living_arrangement = person("ssi_federal_living_arrangement", period.this_year)
        in_medical_institution = (
            living_arrangement
            == living_arrangement.possible_values.MEDICAL_TREATMENT_FACILITY
        )

        aged = person("is_ssi_aged", period.this_year)
        blind = person("is_blind", period.this_year)
        # WAC 388-474-0012(2)(e) added a standalone disabled category effective
        # 2023-07-01 (WSR 23-14-065 emergency rule per HB 1128, made permanent
        # by WSR 23-24-009 on 2023-12-28). Before that date, disabled-only
        # people who weren't also aged/blind/with-ineligible-spouse did not
        # qualify.
        disabled_qualifies = p.eligibility.disabled_category.in_effect & person(
            "is_ssi_disabled", period.this_year
        )

        marital_unit = person.marital_unit
        ssi_eligible_count = marital_unit.sum(is_ssi_eligible)
        has_ineligible_spouse = (
            (marital_unit.nb_persons() == 2)
            & (ssi_eligible_count == 1)
            & is_ssi_eligible
        )

        in_standard_category = aged | blind | disabled_qualifies | has_ineligible_spouse

        categories = WAStateSupplementaryPaymentCategory
        return select(
            [
                base_eligible & in_medical_institution,
                base_eligible & in_standard_category,
            ],
            [
                categories.MEDICAL_INSTITUTION,
                categories.STANDARD,
            ],
            default=categories.NONE,
        )
