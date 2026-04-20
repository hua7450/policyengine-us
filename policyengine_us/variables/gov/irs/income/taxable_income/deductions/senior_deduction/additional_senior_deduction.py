from policyengine_us.model_api import *


class additional_senior_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Senior deduction"
    unit = USD
    definition_period = YEAR
    reference = "https://www.congress.gov/bill/119th-congress/house-bill/1/text"

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.irs.deductions.senior_deduction
        eligible_seniors = add(
            tax_unit,
            period,
            ["additional_senior_deduction_eligible_person"],
        )

        agi = tax_unit("adjusted_gross_income", period)
        filing_status = tax_unit("filing_status", period)
        joint = filing_status == filing_status.possible_values.JOINT
        phase_out_amount = where(
            joint,
            p.phase_out_rate.joint.calc(agi),
            p.phase_out_rate.other.calc(agi),
        )
        # Per IRS Schedule 1-A Part V: phase-out applies to each
        # senior's $6,000 individually, then sum across eligible seniors.
        per_senior_allowed = max_(p.amount - phase_out_amount, 0)
        return per_senior_allowed * eligible_seniors
