##############################################################################
# Documentation
##############################################################################

"""Demonstrate various inertial -> road apis"""

##############################################################################
# Imports
##############################################################################

import os

import maliput

##############################################################################
# Main
##############################################################################

def main():
    # Refer to https://maliput.readthedocs.io/en/latest/api_documentation.html#
    # if you need to information c++ interfaces that are hidden behind python
    # bindings.

    filepath = os.path.join(os.path.dirname(__file__), "xodr", "TShapeRoad.xodr")

    params = { "opendrive_file": filepath }

    road_network = maliput.plugin.create_road_network("maliput_malidrive", params)
    road_geometry = road_network.road_geometry()

    inertial_pos = maliput.api.InertialPosition(0, 0, 0)
    road_pos = road_geometry.ToRoadPosition(inertial_pos)

    # Print the results
    print("")
    print(f"Candidate Inertial Position: {inertial_pos.xyz()}")
    print("")
    print(f"Nearest Inertial Position (Cartesian): {road_pos.nearest_position.xyz()}")
    print(f"  Road Position - Lane ID: {road_pos.road_position.lane.id()}")
    print(f"  Road Position - Lane Position: {road_pos.road_position.pos.srh()}")
    print(f"  Distance from Requested Position: {road_pos.distance}")
    print("")
    print(f"Nearest Inertial Position (Z): {road_pos.nearest_position.xyz()}")
    print(f"  Road Position - Lane ID: {road_pos.road_position.lane.id()}")
    print(f"  Road Position - Lane Position: {road_pos.road_position.pos.srh()}")
    print(f"  Distance from Requested Position: {road_pos.distance}")
    print("")

