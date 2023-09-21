/*****************************************************************************
 * License: BSD-3
 * URL: https://github.com/stonier/maliput_examples/blob/main/LICENSE
*****************************************************************************/

/*****************************************************************************
** Includes
*****************************************************************************/

#include <iostream>

#include <maliput/api/lane.h>
#include <maliput_malidrive/builder/road_network_builder.h>
#include <maliput_malidrive/loader/loader.h>

/*****************************************************************************
** Main
*****************************************************************************/

int main()
{
    // load the road network
    std::map<std::string, std::string> road_network_configuration;
    road_network_configuration.emplace("opendrive_file", "resources/SShapeSuperelevatedRoad.xodr");
    auto road_network = malidrive::loader::Load<malidrive::builder::RoadNetworkBuilder>(
        road_network_configuration
    );

    // get the geometry layer
    const maliput::api::RoadGeometry* road_geometry = road_network->road_geometry();

    // TODO(daniel.stonier): Having to set 2.2 here to land in the road's volume
    // Could use a new api so that I can fetch it without having to know the
    // approximate z-value.
    maliput::api::InertialPosition inertial_position{-58.32, 106.50, 2.2};
    maliput::api::RoadPositionResult result = road_geometry->ToRoadPosition(inertial_position);
    auto road_position = result.road_position;
    const maliput::api::Lane* lane = road_position.lane;
    bool associated = result.distance < road_geometry->linear_tolerance();
    if (!associated) {
        std::cout << "Candidate Point is not associated with a road volume, aborting" << std::endl;
        return 1;
    }
    auto on_the_surface_pos = lane->ToInertialPosition(
        maliput::api::LanePosition(
            road_position.pos.s(),
            road_position.pos.r(),
            0.0  // pin it to the manifold
        )
    );
    // TODO(daniel.stonier): check that it is still a valid lane point
    auto to_the_side_pos = lane->ToInertialPosition(
        maliput::api::LanePosition(
            road_position.pos.s(),
            road_position.pos.r() + 1.0,
            0.0  // pin it to the manifold
        )
    );
  
    std::cout << std::endl;
    std::cout << "Candidate Inertial Position: " << inertial_position.xyz() << std::endl;
    std::cout << "  Surface Position: " << on_the_surface_pos.xyz() << std::endl;
    std::cout << std::endl;
    std::cout << "Sliding Up The Slope (+1.0m)" << std::endl;
    std::cout << "  Surface Position: " << to_the_side_pos.xyz() << std::endl;
    std::cout << std::endl;

    std::cout << "May you be blessed with a tickle from his noodly appendages" << std::endl;

    return 0;
}
