from policyengine_us.model_api import *


STATE_EMPLOYER_UNEMPLOYMENT_TAX_VARIABLES = []

for state_code, state_name in [
    ("AL", "Alabama"),
    ("AK", "Alaska"),
    ("AZ", "Arizona"),
    ("AR", "Arkansas"),
    ("CA", "California"),
    ("CO", "Colorado"),
    ("CT", "Connecticut"),
    ("DE", "Delaware"),
    ("DC", "District of Columbia"),
    ("FL", "Florida"),
    ("GA", "Georgia"),
    ("HI", "Hawaii"),
    ("ID", "Idaho"),
    ("IL", "Illinois"),
    ("IN", "Indiana"),
    ("IA", "Iowa"),
    ("KS", "Kansas"),
    ("KY", "Kentucky"),
    ("LA", "Louisiana"),
    ("ME", "Maine"),
    ("MD", "Maryland"),
    ("MA", "Massachusetts"),
    ("MI", "Michigan"),
    ("MN", "Minnesota"),
    ("MS", "Mississippi"),
    ("MO", "Missouri"),
    ("MT", "Montana"),
    ("NE", "Nebraska"),
    ("NV", "Nevada"),
    ("NH", "New Hampshire"),
    ("NJ", "New Jersey"),
    ("NM", "New Mexico"),
    ("NY", "New York"),
    ("NC", "North Carolina"),
    ("ND", "North Dakota"),
    ("OH", "Ohio"),
    ("OK", "Oklahoma"),
    ("OR", "Oregon"),
    ("PA", "Pennsylvania"),
    ("RI", "Rhode Island"),
    ("SC", "South Carolina"),
    ("SD", "South Dakota"),
    ("TN", "Tennessee"),
    ("TX", "Texas"),
    ("UT", "Utah"),
    ("VT", "Vermont"),
    ("VA", "Virginia"),
    ("WA", "Washington"),
    ("WV", "West Virginia"),
    ("WI", "Wisconsin"),
    ("WY", "Wyoming"),
    ("PR", "Puerto Rico"),
    ("VI", "Virgin Islands"),
]:
    variable_name = f"{state_code.lower()}_employer_state_unemployment_tax"
    STATE_EMPLOYER_UNEMPLOYMENT_TAX_VARIABLES.append(variable_name)
    globals()[variable_name] = type(
        variable_name,
        (Variable,),
        dict(
            value_type=float,
            entity=Person,
            label=f"{state_name} employer state unemployment tax",
            documentation=(
                f"Employer-side unemployment tax liability for {state_name}."
            ),
            unit=USD,
            definition_period=YEAR,
            defined_for=state_code,
            formula=lambda person, period, parameters: (
                person("employer_state_unemployment_tax_rate", period)
                * person("taxable_earnings_for_state_unemployment_tax", period)
            ),
        ),
    )
