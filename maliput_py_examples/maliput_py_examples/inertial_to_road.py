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

    rn = maliput.plugin.create_road_network("maliput_malidrive", params)
    rg = rn.road_geometry()

    inertial_pos = maliput.api.InertialPosition(0, 0, 0)
    road_pos = rg.ToRoadPosition(inertial_pos)

    # Print the results
    print(f"Inertial position: {inertial_pos.xyz()}")
    print(f"Nearest position: {road_pos.nearest_position.xyz()}")
    print(f"Road position - lane id: {road_pos.road_position.lane.id()}")
    print(f"Road position - lane position: {road_pos.road_position.pos.srh()}")
    print(f"Distance: {road_pos.distance}")
