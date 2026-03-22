from policyengine_us.model_api import *

ZONE_1_MAX_THRESHOLD = 375_000
ZONE_2_MIDDLE_THRESHOLD = 437_500
TOP_THRESHOLD = 2_500_000
SUBJECT_THRESHOLD = 312_500


class ny_mctmt_employer_tax(Variable):
    value_type = float
    entity = Person
    label = "New York Metropolitan Commuter Transportation Mobility Tax"
    documentation = (
        "Employer-side New York MCTMT liability attributable to this worker, "
        "using household county as a proxy for work location and employer "
        "quarterly payroll expense as a proxy for applicable zone brackets."
    )
    definition_period = YEAR
    unit = USD
    defined_for = StateCode.NY
    reference = "https://www.tax.ny.gov/bus/mctmt/emp.htm"

    def formula(person, period, parameters):
        quarter_payroll = person("ny_mctmt_employer_quarterly_payroll_expense", period)
        in_zone_1 = person.household("in_nyc", period)
        in_zone_2 = person.household("in_ny_mctd_zone_2", period)
        payroll_in_mctd = quarter_payroll * (in_zone_1 | in_zone_2)

        zone_1_rate = select(
            [
                quarter_payroll <= SUBJECT_THRESHOLD,
                quarter_payroll <= ZONE_1_MAX_THRESHOLD,
                quarter_payroll <= ZONE_2_MIDDLE_THRESHOLD,
                quarter_payroll <= TOP_THRESHOLD,
            ],
            [0, 0.00055, 0.00115, 0.006],
            default=0.00895,
        )
        zone_2_rate = select(
            [
                quarter_payroll <= SUBJECT_THRESHOLD,
                quarter_payroll <= ZONE_1_MAX_THRESHOLD,
                quarter_payroll <= ZONE_2_MIDDLE_THRESHOLD,
                quarter_payroll <= TOP_THRESHOLD,
            ],
            [0, 0.00055, 0.00115, 0.0034],
            default=0.00635,
        )
        applicable_rate = select(
            [in_zone_1, in_zone_2],
            [zone_1_rate, zone_2_rate],
            default=0,
        )

        liable = payroll_in_mctd > SUBJECT_THRESHOLD
        return where(
            liable,
            applicable_rate * person("payroll_tax_gross_wages", period),
            0,
        )
