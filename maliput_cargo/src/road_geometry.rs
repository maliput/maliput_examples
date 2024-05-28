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

// This example demonstrates how to create a RoadNetwork object from an OpenDRIVE file and
// exercise the RoadGeometry API.

use clap::Parser;

/// Load an OpenDRIVE file and exercise the RoadGeometry API via ToRoadPosition query.
#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    /// Name of the OpenDRIVE file to load.
    #[arg(short='m' , long, default_value_t = String::from("TShapeRoad"))]
    xodr_map_name: String,
    /// Inertial position x-coordinate.
    #[arg(short='x', long, default_value_t = f64::from(-0.5))]
    i_pos_x: f64,
    /// Inertial position y-coordinate.
    #[arg(short='y', long, default_value_t = f64::from(0.0))]
    i_pos_y: f64,
    /// Inertial position z-coordinate.
    #[arg(short='z', long, default_value_t = f64::from(1.0))]
    i_pos_z: f64,
}


fn main() {
    use std::collections::HashMap;

    let args = Args::parse();
    // Input arguments
    println!("* Using input args: {:?}", args);

    // Get location of odr resources
    let package_location = std::env::var("CARGO_MANIFEST_DIR").unwrap();
    let xodr_path = format!("{}/resources/{}.xodr", package_location, args.xodr_map_name);

    let road_network_properties = HashMap::from([
        ("road_geometry_id", "my_rg_from_rust"),
        ("opendrive_file", xodr_path.as_str()),
        ("linear_tolerance", "0.001"),
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

    // Call to_road_position() method to convert an INERTIAL position to a LANE position.
    // This inertial position is outside the road volume.
    let inertial_position = maliput::api::InertialPosition::new(args.i_pos_x, args.i_pos_y, args.i_pos_z);
    let road_position_result = road_geometry.to_road_position(&inertial_position);

    let associated = road_position_result.distance < road_geometry.linear_tolerance();
    println!("");
    println!("Candidate Point: {:?}", inertial_position);
    println!("\tInside Road Volume?: {}", associated);
    if !associated {
        println!(
            "\tNearest Point: {:?}",
            road_position_result.nearest_position
        );
        println!(
            "\tNearest Point - Distance: {}",
            road_position_result.distance
        );
    }
    println!(
        "\tLane ID: {}",
        road_position_result.road_position.lane().id()
    );
    println!(
        "\tLane Position: {}",
        road_position_result.road_position.pos()
    );
    println!("");
}
