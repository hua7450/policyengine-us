from policyengine_us.model_api import *


class ca_tanf_countable_income_applicant(Variable):
    value_type = float
    entity = SPMUnit
    label = "California CalWORKs Countable Income for Eligibility"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.CA
    reference = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=WIC&sectionNum=11450.12."

    def formula(spm_unit, period):
        countable_earned = add(
            spm_unit,
            period,
            ["ca_tanf_earned_income_after_disregard_person"],
        )
        db_unearned = spm_unit("ca_tanf_db_unearned_income", period)
        other_unearned = spm_unit("ca_tanf_other_unearned_income", period)

        return countable_earned + db_unearned + other_unearned
