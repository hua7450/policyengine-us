from policyengine_us.model_api import *


class va_ccsp_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Income-eligible for Virginia Child Care Subsidy Program"
    definition_period = MONTH
    defined_for = StateCode.VA
    reference = (
        "https://law.lis.virginia.gov/admincode/title8/agency20/chapter790/section40/",
        "https://doe.virginia.gov/home/showpublisheddocument/56270#page=86",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.va.dss.ccsp.income
        countable_income = spm_unit("va_ccsp_countable_income", period)
        fpg = spm_unit("spm_unit_fpg", period)
        smi = spm_unit("hhs_smi", period)

        # New applicants: FPG-based limit by locality group
        locality_group = spm_unit("va_ccsp_locality_group", period.this_year)
        fpg_rate = p.initial_eligibility_fpg_rate[locality_group]
        initial_limit = fpg * fpg_rate

        # Redetermination (enrolled): 85% SMI
        exit_limit = smi * p.exit_smi_rate

        enrolled = spm_unit("va_ccsp_enrolled", period)
        income_limit = where(enrolled, exit_limit, initial_limit)

        # Young child exception: families with a child age 5 or younger
        # qualify for the higher of FPG limit or 85% SMI regardless
        person = spm_unit.members
        age = person("age", period.this_year)
        has_young_child = spm_unit.any(age <= p.young_child_age_threshold)
        young_child_limit = smi * p.young_child_smi_rate
        income_limit = where(
            has_young_child & ~enrolled,
            max_(initial_limit, young_child_limit),
            income_limit,
        )

        income_test_passed = countable_income <= income_limit

        # TANF/Medicaid/WIC categorical eligibility waives income test
        income_waived = spm_unit("va_ccsp_income_test_waived", period)
        return income_test_passed | income_waived
