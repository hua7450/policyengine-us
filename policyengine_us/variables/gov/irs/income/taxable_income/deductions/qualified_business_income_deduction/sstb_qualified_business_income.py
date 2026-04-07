from policyengine_us.model_api import *


class sstb_qualified_business_income(Variable):
    value_type = float
    entity = Person
    label = "SSTB qualified business income"
    documentation = (
        "Qualified business income from a specified service trade or business "
        "(SSTB) under IRC §199A(d)(2). Tracked separately from non-SSTB QBI so "
        "the §199A(d)(3) applicable-percentage phaseout above the threshold can "
        "reduce only the SSTB component."
    )
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.law.cornell.edu/uscode/text/26/199A#c",
        "https://www.law.cornell.edu/uscode/text/26/199A#d_2",
    )
    defined_for = "business_is_qualified"

    def formula(person, period, parameters):
        p = parameters(period).gov.irs.deductions.qbi
        non_sstb_gross = 0
        for var in p.income_definition:
            non_sstb_gross += person(var, period) * person(
                var + "_would_be_qualified", period
            )
        sstb_gross = person("sstb_self_employment_income", period) * person(
            "sstb_self_employment_income_would_be_qualified", period
        )
        # Pro-rate QBI deductions across non-SSTB and SSTB shares so that
        # SE-tax / health-insurance / pension ALDs reduce both QBI categories
        # in proportion to their gross income.
        gross_total = non_sstb_gross + sstb_gross
        qbi_deductions = add(person, period, p.deduction_definition)
        sstb_share = where(gross_total > 0, sstb_gross / gross_total, 0)
        return max_(0, sstb_gross - qbi_deductions * sstb_share)
