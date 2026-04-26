from policyengine_us.model_api import *


class wa_pte_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for the Washington Senior Citizens and Disabled Persons Property Tax Exemption"
    definition_period = MONTH
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=84.36.381",
        "https://dor.wa.gov/sites/default/files/2022-02/PTExemption_Senior.pdf#page=1",
    )

    def formula(spm_unit, period, parameters):
        person = spm_unit.members
        has_categorical_member = spm_unit.any(
            person("wa_pte_categorical_eligible", period)
        )
        owner_occupant = spm_unit("wa_pte_owner_occupant", period)
        income_eligible = spm_unit("wa_pte_income_eligible", period)
        return has_categorical_member & owner_occupant & income_eligible
