from policyengine_us.model_api import *


class va_tanf_childcare_deduction(Variable):
    value_type = float
    entity = SPMUnit
    label = "VA TANF childcare deduction"
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.VA
    reference = "https://www.dss.virginia.gov/media/vdss/benefit-programs/documents/tanfx2fview/tanf/Combined-Full-Manual-07-24_1.pdf#page=175"

    def formula(spm_unit, period, parameters):
        # Per VA TANF Manual section 305.3 item 5, the disregard covers care
        # of each child or incapacitated adult in the assistance unit.
        p = parameters(period).gov.states.va.dss.tanf.income.deductions.dependent_care
        person = spm_unit.members
        age = person("age", period.this_year)
        dependent = person("is_tax_unit_dependent", period)
        disabled_adult = person("is_adult", period) & person(
            "is_disabled", period.this_year
        )
        care_recipient = dependent | disabled_adult
        childcare_expenses = spm_unit("childcare_expenses", period)
        adult_care_expenses = add(spm_unit, period, ["care_expenses"])
        max_deduction = spm_unit.sum(p.full_time.calc(age) * care_recipient)
        return min_(childcare_expenses + adult_care_expenses, max_deduction)
