from policyengine_us.model_api import *


class ct_c4k_payment_rate(Variable):
    value_type = float
    entity = Person
    unit = USD
    definition_period = MONTH
    defined_for = "ct_c4k_eligible_child"
    label = "Connecticut Care 4 Kids weekly payment rate per child"
    reference = "https://www.ctoec.org/care-4-kids/c4k-providers/c4k-rates/"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ct.oec.c4k
        provider_type = person("ct_c4k_provider_type", period)
        types = provider_type.possible_values
        care_level = person("ct_c4k_care_level", period)
        levels = care_level.possible_values
        region = person.household("ct_c4k_region", period)
        age_group = person("ct_c4k_age_group", period)

        rate = p.rate

        center_ftp = rate.center.full_time_plus[region][age_group]
        center_ft = rate.center.full_time[region][age_group]
        center_ht = rate.center.half_time[region][age_group]
        center_qt = rate.center.quarter_time[region][age_group]

        family_ftp = rate.family.full_time_plus[region][age_group]
        family_ft = rate.family.full_time[region][age_group]
        family_ht = rate.family.half_time[region][age_group]
        family_qt = rate.family.quarter_time[region][age_group]

        relative_ftp = rate.relative.full_time_plus[region][age_group]
        relative_ft = rate.relative.full_time[region][age_group]
        relative_ht = rate.relative.half_time[region][age_group]
        relative_qt = rate.relative.quarter_time[region][age_group]

        recreational_ftp = rate.recreational.full_time_plus[region][age_group]
        recreational_ft = rate.recreational.full_time[region][age_group]
        recreational_ht = rate.recreational.half_time[region][age_group]
        recreational_qt = rate.recreational.quarter_time[region][age_group]

        center_rate = select(
            [
                care_level == levels.FULL_TIME_PLUS,
                care_level == levels.FULL_TIME,
                care_level == levels.HALF_TIME,
                care_level == levels.QUARTER_TIME,
            ],
            [center_ftp, center_ft, center_ht, center_qt],
            default=center_ft,
        )
        family_rate = select(
            [
                care_level == levels.FULL_TIME_PLUS,
                care_level == levels.FULL_TIME,
                care_level == levels.HALF_TIME,
                care_level == levels.QUARTER_TIME,
            ],
            [family_ftp, family_ft, family_ht, family_qt],
            default=family_ft,
        )
        relative_rate = select(
            [
                care_level == levels.FULL_TIME_PLUS,
                care_level == levels.FULL_TIME,
                care_level == levels.HALF_TIME,
                care_level == levels.QUARTER_TIME,
            ],
            [relative_ftp, relative_ft, relative_ht, relative_qt],
            default=relative_ft,
        )
        recreational_rate = select(
            [
                care_level == levels.FULL_TIME_PLUS,
                care_level == levels.FULL_TIME,
                care_level == levels.HALF_TIME,
                care_level == levels.QUARTER_TIME,
            ],
            [
                recreational_ftp,
                recreational_ft,
                recreational_ht,
                recreational_qt,
            ],
            default=recreational_ft,
        )

        weekly_rate = select(
            [
                provider_type == types.CENTER,
                provider_type == types.FAMILY,
                provider_type == types.RELATIVE,
                provider_type == types.RECREATIONAL,
            ],
            [center_rate, family_rate, relative_rate, recreational_rate],
            default=center_rate,
        )

        is_disabled = person("is_disabled", period)
        special_needs_add = where(is_disabled, p.special_needs_supplement, 0)
        is_accredited = person("ct_c4k_provider_accredited", period)
        accreditation_add = where(is_accredited, p.accreditation_bonus, 0)
        return weekly_rate * (1 + special_needs_add + accreditation_add)
