from policyengine_us.model_api import *


class sd_cca_copay(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    label = "South Dakota CCA family co-payment"
    definition_period = MONTH
    defined_for = "sd_cca_eligible"
    reference = (
        "https://dss.sd.gov/docs/childcare/assistance/Subsidy_Manual.pdf#page=21",
        "https://dss.sd.gov/docs/childcare/assistance/Sliding_Fee_Scale.pdf",
    )

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.sd.dss.cca.copay
        # Income is floored at zero so a self-employment loss cannot produce a
        # negative co-payment.
        countable_income = max_(spm_unit("sd_cca_countable_income", period), 0)
        # spm_unit_fpg is an annual dollar amount; the bare monthly period
        # auto-divides it to a monthly value.
        monthly_fpg = spm_unit("spm_unit_fpg", period)
        # The co-payment is 5% of countable income above 170% of the federal
        # poverty level, and zero at or below that threshold.
        income_above_threshold = max_(
            countable_income - p.fpl_threshold * monthly_fpg, 0
        )
        copay = income_above_threshold * p.rate
        # The co-payment never exceeds 12% of countable income.
        copay = min_(copay, p.max_rate * countable_income)
        # The co-payment is waived for families enrolled in the Temporary
        # Assistance for Needy Families program and for foster or
        # protective-services children (Sliding Fee Scale).
        is_tanf_enrolled = spm_unit("is_tanf_enrolled", period)
        has_foster_child = add(spm_unit, period, ["is_in_foster_care"]) > 0
        has_protective_services_child = (
            add(
                spm_unit,
                period.this_year,
                ["receives_or_needs_protective_services"],
            )
            > 0
        )
        waived = is_tanf_enrolled | has_foster_child | has_protective_services_child
        return where(waived, 0, copay)
