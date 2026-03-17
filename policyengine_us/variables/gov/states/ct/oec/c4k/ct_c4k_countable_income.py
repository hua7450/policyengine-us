from policyengine_us.model_api import *


class ct_c4k_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    unit = USD
    definition_period = MONTH
    defined_for = StateCode.CT
    label = "Connecticut Care 4 Kids countable income"
    reference = "https://eregulations.ct.gov/eRegsPortal/Browse/RCSA/Title_17bSubtitle_17b-749Section_17b-749-05/"

    adds = "gov.states.ct.oec.c4k.income.sources"
    subtracts = "gov.states.ct.oec.c4k.income.deductions"
