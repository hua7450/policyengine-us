from policyengine_us.model_api import *


class is_wa_early_eceap_income_eligible(Variable):
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
        p = parameters(period).gov.states.wa.dcyf.eceap.eligibility.income
        spm_unit = person.spm_unit
        # DCYF income verification (WAC 110-425-0080) counts market income plus
        # cash transfers (TANF, SSI, Social Security) and child support; the
        # broader ccdf_income excludes government transfers and so understates
        # ECEAP family income.
        income = spm_unit("wa_eceap_family_income", period)
        threshold = spm_unit("hhs_smi", period) * p.wa_early_eceap_fraction_of_smi
        return income <= threshold
