from policyengine_us.model_api import *


class rrc_cares(Variable):
    value_type = float
    entity = TaxUnit
    label = "Recovery Rebate Credit (CARES)"
    unit = USD
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/uscode/text/26/6428"

    def formula(tax_unit, period, parameters):
        rrc = parameters(period).gov.irs.credits.recovery_rebate_credit
        filing_status = tax_unit("filing_status", period)
        agi = tax_unit("adjusted_gross_income", period)
        # Count children with valid SSN per 26 USC 6428(g)(1)(C)
        # Reuse EITC SSN check - CARES RRC uses same SSN definition (work-authorized SSN)
        # per 26 USC 6428(g)(1), which cross-references the child tax credit SSN rule
        # at 26 USC 24(h)(7), which in turn references EITC's 26 USC 32(m).
        count_children = tax_unit(
            "rrc_cares_qualifying_children_with_valid_ssn", period
        )
        # Count adults with valid SSN per 26 USC 6428(g)(1)(A) and (g)(1)(B)
        # Armed Forces exception per 26 USC 6428(g)(4)
        armed_forces_exception = tax_unit(
            "rrc_qualifies_for_armed_forces_exception", period
        )
        is_joint = tax_unit("tax_unit_is_joint", period)
        adults_with_ssn = tax_unit("rrc_adult_count_with_valid_ssn", period)
        count_adults = where(
            armed_forces_exception,
            2,  # Joint filers always have 2 adults (structural constant)
            where(is_joint, adults_with_ssn, min_(adults_with_ssn, 1)),
        )
        max_payment = (
            rrc.cares.max.adult * count_adults
            + rrc.cares.max.child * count_children
        )
        payment_reduction = rrc.cares.phase_out.rate * max_(
            0, agi - rrc.cares.phase_out.threshold[filing_status]
        )
        return max_(0, max_payment - payment_reduction)
