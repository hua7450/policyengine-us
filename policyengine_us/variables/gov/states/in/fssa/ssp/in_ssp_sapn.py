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
        p = parameters(period).gov.states["in"].fssa.ssp.sapn.amount
        joint_claim = person("ssi_claim_is_joint", period.this_year)
        eligible = person("in_ssp_sapn_eligible", period)
        both_eligible = person.marital_unit.sum(eligible) == 2
        is_couple = joint_claim & both_eligible
        return where(is_couple, p.couple / 2, p.individual)
