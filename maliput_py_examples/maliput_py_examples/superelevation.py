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

    # TODO(daniel.stonier): Having to set 2.2 here to get in a road volume
    # so it find the relevant
    inertial_pos = maliput.api.InertialPosition(-58.32, 106.50, 2.2)
    result = road_geometry.ToRoadPosition(inertial_pos)
    road_position = result.road_position
    lane = road_position.lane
    associated = result.distance < 0.0001  #  how to get this -> road_geometry.linear_tolerance()?
    if not associated:
        print("Candidate Point is not associated with a road volume, aborting")

    on_the_surface_pos = lane.ToInertialPosition(
        maliput.api.LanePosition(
            road_position.pos.s(),
            road_position.pos.r(),
            0.0  # pin it to the manifold
        )
    )
    # TODO(daniel.stonier): check that it is still a valid lane point
    to_the_side_pos = lane.ToInertialPosition(
        maliput.api.LanePosition(
            road_position.pos.s(),
            road_position.pos.r() + 1.0,
            0.0  # pin it to the manifold
        )
    )

    print("")
    print(f"Candidate Inertial Position: {inertial_pos.xyz()}")
    print(f"  Surface Position: {on_the_surface_pos.xyz()}")
    print("")
    print(f"Sliding Up The Slope (+1.0m)")
    print(f"  Surface Position: {to_the_side_pos.xyz()}")
    print("")
 