from policyengine_us.model_api import *


class wa_pte_owner_occupant(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Owner-occupant for the Washington Senior Citizens and Disabled Persons Property Tax Exemption"
    definition_period = MONTH
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=84.36.381",
        "https://app.leg.wa.gov/WAC/default.aspx?cite=458-16A-100",
        "https://dor.wa.gov/sites/default/files/2022-02/PTExemption_Senior.pdf#page=1",
    )

    def formula(spm_unit, period, parameters):
        # Statute requires ownership in fee, life estate, or contract purchase
        # of the principal place of residence. We don't track contract purchase,
        # life estates, coop shares, or non-primary-residence flags at the moment;
        # PolicyEngine assumes the household's residence is its principal residence,
        # so we approximate by checking the household tenure type.
        tenure = spm_unit.household("tenure_type", period.this_year)
        tenure_types = tenure.possible_values
        return (tenure == tenure_types.OWNED_OUTRIGHT) | (
            tenure == tenure_types.OWNED_WITH_MORTGAGE
        )
