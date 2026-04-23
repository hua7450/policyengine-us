from policyengine_us.model_api import *


class ia_ssa(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Iowa State Supplementary Assistance"
    unit = USD
    defined_for = StateCode.IA
    reference = (
        "https://www.legis.iowa.gov/docs/code/249.3.pdf",
        "https://www.legis.iowa.gov/docs/iac/chapter/01-07-2026.441.52.pdf",
        "https://hhs.iowa.gov/assistance-programs/state-supplementary-assistance",
    )

    def formula(person, period, parameters):
        arrangement = person("ia_ssa_living_arrangement", period)
        arr_values = arrangement.possible_values
        p = parameters(period).gov.states.ia.hhs.ssa
        # Monthly income helpers.
        countable_monthly = (
            person("ssi_countable_income", period.this_year) / MONTHS_IN_YEAR
        )
        ssi_monthly = person("ssi", period.this_year) / MONTHS_IN_YEAR
        total_rcf_income = countable_monthly + ssi_monthly
        individual_fbr = parameters(period).gov.ssa.ssi.amount.individual
        couple_fbr = parameters(period).gov.ssa.ssi.amount.couple
        joint_claim = person("ssi_claim_is_joint", period.this_year)
        basic_ssi_disregard = where(joint_claim, couple_fbr, individual_fbr)
        # Federally-administered SSP V-shape (POMS SI 01415.050.F):
        #   supplement = max(0, (FBR + state_supplement) − max(countable, FBR))
        # applied to Blind, DP, FLH with their respective state-supplement
        # parameters.
        countable_or_fbr = max_(countable_monthly, individual_fbr)
        # BLIND — IAC 441—52.1(4): flat $22 state supplement (frozen since 2011).
        blind_amt = max_(0, (individual_fbr + p.blind) - countable_or_fbr)
        # DP — IAC 441—52.1(2): state supplement varies by configuration,
        # capped per person.
        dp_config = person("ia_ssa_dp_configuration", period)
        dp_state_supplement = p.dp.state_supplement[dp_config]
        dp_raw = max_(0, (individual_fbr + dp_state_supplement) - countable_or_fbr)
        dp_amt = min_(dp_raw, p.dp.max_per_person_cap)
        # FLH — IAC 441—52.1(1): state supplement capped at max_supplement
        # ($142 frozen since 2011). For recipients whose only income is SSI
        # (countable_monthly == 0), SSA's $20 general-income disregard goes
        # unused, so Iowa HHS issues a separate Department payment equal to
        # (state_supplement − max_supplement) to close the gap and bring total
        # income to the full standard. In 2011 the state supplement equals
        # max_supplement so no extra is owed; from 2017 onward the extra is $20.
        flh_v_shape = max_(
            0, (individual_fbr + p.flh.state_supplement) - countable_or_fbr
        )
        flh_base = min_(flh_v_shape, p.flh.max_supplement)
        flh_extra = where(
            countable_monthly == 0,
            max_(0, p.flh.state_supplement - p.flh.max_supplement),
            0,
        )
        flh_amt = flh_base + flh_extra
        # RCF — IAC 441—52.1(3): cost-of-care minus client participation.
        # Client participation = total monthly income (SSI countable + federal
        # SSI payment) minus the personal needs allowance.
        rcf_per_diem = person("ia_ssa_rcf_cost_per_diem", period)
        rcf_capped_per_diem = min_(rcf_per_diem, p.rcf.max_per_diem)
        rcf_cost_of_care = rcf_capped_per_diem * p.rcf.days_multiplier
        rcf_client_participation = max_(
            0, total_rcf_income - p.rcf.personal_needs_allowance
        )
        rcf_amt = max_(0, rcf_cost_of_care - rcf_client_participation)
        # IHHRC — IAC 441—177.10(2)(a) and 177.10(3):
        #   payment = max(0, min(cost, per-person cap) − client participation).
        # Client participation is combined marital-unit countable income after
        # the basic SSI standard disregard (the applicable FBR for a single or
        # joint claim). When both spouses need care, split evenly across the
        # marital unit to avoid double-counting when the SPM unit aggregates;
        # when only one spouse needs care, all combined participation is
        # charged to the sole recipient because the services are provided to
        # them alone.
        ihhrc_cost = person("ia_ssa_ihhrc_cost_of_care", period)
        both_need_care = person("ia_ssa_ihhrc_both_need_care", period)
        combined_countable = person.marital_unit.sum(countable_monthly)
        combined_participation = max_(0, combined_countable - basic_ssi_disregard)
        ihhrc_client_participation = where(
            both_need_care,
            combined_participation / person.marital_unit.nb_persons(),
            combined_participation,
        )
        ihhrc_eligible_cost = min_(ihhrc_cost, p.ihhrc.max_cost_single)
        ihhrc_amt = max_(0, ihhrc_eligible_cost - ihhrc_client_participation)
        # SMME — IAC 441—52.1(7): flat amount ($1 since 2017).
        smme_amt = p.smme.amount
        return select(
            [
                arrangement == arr_values.RCF,
                arrangement == arr_values.IHHRC,
                arrangement == arr_values.FLH,
                arrangement == arr_values.DP,
                arrangement == arr_values.BLIND,
                arrangement == arr_values.SMME,
            ],
            [rcf_amt, ihhrc_amt, flh_amt, dp_amt, blind_amt, smme_amt],
            default=0,
        )
