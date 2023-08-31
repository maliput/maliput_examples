##############################################################################
# Documentation
##############################################################################

"""Extract the height from different points in a lane with superelevation."""

##############################################################################
# Imports
##############################################################################

import os

import maliput

##############################################################################
# Main
##############################################################################

def main():
    filepath = os.path.join(os.path.dirname(__file__), "xodr", "SShapeSuperelevatedRoad.xodr")

    params = { "opendrive_file": filepath }

    road_network = maliput.plugin.create_road_network("maliput_malidrive", params)
    road_geometry = road_network.road_geometry()

    inertial_pos = maliput.api.InertialPosition(-58.32, 106.50, 0)
    result = road_geometry.ToRoadPosition(inertial_pos)
    road_position = result.road_position
    nearest_position = result.nearest_position
    to_the_side_lane_pos = maliput.api.LanePosition(
        road_position.pos.s(),
        road_position.pos.r() + 1.0,
        road_position.pos.h()
    )
    to_the_side_pos = road_position.lane.ToInertialPosition(to_the_side_lane_pos)

    print("")
    print(f"Candidate Inertial Position: {inertial_pos.xyz()}")
    print(f"Nearest Inertial Position (Cartesian): {nearest_position.xyz()}")
    print(f"  Road Position - Lane ID: {lane.id()}")
    print(f"  Road Position - Lane Position: {road_position.pos.srh()}")
    print("")
    print(f"Sliding Up The Slope (+1.0m)")
    print(f"  New Inertial Position: {to_the_side_pos.xyz()}")
    print("")
 