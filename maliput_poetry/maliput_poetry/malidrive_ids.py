##############################################################################
# Documentation
##############################################################################

"""Demonstrate the association between malidrive and opendrive lane ids."""

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
    inertial_position = maliput.api.InertialPosition(-58.32, 106.50, 2.2)
    result = road_geometry.ToRoadPosition(inertial_position)
    lane = result.road_position.lane

    print("")
    print("Malidrive")
    print(f"  Lane ID: {lane.id()}")
    print("")
    # TODO(daniel.stonier) parse and print these from the XML itself
    print("OpenDrive")
    print('  <road name="1" length="271.327412287" id="1" junction="-1">')
    print('    ...')
    print('    <lanes>')
    print('      <laneSection s="0.0">')
    print('        ...')
    print("")