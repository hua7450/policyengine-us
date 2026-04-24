from policyengine_us.model_api import *


class is_wa_eceap_income_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Income-eligible for Washington ECEAP under the standard pathway"
    definition_period = YEAR
    defined_for = StateCode.WA
    reference = (
        "https://app.leg.wa.gov/RCW/default.aspx?cite=43.216.505",
        "https://www.dcyf.wa.gov/sites/default/files/pdf/eceap/ECEAP-Federal-Poverty-Level-Chart.pdf",
        "https://www.dcyf.wa.gov/sites/default/files/pdf/eceap/State-Median-Income-Chart.pdf",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states.wa.dcyf.eceap.eligibility.income
        spm_unit = person.spm_unit
        income = spm_unit("ccdf_income", period)
        if p.uses_fpg:
            threshold = spm_unit("spm_unit_fpg", period) * p.standard_fraction_of_fpg
        else:
            threshold = spm_unit("hhs_smi", period) * p.standard_fraction_of_smi
        return income <= threshold
