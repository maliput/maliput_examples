import maliput

filepath = 'TShapeRoad.xodr'
params = {
    "opendrive_file": filepath,
}

rn = maliput.plugin.create_road_network("maliput_malidrive", params)
rg = rn.road_geometry()

inertial_pos = maliput.api.InertialPosition(0, 0, 0)
road_pos = rg.ToRoadPosition(inertial_pos)

# Print the results.
print("Nearest position: " + str(road_pos.nearest_position.xyz()))
print("Road position - lane id: " + str(road_pos.road_position.lane.id()))
print("Road position - lane position" + str(road_pos.road_position.pos.srh()))
print("Distance: " + str(road_pos.distance))
