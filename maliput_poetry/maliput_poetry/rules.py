##############################################################################
# Documentation
##############################################################################

"""Example of how to use Maliput's rule API to query and manipulate traffic rules"""

##############################################################################
# Imports
##############################################################################

import os

import maliput

##############################################################################
# Main
##############################################################################

def filter_rules_by_type(rules, rule_type):
    filtered_rules = {}
    for rule_id, rule in rules.discrete_value_rules.items():
        if rule.type_id().string() == rule_type:
            filtered_rules[rule_id] = rule
    return filtered_rules

def print_discrete_value_rule_states(discrete_value_rule_states):
    for rule_id in discrete_value_rule_states.keys():
        print("  Rule ID:", rule_id.string())
        print("    State ID:", discrete_value_rule_states[rule_id].value)

def print_bulb_states(bulb_states):
    for bulb_id in bulb_states.keys():
        print("  Bulb ID:", bulb_id.string())
        print("    State:", bulb_states[bulb_id])

def print_phase_details(phase):
    discrete_value_rule_states = phase.discrete_value_rule_states()
    print("Discrete Value Rule States:")
    print_discrete_value_rule_states(discrete_value_rule_states)
    bulb_states = phase.bulb_states()
    print("Bulb States:")
    print_bulb_states(bulb_states)

def main():
    filepath = os.path.join(os.path.dirname(__file__), "xodr", "LoopRoadPedestrianCrosswalk.xodr")
    yaml_filepath = os.path.join(os.path.dirname(__file__), "xodr", "LoopRoadPedestrianCrosswalk.yaml")

    # RoadNetwork parameters can be found at https://maliput.readthedocs.io/en/latest/road_network_parameters.html
    # It will depend on the specific RoadNetwork plugin being used.
    params = {
        "opendrive_file": filepath ,
        "road_rule_book": yaml_filepath,
        "rule_registry": yaml_filepath,
        "traffic_light_book": yaml_filepath,
        "phase_ring_book": yaml_filepath,
        "intersection_book": yaml_filepath,
    }

    road_network = maliput.plugin.create_road_network("maliput_malidrive", params)
    rb = road_network.rulebook()

    # Find rules that affect a specific lane s range.
    lane_s_range = maliput.api.LaneSRange(
        lane_id=maliput.api.LaneId("1_1_-1"),
        s_range=maliput.api.SRange(0., 15.0)
    )
    print("************ Rules for Lane 1_1_-1 ************")
    rules_at_range = rb.FindRules([lane_s_range], tolerance=1e-2)
    for rule_id in rules_at_range.discrete_value_rules.keys():
        print("Rule ID:", rule_id.string())
        print(" - Rule Type ID:", rules_at_range.discrete_value_rules[rule_id].type_id())
    right_of_way_rules = filter_rules_by_type(rules_at_range, "Right-Of-Way Rule Type")

    assert len(right_of_way_rules) > 0, "No Right-Of-Way rules found in the specified lane s range."
    assert len(right_of_way_rules) == 1, "Expected exactly one Right-Of-Way rule in the specified lane s range."
    # I expect the rule id to be "Right-Of-Way Rule Type/WestToEastSouth" as I arbitrarily selected the lane "1_1_-1".
    assert list(right_of_way_rules.keys())[0].string() == "Right-Of-Way Rule Type/WestToEastSouth"

    # Access rule of interest by id.
    print("************ Right Of Way Rule for Lane 1_1_-1 ************")
    rule_id = list(right_of_way_rules.keys())[0]
    rule_of_interest = rb.GetDiscreteValueRule(rule_id)
    # Printing rule details
    print("Rule ID:", rule_of_interest.id())
    print("Rule Type ID:", rule_of_interest.type_id())
    print("Rule Zone:")
    for lane_s_range in rule_of_interest.zone().ranges():
        print("  Lane ID:", lane_s_range.lane_id().string())
        print("    s_start:", lane_s_range.s_range().s0())
        print("    s_end:", lane_s_range.s_range().s1())
    print("Rule States:")
    for state in rule_of_interest.states():
        print("  State ID:", state.value)

    # Intersection
    print("************ Intersection Details ************")
    intersection_book = road_network.intersection_book()
    # Find the intersection that contains the rule of interest.
    # You can use other methods to find intersections as needed:
    # - Via TrafficLight::id()
    # - Via Inertial Position
    intersection = intersection_book.FindIntersection(rule_of_interest.id())
    # Directly obtains the current phase of the intersection. (This is a convenience method that uses the PhaseProvider
    # and PhaseRingBook under the hood).
    current_phase_result = intersection.Phase()
    current_phase_id = current_phase_result.state
    next_phase_id = current_phase_result.next.state
    print("Intersection ID:", intersection.id())
    print("Current Phase ID:", current_phase_id.string())
    print("Next Phase ID:", next_phase_id.string())

    # To get the discrete value rule states of the intersection we can query it directly.
    # Similar to the bulb states.
    discrete_value_rule_states = intersection.DiscreteValueRuleStates()
    bulb_states = intersection.bulb_states()
    print("Discrete Value Rule States:")
    print_discrete_value_rule_states(discrete_value_rule_states)
    print("Bulb States:")
    print_bulb_states(bulb_states)


    print("************ Iterate to next phase ************")
    # As there are two phases in this example, we can just swap between them.
    intersection.SetPhase(phase_id=next_phase_id, next_phase=current_phase_id)
    # Now we check the updated phase.
    updated_phase_result = intersection.Phase()
    updated_phase_id = updated_phase_result.state
    updated_next_phase_id = updated_phase_result.next.state
    print("Updated Phase ID:", updated_phase_id.string())
    print("Updated Next Phase ID:", updated_next_phase_id.string())
    discrete_value_rule_states = intersection.DiscreteValueRuleStates()
    bulb_states = intersection.bulb_states()
    print("Discrete Value Rule States:")
    print_discrete_value_rule_states(discrete_value_rule_states)
    print("Bulb States:")
    print_bulb_states(bulb_states)


    # ALTERNATIVELY: Relying manually on the phase ring and phase provider.
    print("************ ALTERNATIVE USING PHASE RING AND PHASE PROVIDER ************")
    print("************ Phase Ring Details ************")
    prb = road_network.phase_ring_book()
    phase_ring_of_interest = prb.FindPhaseRing(rule_id)
    print("Phase Ring ID:", phase_ring_of_interest.id())

    phase_provider = road_network.phase_provider()
    phase_result = phase_provider.GetPhase(phase_ring_of_interest.id())
    current_phase_id = phase_result.state
    print("Current Phase ID:", current_phase_id.string())
    next_phase_id = phase_result.next.state
    print("Next Phase ID:", next_phase_id.string())

    # Phase
    print("************ Phase Details ************")
    print("Current Phase ID:", current_phase_id.string())
    current_phase = phase_ring_of_interest.GetPhase(current_phase_id)
    print_phase_details(current_phase)



if __name__ == "__main__":
    main()
