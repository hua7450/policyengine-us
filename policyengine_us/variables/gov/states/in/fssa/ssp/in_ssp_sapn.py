from policyengine_us.model_api import *


class in_ssp_sapn(Variable):
    value_type = float
    entity = Person
    label = "Indiana Supplemental Assistance for Personal Needs"
    unit = USD
    definition_period = MONTH
    defined_for = "in_ssp_sapn_eligible"
    reference = (
        "https://www.in.gov/fssa/ompp/files/Medicaid_PM_5000.pdf",
        "https://secure.ssa.gov/poms.nsf/lnx/0501401001CHI",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.states["in"].fssa.ssp
        joint_claim = person("ssi_claim_is_joint", period.this_year)
        eligible = person("in_ssp_sapn_eligible", period)
        both_eligible = person.marital_unit.sum(eligible) == 2
        is_couple = joint_claim & both_eligible
        monthly_countable_income = (
            person("ssi_countable_income", period.this_year) / MONTHS_IN_YEAR
        )
        monthly_ssi_payment_limit = (
            person("ssi_amount_if_eligible", period.this_year) / MONTHS_IN_YEAR
        )
        max_individual = p.sapn.amount.individual
        max_couple = p.sapn.amount.couple
        personal_needs_allowance = p.personal_needs_allowance

        individual_amount = max_(
            min_(
                personal_needs_allowance
                - monthly_ssi_payment_limit
                - monthly_countable_income,
                max_individual,
            ),
            0,
        )
        couple_amount = max_(
            min_(
                2 * personal_needs_allowance
                - person.marital_unit.sum(monthly_ssi_payment_limit)
                - person.marital_unit.sum(monthly_countable_income),
                max_couple,
            ),
            0,
        )
        return where(is_couple, couple_amount / 2, individual_amount)
