// BSD 3-Clause License
//
// Copyright (c) 2024, Woven by Toyota.
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// * Redistributions of source code must retain the above copyright notice, this
//   list of conditions and the following disclaimer.
//
// * Redistributions in binary form must reproduce the above copyright notice,
//   this list of conditions and the following disclaimer in the documentation
//   and/or other materials provided with the distribution.
//
// * Neither the name of the copyright holder nor the names of its
//   contributors may be used to endorse or promote products derived from
//   this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
// FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
// DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
// CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
// OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


fn main() {
    use std::collections::HashMap;

    // The ResourceManager is a convenient method for getting the path to the resources of the backends.
    // In this case, we are getting the path to the LoopRoadPedestrianCrosswalk.xodr file from the maliput_malidrive backend.
    // And then using it to create a RoadNetwork.
    let rm = maliput::ResourceManager::new();
    let xodr_path = rm
        .get_resource_path_by_name("maliput_malidrive", "LoopRoadPedestrianCrosswalk.xodr")
        .unwrap();
    let yaml_path = rm
        .get_resource_path_by_name("maliput_malidrive", "LoopRoadPedestrianCrosswalk.yaml")
        .unwrap();

    // Loading parameters of the road network for the maliput malidrive backend.
    // See https://maliput.readthedocs.io/en/latest/road_network_parameters.html for more information.
    let road_network_properties = HashMap::from([
        ("road_geometry_id", "my_rg_from_rust"),
        ("linear_tolerance", "0.001"),
        ("opendrive_file", xodr_path.to_str().unwrap()),
        ("rule_registry", yaml_path.to_str().unwrap()),
        ("road_rule_book", yaml_path.to_str().unwrap()),
        ("traffic_light_book", yaml_path.to_str().unwrap()),
        ("phase_ring_book", yaml_path.to_str().unwrap()),
        ("intersection_book", yaml_path.to_str().unwrap()),
    ]);

    let road_network =
        maliput::api::RoadNetwork::new("maliput_malidrive", &road_network_properties);
    let road_geometry = road_network.road_geometry();

    // Exercise the RoadGeometry API.
    println!("linear_tolerance: {}", road_geometry.linear_tolerance());
    println!("angular_tolerance: {}", road_geometry.angular_tolerance());
    println!("num_junctions: {}", road_geometry.num_junctions());

    let lanes = road_geometry.get_lanes();
    println!("num_lanes: {}", lanes.len());
    println!("lanes: ");
    for lane in lanes {
        println!("\tlane id: {}", lane.id());
    }

    // Get the traffic lights from the road network.
    let traffic_lights = road_network.traffic_light_book();
    println!("num_traffic_lights: {}", traffic_lights.traffic_lights().len());
    println!("traffic_lights: ");
    for traffic_light in traffic_lights.traffic_lights() {
        println!("\ttraffic_light id: {}", traffic_light.id());
        println!("\t\tposition: {}", traffic_light.position_road_network());
        println!("\t\torientation: {}", traffic_light.orientation_road_network().rpy().vector());
        println!("\t\tbulb_groups: ");
        for bulb_group in traffic_light.bulb_groups() {
            println!("\t\t\tbulb_group id: {}", bulb_group.id());
            for bulb in bulb_group.bulbs() {
                println!("\t\t\t\tbulb id: {}", bulb.id());
                println!("\t\t\t\t\tstates: {:?}", bulb.states());
            }
        }
    }

}
