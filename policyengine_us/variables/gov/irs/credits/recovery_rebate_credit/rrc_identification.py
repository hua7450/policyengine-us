from policyengine_us.model_api import *


class rrc_adult_count_with_valid_ssn(Variable):
    value_type = int
    entity = TaxUnit
    definition_period = YEAR
    label = "Count of tax unit head/spouse with valid SSN for RRC"
    reference = (
        "https://www.law.cornell.edu/uscode/text/26/6428B#e_2_A",
        "https://www.law.cornell.edu/uscode/text/26/6428B#e_2_B",
    )

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        head_or_spouse = person("is_tax_unit_head_or_spouse", period)
        # Reuse existing EITC SSN check - identical definition (SSN required)
        has_valid_ssn = person(
            "meets_eitc_identification_requirements", period
        )
        return tax_unit.sum(head_or_spouse & has_valid_ssn)


class rrc_qualifies_for_armed_forces_exception(Variable):
    value_type = bool
    entity = TaxUnit
    definition_period = YEAR
    label = "Tax unit qualifies for RRC Armed Forces SSN exception"
    reference = "https://www.law.cornell.edu/uscode/text/26/6428B#e_2_E"

    def formula(tax_unit, period, parameters):
        # Per statute: "at least 1 spouse was a member of the Armed Forces...
        # AND the valid identification number of at least 1 spouse is included"
        # These are TWO INDEPENDENT conditions - can be different people
        person = tax_unit.members
        is_joint = tax_unit("tax_unit_is_joint", period)
        head_or_spouse = person("is_tax_unit_head_or_spouse", period)
        is_military = person("is_military", period)
        has_valid_ssn = person(
            "meets_eitc_identification_requirements", period
        )
        # Check conditions independently (can be different spouses)
        has_military_spouse = tax_unit.any(head_or_spouse & is_military)
        has_spouse_with_ssn = tax_unit.any(head_or_spouse & has_valid_ssn)
        return is_joint & has_military_spouse & has_spouse_with_ssn


class rrc_cares_qualifying_children_with_valid_ssn(Variable):
    value_type = int
    entity = TaxUnit
    definition_period = YEAR
    label = "Count of CTC qualifying children with valid SSN for CARES RRC"
    reference = "https://www.law.cornell.edu/uscode/text/26/6428#g_2"

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        is_ctc_qualifying_child = person("ctc_qualifying_child", period)
        has_valid_ssn = person(
            "meets_eitc_identification_requirements", period
        )
        return tax_unit.sum(is_ctc_qualifying_child & has_valid_ssn)


class rrc_arpa_dependents_with_valid_ssn(Variable):
    value_type = int
    entity = TaxUnit
    definition_period = YEAR
    label = "Count of dependents with valid SSN for ARPA RRC"
    reference = "https://www.law.cornell.edu/uscode/text/26/6428B#e_2_C"

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        is_dependent = person("is_tax_unit_dependent", period)
        has_valid_ssn = person(
            "meets_eitc_identification_requirements", period
        )
        return tax_unit.sum(is_dependent & has_valid_ssn)
