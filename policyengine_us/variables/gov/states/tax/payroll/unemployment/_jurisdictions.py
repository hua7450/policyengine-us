from policyengine_us.model_api import *


STATE_UNEMPLOYMENT_TAX_JURISDICTIONS = [
    ("states", "AL", "al", "Alabama"),
    ("states", "AK", "ak", "Alaska"),
    ("states", "AZ", "az", "Arizona"),
    ("states", "AR", "ar", "Arkansas"),
    ("states", "CA", "ca", "California"),
    ("states", "CO", "co", "Colorado"),
    ("states", "CT", "ct", "Connecticut"),
    ("states", "DE", "de", "Delaware"),
    ("states", "DC", "dc", "District of Columbia"),
    ("states", "FL", "fl", "Florida"),
    ("states", "GA", "ga", "Georgia"),
    ("states", "HI", "hi", "Hawaii"),
    ("states", "ID", "id", "Idaho"),
    ("states", "IL", "il", "Illinois"),
    ("states", "IN", "in", "Indiana"),
    ("states", "IA", "ia", "Iowa"),
    ("states", "KS", "ks", "Kansas"),
    ("states", "KY", "ky", "Kentucky"),
    ("states", "LA", "la", "Louisiana"),
    ("states", "ME", "me", "Maine"),
    ("states", "MD", "md", "Maryland"),
    ("states", "MA", "ma", "Massachusetts"),
    ("states", "MI", "mi", "Michigan"),
    ("states", "MN", "mn", "Minnesota"),
    ("states", "MS", "ms", "Mississippi"),
    ("states", "MO", "mo", "Missouri"),
    ("states", "MT", "mt", "Montana"),
    ("states", "NE", "ne", "Nebraska"),
    ("states", "NV", "nv", "Nevada"),
    ("states", "NH", "nh", "New Hampshire"),
    ("states", "NJ", "nj", "New Jersey"),
    ("states", "NM", "nm", "New Mexico"),
    ("states", "NY", "ny", "New York"),
    ("states", "NC", "nc", "North Carolina"),
    ("states", "ND", "nd", "North Dakota"),
    ("states", "OH", "oh", "Ohio"),
    ("states", "OK", "ok", "Oklahoma"),
    ("states", "OR", "or", "Oregon"),
    ("states", "PA", "pa", "Pennsylvania"),
    ("states", "RI", "ri", "Rhode Island"),
    ("states", "SC", "sc", "South Carolina"),
    ("states", "SD", "sd", "South Dakota"),
    ("states", "TN", "tn", "Tennessee"),
    ("states", "TX", "tx", "Texas"),
    ("states", "UT", "ut", "Utah"),
    ("states", "VT", "vt", "Vermont"),
    ("states", "VA", "va", "Virginia"),
    ("states", "WA", "wa", "Washington"),
    ("states", "WV", "wv", "West Virginia"),
    ("states", "WI", "wi", "Wisconsin"),
    ("states", "WY", "wy", "Wyoming"),
    ("territories", "PR", "pr", "Puerto Rico"),
    ("territories", "VI", "vi", "Virgin Islands"),
]

STATE_EMPLOYER_UNEMPLOYMENT_TAX_VARIABLES = [
    f"{slug}_employer_state_unemployment_tax"
    for _, _, slug, _ in STATE_UNEMPLOYMENT_TAX_JURISDICTIONS
]


def select_state_unemployment_tax_parameter(
    person: Population,
    period: Period,
    parameters,
    parameter_name: str,
) -> ArrayLike:
    state_code = person.household("state_code_str", period)
    gov = parameters(period).gov
    conditions = []
    values = []

    for group, code, slug, _ in STATE_UNEMPLOYMENT_TAX_JURISDICTIONS:
        jurisdiction = getattr(getattr(gov, group), slug)
        unemployment = jurisdiction.tax.payroll.unemployment
        conditions.append(state_code == code)
        values.append(getattr(unemployment, parameter_name))

    return select(conditions, values, default=0)
