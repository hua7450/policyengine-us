from policyengine_us.model_api import *


class wa_early_eceap_income_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Income-eligible for Washington Early ECEAP"
    definition_period = YEAR
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=43.216.505",
        "https://www.startearly.org/app/uploads/2021/06/Final-Summary-of-Fair-Start-for-Kids-Act.pdf#page=9",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.wa.dcyf.eceap
        spm_unit = person.spm_unit
        income = spm_unit("wa_eceap_family_income", period)
        if p.uses_fpg:
            threshold = spm_unit("spm_unit_fpg", period) * p.early_eceap.income.fpg_rate
        else:
            threshold = spm_unit("hhs_smi", period) * p.early_eceap.income.smi_rate
        return income <= threshold
