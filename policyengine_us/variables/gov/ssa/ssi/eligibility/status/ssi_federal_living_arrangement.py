from policyengine_us.model_api import *


class SSIFederalLivingArrangement(Enum):
    A = "Own household"
    B = "Another person's household"
    C = "Child in parental household"
    D = "Medical treatment facility"


class ssi_federal_living_arrangement(Variable):
    value_type = Enum
    entity = Person
    label = "SSI federal living arrangement"
    definition_period = YEAR
    possible_values = SSIFederalLivingArrangement
    default_value = SSIFederalLivingArrangement.A
    reference = (
        "https://www.law.cornell.edu/cfr/text/20/416.1132",
        "https://secure.ssa.gov/apps10/poms.nsf/lnx/0500835001",
    )

    def formula(person, period, parameters):
        # Classification priority per POMS SI 00835.005:
        # D > C > B > A (A is residual)

        # Status D: Medical treatment facility with Medicaid paying >50%
        is_d = person("ssi_lives_in_medical_treatment_facility", period) & person(
            "ssi_medicaid_pays_majority_of_care", period
        )

        # Status C: Child under 18 with ineligible parent in the tax unit.
        # Uses existing is_child (age < 18) and is_ssi_ineligible_parent
        # from the deeming framework. Under-22 students are excluded because
        # is_ssi_ineligible_parent keys off is_child (age < 18); extending
        # to under-22 students requires updating the deeming framework.
        has_ineligible_parent = (
            person.tax_unit.sum(
                person.tax_unit.members("is_ssi_ineligible_parent", period)
            )
            > 0
        )
        is_c = ~is_d & person("is_child", period) & has_ineligible_parent

        # Status B: In another person's household AND receives shelter
        # AND others pay all meals (the VTR gateway conditions)
        in_another_household = person("ssi_lives_in_another_persons_household", period)
        receives_shelter = person(
            "ssi_receives_shelter_from_others_in_household", period
        )
        all_meals_paid = person("ssi_others_pay_all_meals", period)
        is_b = ~is_d & ~is_c & in_another_household & receives_shelter & all_meals_paid

        # Status A: Residual (everyone else)
        return select(
            [is_d, is_c, is_b],
            [
                SSIFederalLivingArrangement.D,
                SSIFederalLivingArrangement.C,
                SSIFederalLivingArrangement.B,
            ],
            default=SSIFederalLivingArrangement.A,
        )
