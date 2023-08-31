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

    inertial_pos = maliput.api.InertialPosition(-0.5, 0, 1.0)
    result = road_geometry.ToRoadPosition(inertial_pos)

    # This is somewhat nuanced. If you're in a road volume, you'll get the
    # the candidate inertial position as the result along with whatever
    # lane it is associated with and it's coordinates in srh space.
    # 
    # If you're not in a road volume, this will find the nearest (cartesian
    # distance) inertial point that is in a road volume, etc.
    #
    # Check the distance if you care about that!
    nearest_position = result.nearest_position
    distance = result.distance
    associated = distance < 0.0001  #  how to get this -> road_geometry.linear_tolerance()?

    print("")
    print(f"Candidate Point - Inertial Position: {inertial_pos.xyz()}")
    print("  Inside Road Volume?: {}".format("yes" if associated else "no"))
    if not associated:
        print(f"  Nearest Point - Inertial Position: {nearest_position.xyz()}")
        print(f"  Nearest Point - Distance: {distance}")
    print(f"  Lane ID: {result.road_position.lane.id()}")
    print(f"  Lane Position: {result.road_position.pos.srh()}")
    print("")

