from policyengine_us.model_api import *


class meets_rrc_identification_requirements(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person meets Recovery Rebate Credit identification requirements"
    reference = (
        "https://www.law.cornell.edu/uscode/text/26/6428#g",
        "https://www.law.cornell.edu/uscode/text/26/6428A#d",
        "https://www.law.cornell.edu/uscode/text/26/6428B#e_2",
    )
    documentation = """
    Valid identification number for RRC means a Social Security Number (SSN).
    ITINs are not valid. ATINs are valid for adopted children only (not modeled).
    SSN card types CITIZEN and NON_CITIZEN_VALID_EAD indicate valid SSN.
    """

    def formula(person, period, parameters):
        ssn_card_type = person("ssn_card_type", period)
        ssn_card_types = ssn_card_type.possible_values
        citizen = ssn_card_type == ssn_card_types.CITIZEN
        non_citizen_valid_ead = (
            ssn_card_type == ssn_card_types.NON_CITIZEN_VALID_EAD
        )
        return citizen | non_citizen_valid_ead


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
        has_valid_ssn = person("meets_rrc_identification_requirements", period)
        return tax_unit.sum(head_or_spouse & has_valid_ssn)


class rrc_qualifies_for_armed_forces_exception(Variable):
    value_type = bool
    entity = TaxUnit
    definition_period = YEAR
    label = "Tax unit qualifies for RRC Armed Forces SSN exception"
    reference = "https://www.law.cornell.edu/uscode/text/26/6428B#e_2_E"
    documentation = """
    For joint returns, if at least one spouse was a member of the Armed Forces
    during the tax year and has a valid SSN, the full adult amount is allowed
    even if the other spouse lacks a valid SSN.
    """

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        is_joint = tax_unit("tax_unit_is_joint", period)
        head_or_spouse = person("is_tax_unit_head_or_spouse", period)
        is_military = person("is_military", period)
        has_valid_ssn = person("meets_rrc_identification_requirements", period)
        military_spouse_with_ssn = tax_unit.any(
            head_or_spouse & is_military & has_valid_ssn
        )
        return is_joint & military_spouse_with_ssn


class rrc_cares_qualifying_children_with_valid_ssn(Variable):
    value_type = int
    entity = TaxUnit
    definition_period = YEAR
    label = "Count of CTC qualifying children with valid SSN for CARES RRC"
    reference = "https://www.law.cornell.edu/uscode/text/26/6428#g_2"

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        is_ctc_qualifying_child = person("ctc_qualifying_child", period)
        has_valid_ssn = person("meets_rrc_identification_requirements", period)
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
        has_valid_ssn = person("meets_rrc_identification_requirements", period)
        return tax_unit.sum(is_dependent & has_valid_ssn)
